
.. _API-ccw-device-resume:

=================
ccw_device_resume
=================

*man ccw_device_resume(9)*

*4.6.0-rc1*

resume channel program execution


Synopsis
========

.. c:function:: int ccw_device_resume( struct ccw_device * cdev )

Arguments
=========

``cdev``
    target ccw device


Description
===========

``ccw_device_resume`` calls rsch on ``cdev``'s subchannel.


Returns
=======

``0`` on success, -``ENODEV`` on device not operational, -``EINVAL`` on invalid device state, -``EBUSY`` on device busy or interrupt pending.


Context
=======

Interrupts disabled, ccw device lock held
