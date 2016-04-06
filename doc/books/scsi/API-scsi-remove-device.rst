
.. _API-scsi-remove-device:

==================
scsi_remove_device
==================

*man scsi_remove_device(9)*

*4.6.0-rc1*

unregister a device from the scsi bus


Synopsis
========

.. c:function:: void scsi_remove_device( struct scsi_device * sdev )

Arguments
=========

``sdev``
    scsi_device to unregister
