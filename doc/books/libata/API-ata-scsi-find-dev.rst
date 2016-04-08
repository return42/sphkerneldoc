
.. _API-ata-scsi-find-dev:

=================
ata_scsi_find_dev
=================

*man ata_scsi_find_dev(9)*

*4.6.0-rc1*

lookup ata_device from scsi_cmnd


Synopsis
========

.. c:function:: struct ata_device ⋆ ata_scsi_find_dev( struct ata_port * ap, const struct scsi_device * scsidev )

Arguments
=========

``ap``
    ATA port to which the device is attached

``scsidev``
    SCSI device from which we derive the ATA device


Description
===========

Given various information provided in struct scsi_cmnd, map that onto an ATA bus, and using that mapping determine which ata_device is associated with the SCSI command to be
sent.


LOCKING
=======

spin_lock_irqsave(host lock)


RETURNS
=======

Associated ATA device, or ``NULL`` if not found.
