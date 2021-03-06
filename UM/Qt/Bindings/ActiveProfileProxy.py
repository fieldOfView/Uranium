# Copyright (c) 2015 Ultimaker B.V.
# Uranium is released under the terms of the AGPLv3 or higher.

from PyQt5.QtCore import pyqtSlot, pyqtProperty, pyqtSignal, QObject, QVariant, QUrl

from UM.Application import Application
from UM.PluginRegistry import PluginRegistry

class ActiveProfileProxy(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self._setting_values = None
        self._active_profile = None
        Application.getInstance().getMachineManager().activeProfileChanged.connect(self._onActiveProfileChanged)
        self._onActiveProfileChanged()

    activeProfileChanged = pyqtSignal()

    @pyqtProperty(bool, notify = activeProfileChanged)
    def valid(self):
        return self._active_profile != None

    settingValuesChanges = pyqtSignal()
    @pyqtProperty("QVariant", notify = settingValuesChanges)
    def settingValues(self):
        return self._setting_values

    @pyqtSlot(str, "QVariant")
    def setSettingValue(self, key, value):
        if key in self._setting_values and self._setting_values[key] == value:
            return

        self._active_profile.setSettingValue(key, value)

    def _onActiveProfileChanged(self):
        if self._active_profile:
            self._active_profile.settingValueChanged.disconnect(self._onSettingValuesChanged)

        self._active_profile = Application.getInstance().getMachineManager().getActiveProfile()
        self.activeProfileChanged.emit()

        if self._active_profile:
            self._active_profile.settingValueChanged.connect(self._onSettingValuesChanged)
            self._onSettingValuesChanged()

    def _onSettingValuesChanged(self, setting = None):
        self._setting_values = self._active_profile.getAllSettingValues()
        self.settingValuesChanges.emit()

def createActiveProfileProxy(engine, script_engine):
    return ActiveProfileProxy()

