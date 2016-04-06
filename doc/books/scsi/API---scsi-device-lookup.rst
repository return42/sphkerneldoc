
.. _API---scsi-device-lookup:

====================
__scsi_device_lookup
====================

*man __scsi_device_lookup(9)*

*4.6.0-rc1*

find a device given the host (UNLOCKED)


Synopsis
========

.. c:function:: struct scsi_device ⋆ __scsi_device_lookup( struct Scsi_Host * shost, uint channel, uint id, u64 lun )

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

Looks up the scsi_device with the specified ``channel``, ``id``, ``lun`` for a given host. The returned scsi_device does not have an additional reference. You must hold the
host's host_lock over this call and any access to the returned scsi_device.


Note
====

The only reason why drivers would want to use this is because they need to access the device list in irq context. Otherwise you really want to use scsi_device_lookup instead.
