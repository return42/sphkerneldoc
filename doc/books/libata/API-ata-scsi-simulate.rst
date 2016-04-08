
.. _API-ata-scsi-simulate:

=================
ata_scsi_simulate
=================

*man ata_scsi_simulate(9)*

*4.6.0-rc1*

simulate SCSI command on ATA device


Synopsis
========

.. c:function:: void ata_scsi_simulate( struct ata_device * dev, struct scsi_cmnd * cmd )

Arguments
=========

``dev``
    the target device

``cmd``
    SCSI command being sent to device.


Description
===========

Interprets and directly executes a select list of SCSI commands that can be handled internally.


LOCKING
=======

spin_lock_irqsave(host lock)
