
.. _API-scsi-add-single-device:

======================
scsi_add_single_device
======================

*man scsi_add_single_device(9)*

*4.6.0-rc1*

Respond to user request to probe for/add device


Synopsis
========

.. c:function:: int scsi_add_single_device( uint host, uint channel, uint id, uint lun )

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

called by writing “scsi add-single-device” to /proc/scsi/scsi.

does ``scsi_host_lookup`` and either ``user_scan`` if that transport type supports it, or else ``scsi_scan_host_selected``


Note
====

this seems to be aimed exclusively at SCSI parallel busses.
