# Copyright (c) 2015 Ultimaker B.V.
# Uranium is released under the terms of the AGPLv3 or higher.

from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty
from UM.i18n import i18nCatalog
from UM.Message import Message
from UM.Application import Application

i18n_catalog = i18nCatalog("uranium")

class BackendProxy(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self._backend = Application.getInstance().getBackend()
        self._progress = -1;
        if self._backend:
            self._backend.processingProgress.connect(self._onProcessingProgress)

    processingProgress = pyqtSignal(float, arguments = ["amount"])
    
    @pyqtProperty(float, notify = processingProgress)
    def progress(self):
        return self._progress

    def _onProcessingProgress(self, amount):
        self._progress = amount
        self.processingProgress.emit(amount)
