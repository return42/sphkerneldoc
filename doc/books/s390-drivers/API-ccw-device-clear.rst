
.. _API-ccw-device-clear:

================
ccw_device_clear
================

*man ccw_device_clear(9)*

*4.6.0-rc1*

terminate I/O request processing


Synopsis
========

.. c:function:: int ccw_device_clear( struct ccw_device * cdev, unsigned long intparm )

Arguments
=========

``cdev``
    target ccw device

``intparm``
    interruption parameter; value is only used if no I/O is outstanding, otherwise the intparm associated with the I/O request is returned


Description
===========

``ccw_device_clear`` calls csch on ``cdev``'s subchannel.


Returns
=======

``0`` on success, -``ENODEV`` on device not operational, -``EINVAL`` on invalid device state.


Context
=======

Interrupts disabled, ccw device lock held
