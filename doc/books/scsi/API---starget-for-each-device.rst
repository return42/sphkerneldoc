.. -*- coding: utf-8; mode: rst -*-

.. _API---starget-for-each-device:

=========================
__starget_for_each_device
=========================

*man __starget_for_each_device(9)*

*4.6.0-rc5*

helper to walk all devices of a target (UNLOCKED)


Synopsis
========

.. c:function:: void __starget_for_each_device( struct scsi_target * starget, void * data, void (*fn) struct scsi_device *, void * )

Arguments
=========

``starget``
    target whose devices we want to iterate over.

``data``
    parameter for callback ``fn``\ ()

``fn``
    callback function that is invoked for each device


Description
===========

This traverses over each device of ``starget``. It does _not_ take a
reference on the scsi_device, so the whole loop must be protected by
shost->host_lock.


Note
====

The only reason why drivers would want to use this is because they need
to access the device list in irq context. Otherwise you really want to
use starget_for_each_device instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
