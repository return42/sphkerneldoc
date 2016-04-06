
.. _API-scsi-internal-device-block:

==========================
scsi_internal_device_block
==========================

*man scsi_internal_device_block(9)*

*4.6.0-rc1*

internal function to put a device temporarily into the SDEV_BLOCK state


Synopsis
========

.. c:function:: int scsi_internal_device_block( struct scsi_device * sdev )

Arguments
=========

``sdev``
    device to block


Description
===========

Block request made by scsi lld's to temporarily stop all scsi commands on the specified device. Called from interrupt or normal process context.

Returns zero if successful or error if not


Notes
=====

This routine transitions the device to the SDEV_BLOCK state (which must be a legal transition). When the device is in this state, all commands are deferred until the scsi lld
reenables the device with scsi_device_unblock or device_block_tmo fires.
