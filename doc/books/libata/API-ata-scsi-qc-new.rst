
.. _API-ata-scsi-qc-new:

===============
ata_scsi_qc_new
===============

*man ata_scsi_qc_new(9)*

*4.6.0-rc1*

acquire new ata_queued_cmd reference


Synopsis
========

.. c:function:: struct ata_queued_cmd ⋆ ata_scsi_qc_new( struct ata_device * dev, struct scsi_cmnd * cmd )

Arguments
=========

``dev``
    ATA device to which the new command is attached

``cmd``
    SCSI command that originated this ATA command


Description
===========

Obtain a reference to an unused ata_queued_cmd structure, which is the basic libata structure representing a single ATA command sent to the hardware.

If a command was available, fill in the SCSI-specific portions of the structure with information on the current command.


LOCKING
=======

spin_lock_irqsave(host lock)


RETURNS
=======

Command allocated, or ``NULL`` if none available.
