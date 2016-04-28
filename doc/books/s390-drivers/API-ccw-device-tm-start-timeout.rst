.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-tm-start-timeout:

===========================
ccw_device_tm_start_timeout
===========================

*man ccw_device_tm_start_timeout(9)*

*4.6.0-rc5*

perform start function


Synopsis
========

.. c:function:: int ccw_device_tm_start_timeout( struct ccw_device * cdev, struct tcw * tcw, unsigned long intparm, u8 lpm, int expires )

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

``expires``
    time span in jiffies after which to abort request


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
