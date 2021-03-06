# Copyright (c) 2015 Ultimaker B.V.
# Uranium is released under the terms of the AGPLv3 or higher.

from UM.Scene.SceneNodeDecorator import SceneNodeDecorator
from UM.Signal import Signal, SignalEmitter
from UM.Application import Application

from copy import deepcopy

##  A decorator that can be used to override individual setting values.
class SettingOverrideDecorator(SceneNodeDecorator, SignalEmitter):
    def __init__(self):
        super().__init__()

        self._settings = {}
        self._setting_values = {}

        self._temp_values = {}

    settingAdded = Signal()
    settingRemoved = Signal()
    settingValueChanged = Signal()

    def getAllSettings(self):
        return self._settings

    def getAllSettingValues(self):
        self._temp_values = {}

        settings = Application.getInstance().getMachineManager().getActiveMachineInstance().getMachineDefinition().getAllSettings(include_machine = False)
        for setting in settings:
            key = setting.getKey()

            if key in self._setting_values:
                self._temp_values[key] = setting.parseValue(self._setting_values[key])
                continue

            self._temp_values[key] = setting.getDefaultValue(self)

        values = self._temp_values
        self._temp_values = {}
        return values

    def addSetting(self, key):
        instance = Application.getInstance().getMachineManager().getActiveMachineInstance()

        setting = instance.getMachineDefinition().getSetting(key)
        if not setting:
            return

        self._settings[key] = setting

        self.settingAdded.emit()
        Application.getInstance().getController().getScene().sceneChanged.emit(self.getNode())

    def setSettingValue(self, key, value):
        if key not in self._settings:
            return

        self._setting_values[key] = value
        self.settingValueChanged.emit(self._settings[key])
        Application.getInstance().getController().getScene().sceneChanged.emit(self.getNode())

    def getSetting(self, key):
        if key not in self._settings:
            parent = self._node.getParent()
            # It could be that the parent does not have a decoration but it's parent parent does. 
            while parent is not None:
                if parent.hasDecoration("getSetting"):
                    return parent.callDecoration("getSetting")
                else:
                    parent = parent.getParent()
        else:
            return self._settings[key]

    def getSettingValue(self, key):
        if key not in self._settings and key not in self._temp_values:
            if self.getNode().callDecoration("getProfile"):
                return self.getNode().callDecoration("getProfile").getSettingValue(key)

            return Application.getInstance().getMachineManager().getActiveProfile().getSettingValue(key)

        if key in self._temp_values:
            return self._temp_values[key]

        setting = self._settings[key]

        if key in self._setting_values:
            return setting.parseValue(self._setting_values[key])

        return setting.getDefaultValue(self)

    def removeSetting(self, key):
        if key not in self._settings:
            return

        del self._settings[key]

        if key in self._setting_values:
            del self._setting_values[key]

        self.settingRemoved.emit()
        Application.getInstance().getController().getScene().sceneChanged.emit(self.getNode())
