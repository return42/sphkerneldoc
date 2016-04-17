
.. _ccw:

===========
The ccw bus
===========

The ccw bus typically contains the majority of devices available to a s390 system. Named after the channel command word (ccw), the basic command structure used to address its
devices, the ccw bus contains so-called channel attached devices. They are addressed via I/O subchannels, visible on the css bus. A device driver for channel-attached devices,
however, will never interact with the subchannel directly, but only via the I/O device on the ccw bus, the ccw device.


.. _channelIO:

I/O functions for channel-attached devices
==========================================

Some hardware structures have been translated into C structures for use by the common I/O layer and device drivers. For more information on the hardware structures represented
here, please consult the Principles of Operation.


.. toctree::
    :maxdepth: 1

    API-struct-ccw1
    API-struct-erw
    API-struct-erw-eadm
    API-struct-sublog
    API-struct-esw0
    API-struct-esw1
    API-struct-esw2
    API-struct-esw3
    API-struct-esw-eadm
    API-struct-irb
    API-struct-ciw
    API-struct-ccw-dev-id
    API-ccw-dev-id-is-equal
    API-pathmask-to-pos

.. _ccwdev:

ccw devices
===========

Devices that want to initiate channel I/O need to attach to the ccw bus. Interaction with the driver core is done via the common I/O layer, which provides the abstractions of ccw
devices and ccw device drivers.

The functions that initiate or terminate channel I/O all act upon a ccw device structure. Device drivers must not bypass those functions or strange side effects may happen.


.. toctree::
    :maxdepth: 1

    API-struct-ccw-device
    API-struct-ccw-driver
    API-ccw-device-set-offline
    API-ccw-device-set-online
    API-get-ccwdev-by-dev-id
    API-get-ccwdev-by-busid
    API-ccw-driver-register
    API-ccw-driver-unregister
    API-ccw-device-siosl
    API-ccw-device-set-options-mask
    API-ccw-device-set-options
    API-ccw-device-clear-options
    API-ccw-device-is-pathgroup
    API-ccw-device-is-multipath
    API-ccw-device-clear
    API-ccw-device-start-key
    API-ccw-device-start-timeout-key
    API-ccw-device-start
    API-ccw-device-start-timeout
    API-ccw-device-halt
    API-ccw-device-resume
    API-ccw-device-get-ciw
    API-ccw-device-get-path-mask
    API-ccw-device-get-chp-desc
    API-ccw-device-get-id
    API-ccw-device-tm-start-key
    API-ccw-device-tm-start-timeout-key
    API-ccw-device-tm-start
    API-ccw-device-tm-start-timeout
    API-ccw-device-get-mdc
    API-ccw-device-tm-intrg
    API-ccw-device-get-schid

.. _cmf:

The channel-measurement facility
================================

The channel-measurement facility provides a means to collect measurement data which is made available by the channel subsystem for each channel attached device.


.. toctree::
    :maxdepth: 1

    ccw-000-004-003
    API-enable-cmf
    API-disable-cmf
    API-cmf-read
    API-cmf-readall
