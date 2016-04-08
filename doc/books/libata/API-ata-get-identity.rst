
.. _API-ata-get-identity:

================
ata_get_identity
================

*man ata_get_identity(9)*

*4.6.0-rc1*

Handler for HDIO_GET_IDENTITY ioctl


Synopsis
========

.. c:function:: int ata_get_identity( struct ata_port * ap, struct scsi_device * sdev, void __user * arg )

Arguments
=========

``ap``
    target port

``sdev``
    SCSI device to get identify data for

``arg``
    User buffer area for identify data


LOCKING
=======

Defined by the SCSI layer. We don't really care.


RETURNS
=======

Zero on success, negative errno on error.
