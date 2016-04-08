
.. _API-ata-scsiop-report-luns:

======================
ata_scsiop_report_luns
======================

*man ata_scsiop_report_luns(9)*

*4.6.0-rc1*

Simulate REPORT LUNS command


Synopsis
========

.. c:function:: unsigned int ata_scsiop_report_luns( struct ata_scsi_args * args, u8 * rbuf )

Arguments
=========

``args``
    device IDENTIFY data / SCSI command of interest.

``rbuf``
    Response buffer, to which simulated SCSI cmd output is sent.


Description
===========

Simulate REPORT LUNS command.


LOCKING
=======

spin_lock_irqsave(host lock)
