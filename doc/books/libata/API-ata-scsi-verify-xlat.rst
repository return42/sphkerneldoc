
.. _API-ata-scsi-verify-xlat:

====================
ata_scsi_verify_xlat
====================

*man ata_scsi_verify_xlat(9)*

*4.6.0-rc1*

Translate SCSI VERIFY command into an ATA one


Synopsis
========

.. c:function:: unsigned int ata_scsi_verify_xlat( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Storage for translated ATA taskfile


Description
===========

Converts SCSI VERIFY command to an ATA READ VERIFY command.


LOCKING
=======

spin_lock_irqsave(host lock)


RETURNS
=======

Zero on success, non-zero on error.
