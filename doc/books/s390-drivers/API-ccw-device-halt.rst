.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-halt:

===============
ccw_device_halt
===============

*man ccw_device_halt(9)*

*4.6.0-rc5*

halt I/O request processing


Synopsis
========

.. c:function:: int ccw_device_halt( struct ccw_device * cdev, unsigned long intparm )

Arguments
=========

``cdev``
    target ccw device

``intparm``
    interruption parameter; value is only used if no I/O is outstanding,
    otherwise the intparm associated with the I/O request is returned


Description
===========

``ccw_device_halt`` calls hsch on ``cdev``'s subchannel.


Returns
=======

``0`` on success, -``ENODEV`` on device not operational, -``EINVAL`` on
invalid device state, -``EBUSY`` on device busy or interrupt pending.


Context
=======

Interrupts disabled, ccw device lock held


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
