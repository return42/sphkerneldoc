
.. _API-ata-task-ioctl:

==============
ata_task_ioctl
==============

*man ata_task_ioctl(9)*

*4.6.0-rc1*

Handler for HDIO_DRIVE_TASK ioctl


Synopsis
========

.. c:function:: int ata_task_ioctl( struct scsi_device * scsidev, void __user * arg )

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
