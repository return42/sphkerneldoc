.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsiop-report-luns:

======================
ata_scsiop_report_luns
======================

*man ata_scsiop_report_luns(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
