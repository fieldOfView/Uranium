# Copyright (c) 2015 Ultimaker B.V.
# Uranium is released under the terms of the AGPLv3 or higher.

from UM.Tool import Tool
from UM.Job import Job
from UM.Event import Event, MouseEvent, KeyEvent
from UM.Message import Message
from UM.Scene.ToolHandle import ToolHandle
from UM.Scene.Selection import Selection

from UM.Math.Plane import Plane
from UM.Math.Vector import Vector
from UM.Math.Quaternion import Quaternion

from PyQt5.QtCore import Qt

from UM.Operations.RotateOperation import RotateOperation
from UM.Operations.GroupedOperation import GroupedOperation
from UM.Operations.SetTransformOperation import SetTransformOperation
from UM.Operations.LayFlatOperation import LayFlatOperation

from . import RotateToolHandle

import math
import time

##  Provides the tool to rotate meshes and groups
#
#   The tool exposes a ToolHint to show the rotation angle of the current operation

class RotateTool(Tool):
    def __init__(self):
        super().__init__()
        self._handle = RotateToolHandle.RotateToolHandle()

        self._snap_rotation = True
        self._snap_angle = math.radians(15)

        self._angle = None
        self._angle_update_time = None

        self._shortcut_key = Qt.Key_Z

        self._progress_message = None
        self._iterations = 0
        self._total_iterations = 0
        self._rotating = False
        self.setExposedProperties("ToolHint", "RotationSnap", "RotationSnapAngle", "X", "Y", "Z" )
        self._saved_node_positions = []

    ##  Handle mouse and keyboard events
    #
    #   \param event type(Event)
    def event(self, event):
        super().event(event)

        if event.type == Event.KeyPressEvent and event.key == KeyEvent.ShiftKey:
            # Snap is toggled when pressing the shift button
            self._snap_rotation = (not self._snap_rotation)
            self.propertyChanged.emit()

        if event.type == Event.KeyReleaseEvent and event.key == KeyEvent.ShiftKey:
            # Snap is "toggled back" when releasing the shift button
            self._snap_rotation = (not self._snap_rotation)
            self.propertyChanged.emit()

        if event.type == Event.MousePressEvent and self._controller.getToolsEnabled():
            # Start a rotate operation
            if MouseEvent.LeftButton not in event.buttons:
                return False

            id = self._selection_pass.getIdAtPosition(event.x, event.y)
            if not id:
                return False

            if self._handle.isAxis(id):
                self.setLockedAxis(id)
            else:
                # Not clicked on an axis: do nothing.
                return False

            handle_position = self._handle.getWorldPosition()

            # Save the current positions of the node, as we want to rotate around their current centres
            self._saved_node_positions = []
            for node in Selection.getAllSelectedObjects():
                self._saved_node_positions.append((node, node.getPosition()))

            if id == ToolHandle.XAxis:
                self.setDragPlane(Plane(Vector(1, 0, 0), handle_position.x))
            elif id == ToolHandle.YAxis:
                self.setDragPlane(Plane(Vector(0, 1, 0), handle_position.y))
            elif self._locked_axis == ToolHandle.ZAxis:
                self.setDragPlane(Plane(Vector(0, 0, 1), handle_position.z))
            else:
                self.setDragPlane(Plane(Vector(0, 1, 0), handle_position.y))

            self.setDragStart(event.x, event.y)
            self._rotating = False
            self._angle = 0


        if event.type == Event.MouseMoveEvent:
            # Perform a rotate operation
            if not self.getDragPlane():
                return False

            if not self.getDragStart():
                self.setDragStart(event.x, event.y)

            if not self._rotating:
                self._rotating = True
                self.operationStarted.emit(self)

            handle_position = self._handle.getWorldPosition()

            drag_start = (self.getDragStart() - handle_position).normalized()
            drag_position = self.getDragPosition(event.x, event.y)
            if not drag_position:
                return
            drag_end = (drag_position - handle_position).normalized()

            try:
                angle = math.acos(drag_start.dot(drag_end))
            except ValueError:
                angle = 0

            if self._snap_rotation:
                angle = int(angle / self._snap_angle) * self._snap_angle
                if angle == 0:
                    return

            rotation = None
            if self.getLockedAxis() == ToolHandle.XAxis:
                direction = 1 if Vector.Unit_X.dot(drag_start.cross(drag_end)) > 0 else -1
                rotation = Quaternion.fromAngleAxis(direction * angle, Vector.Unit_X)
            elif self.getLockedAxis() == ToolHandle.YAxis:
                direction = 1 if Vector.Unit_Y.dot(drag_start.cross(drag_end)) > 0 else -1
                rotation = Quaternion.fromAngleAxis(direction * angle, Vector.Unit_Y)
            elif self.getLockedAxis() == ToolHandle.ZAxis:
                direction = 1 if Vector.Unit_Z.dot(drag_start.cross(drag_end)) > 0 else -1
                rotation = Quaternion.fromAngleAxis(direction * angle, Vector.Unit_Z)
            else:
                direction = -1

            # Rate-limit the angle change notification
            # This is done to prevent the UI from being flooded with property change notifications,
            # which in turn would trigger constant repaints.
            new_time = time.monotonic()
            if not self._angle_update_time or new_time - self._angle_update_time > 0.1:
                self._angle_update_time = new_time
                self._angle += direction * angle

                # Rotate around the saved centeres of all selected nodes
                op = GroupedOperation()
                for node, position in self._saved_node_positions:
                    op.addOperation(RotateOperation(node, rotation, rotate_around_point = position))
                op.push()

                self.setDragStart(event.x, event.y)
                self.propertyChanged.emit()

        if event.type == Event.MouseReleaseEvent:
            # Finish a rotate operation
            if self.getDragPlane():
                self.setDragPlane(None)
                self.setLockedAxis(None)
                self._angle = None
                if self._rotating:
                    self.operationStopped.emit(self)
                return True

    ##  Return a formatted angle of the current rotate operation
    #
    #   \return type(String) fully formatted string showing the angle by which the mesh(es) are rotated
    def getToolHint(self):
        return "%d°" % round(math.degrees(self._angle)) if self._angle else None

    ##  Get the state of the "snap rotation to N-degree increments" option
    #
    #   \return type(Boolean)
    def getRotationSnap(self):
        return self._snap_rotation

    ##  Set the state of the "snap rotation to N-degree increments" option
    #
    #   \param snap type(Boolean)
    def setRotationSnap(self, snap):
        if snap != self._snap_rotation:
            self._snap_rotation = snap
            self.propertyChanged.emit()

    ##  Get the number of degrees used in the "snap rotation to N-degree increments" option
    #
    #   \return type(Number)
    def getRotationSnapAngle(self):
        return self._snap_angle

    ##  Set the number of degrees used in the "snap rotation to N-degree increments" option
    #
    #   \param snap type(Number)
    def setRotationSnapAngle(self, angle):
        if angle != self._snap_angle:
            self._snap_angle = angle
            self.propertyChanged.emit()


    def _parseInt(self, str_value):
        try:
            parsed_value = float(str_value)
        except ValueError:
            parsed_value = float(0)
        return parsed_value

    ##  Get X
    #
    #   \return type(float)
    def getX(self):
        if Selection.hasSelection():
            euler_angles = Selection.getSelectedObject(0).getLocalTransformation().getEuler()
            return float(math.degrees(euler_angles.x))
        return 0.0

    ##  Set X
    #
    #   \param x type(float)
    def setX(self, x):
        x = math.radians(self._parseInt(x))
        current_x_angle = Selection.getSelectedObject(0).getLocalTransformation().getEuler().x

        if x != current_x_angle:
            x_angle_change = x - current_x_angle

            rotation = Quaternion.fromAngleAxis(x_angle_change, Vector.Unit_X)

            # Save the current positions of the node, as we want to rotate around their current centres
            self._saved_node_positions = []
            for node in Selection.getAllSelectedObjects():
                self._saved_node_positions.append((node, node.getPosition()))

            # Rate-limit the angle change notification
            # This is done to prevent the UI from being flooded with property change notifications,
            # which in turn would trigger constant repaints.
            new_time = time.monotonic()
            if not self._angle_update_time or new_time - self._angle_update_time > 0.1:
                self._angle_update_time = new_time
                self.propertyChanged.emit()

                # Rotate around the saved centeres of all selected nodes
                op = GroupedOperation()
                for node, position in self._saved_node_positions:
                    op.addOperation(RotateOperation(node, rotation, rotate_around_point = position))
                op.push()

            self.propertyChanged.emit()

    ##  Get Y
    #
    #   \return type(float)
    def getY(self):
        if Selection.hasSelection():
            euler_angles = Selection.getSelectedObject(0).getLocalTransformation().getEuler()
            return float(math.degrees(euler_angles.z))
        return 0.0

    ##  Set Y
    #
    #   \param y type(float)
    def setY(self, y):
        y = math.radians(self._parseInt(y))
        current_y_angle = Selection.getSelectedObject(0).getLocalTransformation().getEuler().z

        if y != current_y_angle:
            y_angle_change = y - current_y_angle

            rotation = Quaternion.fromAngleAxis(y_angle_change, Vector.Unit_Z)

            # Save the current positions of the node, as we want to rotate around their current centres
            self._saved_node_positions = []
            for node in Selection.getAllSelectedObjects():
                self._saved_node_positions.append((node, node.getPosition()))

            # Rate-limit the angle change notification
            # This is done to prevent the UI from being flooded with property change notifications,
            # which in turn would trigger constant repaints.
            new_time = time.monotonic()
            if not self._angle_update_time or new_time - self._angle_update_time > 0.1:
                self._angle_update_time = new_time
                self.propertyChanged.emit()

                # Rotate around the saved centeres of all selected nodes
                op = GroupedOperation()
                for node, position in self._saved_node_positions:
                    op.addOperation(RotateOperation(node, rotation, rotate_around_point = position))
                op.push()

            self.propertyChanged.emit()


    ##  Get Z
    #
    #   \return type(float)
    def getZ(self):
        if Selection.hasSelection():
            euler_angles = Selection.getSelectedObject(0).getLocalTransformation().getEuler()
            return float(math.degrees(euler_angles.y))
        return 0.0

    ##  Set Z
    #
    #   \param z type(float)
    def setZ(self, z):
        z = math.radians(self._parseInt(z))
        current_z_angle = Selection.getSelectedObject(0).getLocalTransformation().getEuler().y

        if z != current_z_angle:
            z_angle_change = z - current_z_angle

            rotation = Quaternion.fromAngleAxis(z_angle_change, Vector.Unit_Y)

            # Save the current positions of the node, as we want to rotate around their current centres
            self._saved_node_positions = []
            for node in Selection.getAllSelectedObjects():
                self._saved_node_positions.append((node, node.getPosition()))

            # Rate-limit the angle change notification
            # This is done to prevent the UI from being flooded with property change notifications,
            # which in turn would trigger constant repaints.
            new_time = time.monotonic()
            if not self._angle_update_time or new_time - self._angle_update_time > 0.1:
                self._angle_update_time = new_time
                self.propertyChanged.emit()

                # Rotate around the saved centeres of all selected nodes
                op = GroupedOperation()
                for node, position in self._saved_node_positions:
                    op.addOperation(RotateOperation(node, rotation, rotate_around_point = position))
                op.push()

            self.propertyChanged.emit()



    ##  Reset the orientation of the mesh(es) to their original orientation(s)
    def resetRotation(self):
        Selection.applyOperation(SetTransformOperation, None, Quaternion(), None)
        self.propertyChanged.emit()

    ##  Initialise and start a LayFlatOperation
    #
    #   Note: The LayFlat functionality is mostly used for 3d printing and should probably be moved into the Cura project
    def layFlat(self):
        self.operationStarted.emit(self)
        self._progress_message = Message("Laying object flat on buildplate...", lifetime = 0, dismissable = False)
        self._progress_message.setProgress(0)

        self._iterations = 0
        self._total_iterations = 0
        for selected_object in Selection.getAllSelectedObjects():
            self._layObjectFlat(selected_object)

        self._progress_message.show()

        operations = Selection.applyOperation(LayFlatOperation)
        for op in operations:
            op.progress.connect(self._layFlatProgress)

        job = LayFlatJob(operations)
        job.finished.connect(self._layFlatFinished)
        job.start()

    ##  Lays the given object flat. The given object can be a group or not.
    def _layObjectFlat(self, selected_object):
        if not selected_object.callDecoration("isGroup"):
            self._total_iterations += len(selected_object.getMeshDataTransformed().getVertices()) * 2
        else:
            for child in selected_object.getChildren():
                self._layObjectFlat(child)

    ##  Called while performing the LayFlatOperation so progress can be shown
    #
    #   Note that the LayFlatOperation rate-limits these callbacks to prevent the UI from being flooded with property change notifications,
    #   \param iterations type(int) number of iterations performed since the last callback
    def _layFlatProgress(self, iterations):
        self._iterations += iterations
        self._progress_message.setProgress(100 * self._iterations / self._total_iterations)

    ##  Called when the LayFlatJob is done running all of its LayFlatOperations
    #
    #   \param job type(LayFlatJob)
    def _layFlatFinished(self, job):
        if self._progress_message:
            self._progress_message.hide()
            self._progress_message = None

        self.operationStopped.emit(self)
        self.propertyChanged.emit()

##  A LayFlatJob bundles multiple LayFlatOperations for multiple selected objects
#
#   The job is executed on its own thread, processing each operation in order, so it does not lock up the GUI.
class LayFlatJob(Job):
    def __init__(self, operations):
        super().__init__()

        self._operations = operations

    def run(self):
        for op in self._operations:
            op.process()
