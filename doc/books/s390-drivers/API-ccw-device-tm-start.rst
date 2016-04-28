.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-tm-start:

===================
ccw_device_tm_start
===================

*man ccw_device_tm_start(9)*

*4.6.0-rc5*

perform start function


Synopsis
========

.. c:function:: int ccw_device_tm_start( struct ccw_device * cdev, struct tcw * tcw, unsigned long intparm, u8 lpm )

Arguments
=========

``cdev``
    ccw device on which to perform the start function

``tcw``
    transport-command word to be started

``intparm``
    user defined parameter to be passed to the interrupt handler

``lpm``
    mask of paths to use


Description
===========

Start the tcw on the given ccw device. Return zero on success, non-zero
otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
