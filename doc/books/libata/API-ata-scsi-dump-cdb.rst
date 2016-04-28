.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-dump-cdb:

=================
ata_scsi_dump_cdb
=================

*man ata_scsi_dump_cdb(9)*

*4.6.0-rc5*

dump SCSI command contents to dmesg


Synopsis
========

.. c:function:: void ata_scsi_dump_cdb( struct ata_port * ap, struct scsi_cmnd * cmd )

Arguments
=========

``ap``
    ATA port to which the command was being sent

``cmd``
    SCSI command to dump


Description
===========

Prints the contents of a SCSI command via ``printk``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
