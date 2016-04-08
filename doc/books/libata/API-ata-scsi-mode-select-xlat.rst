
.. _API-ata-scsi-mode-select-xlat:

=========================
ata_scsi_mode_select_xlat
=========================

*man ata_scsi_mode_select_xlat(9)*

*4.6.0-rc1*

Simulate MODE SELECT 6, 10 commands


Synopsis
========

.. c:function:: unsigned int ata_scsi_mode_select_xlat( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Storage for translated ATA taskfile


Description
===========

Converts a MODE SELECT command to an ATA SET FEATURES taskfile. Assume this is invoked for direct access devices (e.g. disks) only. There should be no block descriptor for other
device types.


LOCKING
=======

spin_lock_irqsave(host lock)
