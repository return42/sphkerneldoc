
.. _API-ata-scsi-change-queue-depth:

===========================
ata_scsi_change_queue_depth
===========================

*man ata_scsi_change_queue_depth(9)*

*4.6.0-rc1*

SCSI callback for queue depth config


Synopsis
========

.. c:function:: int ata_scsi_change_queue_depth( struct scsi_device * sdev, int queue_depth )

Arguments
=========

``sdev``
    SCSI device to configure queue depth for

``queue_depth``
    new queue depth


Description
===========

This is libata standard hostt->change_queue_depth callback. SCSI will call into this callback when user tries to set queue depth via sysfs.


LOCKING
=======

SCSI layer (we don't care)


RETURNS
=======

Newly configured queue depth.
