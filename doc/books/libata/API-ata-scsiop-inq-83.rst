
.. _API-ata-scsiop-inq-83:

=================
ata_scsiop_inq_83
=================

*man ata_scsiop_inq_83(9)*

*4.6.0-rc1*

Simulate INQUIRY VPD page 83, device identity


Synopsis
========

.. c:function:: unsigned int ata_scsiop_inq_83( struct ata_scsi_args * args, u8 * rbuf )

Arguments
=========

``args``
    device IDENTIFY data / SCSI command of interest.

``rbuf``
    Response buffer, to which simulated SCSI cmd output is sent.


Yields two logical unit device identification designators
=========================================================

- vendor specific ASCII containing the ATA serial number - SAT defined “t10 vendor id based” containing ASCII vendor name (“ATA”), model and serial numbers.


LOCKING
=======

spin_lock_irqsave(host lock)
