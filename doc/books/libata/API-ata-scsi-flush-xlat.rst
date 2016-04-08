
.. _API-ata-scsi-flush-xlat:

===================
ata_scsi_flush_xlat
===================

*man ata_scsi_flush_xlat(9)*

*4.6.0-rc1*

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
