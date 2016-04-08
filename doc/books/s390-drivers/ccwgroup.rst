
.. _ccwgroup:

================
The ccwgroup bus
================

The ccwgroup bus only contains artificial devices, created by the user. Many networking devices (e.g. qeth) are in fact composed of several ccw devices (like read, write and data
channel for qeth). The ccwgroup bus provides a mechanism to create a meta-device which contains those ccw devices as slave devices and can be associated with the netdevice.


.. _ccwgroupdevices:

ccw group devices
=================


.. toctree::
    :maxdepth: 1

    API-struct-ccwgroup-device
    API-struct-ccwgroup-driver
    API-ccwgroup-set-online
    API-ccwgroup-set-offline
    API-ccwgroup-create-dev
    API-ccwgroup-driver-register
    API-ccwgroup-driver-unregister
    API-ccwgroup-probe-ccwdev
    API-ccwgroup-remove-ccwdev
