
.. _API-scsi-device-get:

===============
scsi_device_get
===============

*man scsi_device_get(9)*

*4.6.0-rc1*

get an additional reference to a scsi_device


Synopsis
========

.. c:function:: int scsi_device_get( struct scsi_device * sdev )

Arguments
=========

``sdev``
    device to get a reference to


Description
===========

Gets a reference to the scsi_device and increments the use count of the underlying LLDD module. You must hold host_lock of the parent Scsi_Host or already have a reference when
calling this.

This will fail if a device is deleted or cancelled, or when the LLD module is in the process of being unloaded.
