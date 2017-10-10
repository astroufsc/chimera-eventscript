import ntpath
import threading
import os
import subprocess
from chimera.interfaces.camera import CameraStatus
from chimera.util.image import ImageUtil, Image
from chimera.controllers.imageserver.util import getImageServer
from chimera.core.chimeraobject import ChimeraObject

import datetime as dt


class EventScript(ChimeraObject):
    __config__ = {
        "camera": "/Camera/0",
        "camera_readoutcomplete_script": None,
    }

    def _getCam(self):
        return self.getManager().getProxy(self["camera"])

    def __init__(self):
        ChimeraObject.__init__(self)

    def __start__(self):
        self._getCam().readoutComplete += self.getProxy()._CameraReadoutCompleteClbk

    def run_script(self, script, proxy, status):
        if status == CameraStatus.OK:

            image_fname = proxy.filename()
            if ':\\' in image_fname:
                modpath = ntpath
            else:
                modpath = os.path
            image_fname = modpath.basename(image_fname)
            image_type = proxy["IMAGETYP"] if "IMAGETYP" in proxy.keys() else "UNKNOWN"
            subprocess.call([os.path.expanduser(script), image_fname, image_type])
        return

    def _CameraReadoutCompleteClbk(self, proxy, status):
        self.log.debug("Acquired CameraReadoutComplete event")
        if self["camera_readoutcomplete_script"] is not None:
            p = threading.Thread(target=self.run_script, args=(self['camera_readoutcomplete_script'], proxy, status))
            p.start()
        else:
            self.log.debug("Skipping camera_readoutcomplete_script is None")

    def __stop__(self):
        pass
