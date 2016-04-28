.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-set-timeout:

===================
parport_set_timeout
===================

*man parport_set_timeout(9)*

*4.6.0-rc5*

set the inactivity timeout for a device


Synopsis
========

.. c:function:: long parport_set_timeout( struct pardevice * dev, long inactivity )

Arguments
=========

``dev``
    device on a port

``inactivity``
    inactivity timeout (in jiffies)


Description
===========

This sets the inactivity timeout for a particular device on a port. This
affects functions like ``parport_wait_peripheral``. The special value 0
means not to call ``schedule`` while dealing with this device.

The return value is the previous inactivity timeout.

Any callers of ``parport_wait_event`` for this device are woken up.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
