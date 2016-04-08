
.. _API-ata-scsiop-mode-sense:

=====================
ata_scsiop_mode_sense
=====================

*man ata_scsiop_mode_sense(9)*

*4.6.0-rc1*

Simulate MODE SENSE 6, 10 commands


Synopsis
========

.. c:function:: unsigned int ata_scsiop_mode_sense( struct ata_scsi_args * args, u8 * rbuf )

Arguments
=========

``args``
    device IDENTIFY data / SCSI command of interest.

``rbuf``
    Response buffer, to which simulated SCSI cmd output is sent.


Description
===========

Simulate MODE SENSE commands. Assume this is invoked for direct access devices (e.g. disks) only. There should be no block descriptor for other device types.


LOCKING
=======

spin_lock_irqsave(host lock)
