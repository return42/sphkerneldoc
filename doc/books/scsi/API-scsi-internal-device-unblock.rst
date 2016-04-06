
.. _API-scsi-internal-device-unblock:

============================
scsi_internal_device_unblock
============================

*man scsi_internal_device_unblock(9)*

*4.6.0-rc1*

resume a device after a block request


Synopsis
========

.. c:function:: int scsi_internal_device_unblock( struct scsi_device * sdev, enum scsi_device_state new_state )

Arguments
=========

``sdev``
    device to resume

``new_state``
    state to set devices to after unblocking


Description
===========

Called by scsi lld's or the midlayer to restart the device queue for the previously suspended scsi device. Called from interrupt or normal process context.

Returns zero if successful or error if not.


Notes
=====

This routine transitions the device to the SDEV_RUNNING state or to one of the offline states (which must be a legal transition) allowing the midlayer to goose the queue for this
device.
