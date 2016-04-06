
.. _API-scsi-device-quiesce:

===================
scsi_device_quiesce
===================

*man scsi_device_quiesce(9)*

*4.6.0-rc1*

Block user issued commands.


Synopsis
========

.. c:function:: int scsi_device_quiesce( struct scsi_device * sdev )

Arguments
=========

``sdev``
    scsi device to quiesce.


Description
===========

This works by trying to transition to the SDEV_QUIESCE state (which must be a legal transition). When the device is in this state, only special requests will be accepted, all
others will be deferred. Since special requests may also be requeued requests, a successful return doesn't guarantee the device will be totally quiescent.

Must be called with user context, may sleep.

Returns zero if unsuccessful or an error if not.
