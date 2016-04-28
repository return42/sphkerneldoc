.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-change-queue-depth:

===========================
ata_scsi_change_queue_depth
===========================

*man ata_scsi_change_queue_depth(9)*

*4.6.0-rc5*

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

This is libata standard hostt->change_queue_depth callback. SCSI will
call into this callback when user tries to set queue depth via sysfs.


LOCKING
=======

SCSI layer (we don't care)


RETURNS
=======

Newly configured queue depth.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
