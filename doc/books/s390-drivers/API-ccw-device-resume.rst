.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-resume:

=================
ccw_device_resume
=================

*man ccw_device_resume(9)*

*4.6.0-rc5*

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
