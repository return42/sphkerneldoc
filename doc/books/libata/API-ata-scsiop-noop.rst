
.. _API-ata-scsiop-noop:

===============
ata_scsiop_noop
===============

*man ata_scsiop_noop(9)*

*4.6.0-rc1*

Command handler that simply returns success.


Synopsis
========

.. c:function:: unsigned int ata_scsiop_noop( struct ata_scsi_args * args, u8 * rbuf )

Arguments
=========

``args``
    device IDENTIFY data / SCSI command of interest.

``rbuf``
    Response buffer, to which simulated SCSI cmd output is sent.


Description
===========

No operation. Simply returns success to caller, to indicate that the caller should successfully complete this SCSI command.


LOCKING
=======

spin_lock_irqsave(host lock)
