# Copyright (c) 2017 Ultimaker B.V.
# Uranium is released under the terms of the LGPLv3 or higher.

import os #To get the ID from a filename.
from typing import Any, Dict, Iterable, Optional

from UM.Logger import Logger
from UM.Settings.ContainerProvider import ContainerProvider #The class we're implementing.
from UM.Settings.DefinitionContainer import DefinitionContainer #To parse JSON files and get their metadata.
from UM.Resources import Resources

##  Provides definition containers from the local installation.
class LocalDefinitionProvider(ContainerProvider):
    ##  Creates the local definition provider.
    #
    #   This creates a cache which translates definition IDs to their file
    #   names.
    def __init__(self):
        super().__init__()

        #Translates definition IDs to the path to where the file is located.
        self._id_to_path = {} # type: Dict[str, str]

        self._updatePathCache()

    ##  Gets the IDs of all local definitions.
    #
    #   \return A sequence of all definition IDs.
    def getAllIds(self) -> Iterable[str]:
        return self._id_to_path.keys()

    def loadContainer(self, container_id: str) -> "ContainerInterface":
        #Find the file name from the cache.
        try:
            filename = self._id_to_path[container_id] #Raises KeyError if container ID does not exist in the (cache of the) files!
        except KeyError:
            #Update the cache. This shouldn't happen or be necessary because the list of definitions never changes during runtime, but let's update the cache just to be sure.
            Logger.log("w", "Couldn't find definition file with ID {container_id}. Refreshing cache from resources and trying again...".format(container_id = container_id))
            self._updatePathCache()
            filename = self._id_to_path[container_id]
            #If we get another KeyError, pass that on up because that's a programming error for sure then.

        #The actual loading.
        container = DefinitionContainer(container_id = container_id)
        with open(filename) as f:
            container.deserialize(f.read())
        return container

    ##  Load the metadata of a specified container.
    #
    #   \param container_id The ID of the container to load the metadata of.
    #   \return The metadata of the specified container, or ``None`` if the
    #   metadata failed to load.
    def loadMetadata(self, container_id: str) -> Optional[Dict[str, Any]]:
        try:
            filename = self._id_to_path[container_id] #Raises KeyError if container ID does not exist in the (cache of the) files!
        except KeyError:
            #Update the cache. This shouldn't happen or be necessary because the list of definitions never changes during runtime, but let's update the cache just to be sure.
            Logger.log("w", "Couldn't find definition file with ID {container_id}. Refreshing cache from resources and trying again...".format(container_id = container_id))
            self._updatePathCache()
            filename = self._id_to_path[container_id]
            #If we get another KeyError, pass that on up because that's a programming error for sure then.

        with open(filename) as f:
            metadata = DefinitionContainer.getMetadataFromSerialized(f.read())
        if metadata is None:
            return None
        metadata["id"] = container_id #Always fill in the ID from the filename, rather than the ID in the metadata itself.
        return metadata

    ##  Updates the cache of paths to definitions.
    #
    #   This way we can more easily load the definition files we want lazily.
    def _updatePathCache(self):
        self._id_to_path = {} #Clear cache first.

        for filename in Resources.getAllResourcesOfType(Resources.DefinitionContainers):
            definition_id = ".".join(os.path.basename(filename).split(".")[:-2]) #Remove the last two extensions.
            self._id_to_path[definition_id] = filename