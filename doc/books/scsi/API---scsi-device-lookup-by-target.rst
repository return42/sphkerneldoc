.. -*- coding: utf-8; mode: rst -*-

.. _API---scsi-device-lookup-by-target:

==============================
__scsi_device_lookup_by_target
==============================

*man __scsi_device_lookup_by_target(9)*

*4.6.0-rc5*

find a device given the target (UNLOCKED)


Synopsis
========

.. c:function:: struct scsi_device * __scsi_device_lookup_by_target( struct scsi_target * starget, u64 lun )

Arguments
=========

``starget``
    SCSI target pointer

``lun``
    SCSI Logical Unit Number


Description
===========

Looks up the scsi_device with the specified ``lun`` for a given
``starget``. The returned scsi_device does not have an additional
reference. You must hold the host's host_lock over this call and any
access to the returned scsi_device. A scsi_device in state SDEV_DEL
is skipped.


Note
====

The only reason why drivers should use this is because they need to
access the device list in irq context. Otherwise you really want to use
scsi_device_lookup_by_target instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
