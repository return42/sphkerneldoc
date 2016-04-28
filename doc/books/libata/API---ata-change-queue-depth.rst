.. -*- coding: utf-8; mode: rst -*-

.. _API---ata-change-queue-depth:

========================
__ata_change_queue_depth
========================

*man __ata_change_queue_depth(9)*

*4.6.0-rc5*

helper for ata_scsi_change_queue_depth


Synopsis
========

.. c:function:: int __ata_change_queue_depth( struct ata_port * ap, struct scsi_device * sdev, int queue_depth )

Arguments
=========

``ap``
    ATA port to which the device change the queue depth

``sdev``
    SCSI device to configure queue depth for

``queue_depth``
    new queue depth


Description
===========

libsas and libata have different approaches for associating a sdev to
its ata_port.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
