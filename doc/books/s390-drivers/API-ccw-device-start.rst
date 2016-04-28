.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-start:

================
ccw_device_start
================

*man ccw_device_start(9)*

*4.6.0-rc5*

start a s390 channel program


Synopsis
========

.. c:function:: int ccw_device_start( struct ccw_device * cdev, struct ccw1 * cpa, unsigned long intparm, __u8 lpm, unsigned long flags )

Arguments
=========

``cdev``
    target ccw device

``cpa``
    logical start address of channel program

``intparm``
    user specific interruption parameter; will be presented back to
    ``cdev``'s interrupt handler. Allows a device driver to associate
    the interrupt with a particular I/O request.

``lpm``
    defines the channel path to be used for a specific I/O request. A
    value of 0 will make cio use the opm.

``flags``
    additional flags; defines the action to be performed for I/O
    processing.


Description
===========

Start a S/390 channel program. When the interrupt arrives, the IRQ
handler is called, either immediately, delayed (dev-end missing, or
sense required) or never (no IRQ handler registered).


Returns
=======

``0``, if the operation was successful; -``EBUSY``, if the device is
busy, or status pending; -``EACCES``, if no path specified in ``lpm`` is
operational; -``ENODEV``, if the device is not operational.


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
