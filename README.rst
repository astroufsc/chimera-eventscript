chimera-template plugin
=======================

This is a plugin for the chimera observatory control system.
https://github.com/astroufsc/chimera.

It runs scripts when events are triggered by an instrument.

Usage
-----

Install and configure as the example of Configuration Example section. Some events call the script with arguments as
shown below. Supported events are::

    Event                       chimera.config entry              arguments passed
    --------------------------------------------------------------------------------------
    Camera.readoutComplete()    camera_readoutcomplete_script     image_filename IMAGETYP

Installation
------------

::

    pip install -U git+https://github.com/astroufsc/chimera-eventscript.git


Configuration Example
---------------------
::

    controllers:
       - type: EventScript
         camera: /FakeCamera/fake
         camera_readout_script: ~/.chimera/test_readout.sh


Contact
-------

For more information, contact us on chimera's discussion list:
https://groups.google.com/forum/#!forum/chimera-discuss

Bug reports and patches are welcome and can be sent over our GitHub page:
https://github.com/astroufsc/chimera-eventscript/
