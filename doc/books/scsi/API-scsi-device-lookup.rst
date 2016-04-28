.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-device-lookup:

==================
scsi_device_lookup
==================

*man scsi_device_lookup(9)*

*4.6.0-rc5*

find a device given the host


Synopsis
========

.. c:function:: struct scsi_device * scsi_device_lookup( struct Scsi_Host * shost, uint channel, uint id, u64 lun )

Arguments
=========

``shost``
    SCSI host pointer

``channel``
    SCSI channel (zero if only one channel)

``id``
    SCSI target number (physical unit number)

``lun``
    SCSI Logical Unit Number


Description
===========

Looks up the scsi_device with the specified ``channel``, ``id``,
``lun`` for a given host. The returned scsi_device has an additional
reference that needs to be released with scsi_device_put once you're
done with it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
