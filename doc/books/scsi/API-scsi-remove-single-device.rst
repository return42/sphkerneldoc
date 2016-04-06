
.. _API-scsi-remove-single-device:

=========================
scsi_remove_single_device
=========================

*man scsi_remove_single_device(9)*

*4.6.0-rc1*

Respond to user request to remove a device


Synopsis
========

.. c:function:: int scsi_remove_single_device( uint host, uint channel, uint id, uint lun )

Arguments
=========

``host``
    user-supplied decimal integer

``channel``
    user-supplied decimal integer

``id``
    user-supplied decimal integer

``lun``
    user-supplied decimal integer


Description
===========

called by writing “scsi remove-single-device” to /proc/scsi/scsi. Does a ``scsi_device_lookup`` and ``scsi_remove_device``
