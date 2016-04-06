
.. _API-scsi-device-resume:

==================
scsi_device_resume
==================

*man scsi_device_resume(9)*

*4.6.0-rc1*

Restart user issued commands to a quiesced device.


Synopsis
========

.. c:function:: void scsi_device_resume( struct scsi_device * sdev )

Arguments
=========

``sdev``
    scsi device to resume.


Description
===========

Moves the device from quiesced back to running and restarts the queues.

Must be called with user context, may sleep.
