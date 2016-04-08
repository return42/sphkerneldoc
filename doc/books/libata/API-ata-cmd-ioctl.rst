
.. _API-ata-cmd-ioctl:

=============
ata_cmd_ioctl
=============

*man ata_cmd_ioctl(9)*

*4.6.0-rc1*

Handler for HDIO_DRIVE_CMD ioctl


Synopsis
========

.. c:function:: int ata_cmd_ioctl( struct scsi_device * scsidev, void __user * arg )

Arguments
=========

``scsidev``
    Device to which we are issuing command

``arg``
    User provided data for issuing command


LOCKING
=======

Defined by the SCSI layer. We don't really care.


RETURNS
=======

Zero on success, negative errno on error.
