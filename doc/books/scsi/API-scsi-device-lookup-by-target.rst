.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-device-lookup-by-target:

============================
scsi_device_lookup_by_target
============================

*man scsi_device_lookup_by_target(9)*

*4.6.0-rc5*

find a device given the target


Synopsis
========

.. c:function:: struct scsi_device * scsi_device_lookup_by_target( struct scsi_target * starget, u64 lun )

Arguments
=========

``starget``
    SCSI target pointer

``lun``
    SCSI Logical Unit Number


Description
===========

Looks up the scsi_device with the specified ``lun`` for a given
``starget``. The returned scsi_device has an additional reference that
needs to be released with scsi_device_put once you're done with it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
