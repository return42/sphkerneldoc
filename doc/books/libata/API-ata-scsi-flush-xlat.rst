.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-flush-xlat:

===================
ata_scsi_flush_xlat
===================

*man ata_scsi_flush_xlat(9)*

*4.6.0-rc5*

Translate SCSI SYNCHRONIZE CACHE command


Synopsis
========

.. c:function:: unsigned int ata_scsi_flush_xlat( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Storage for translated ATA taskfile


Description
===========

Sets up an ATA taskfile to issue FLUSH CACHE or FLUSH CACHE EXT.


LOCKING
=======

spin_lock_irqsave(host lock)


RETURNS
=======

Zero on success, non-zero on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
