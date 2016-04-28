.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsiop-inq-80:

=================
ata_scsiop_inq_80
=================

*man ata_scsiop_inq_80(9)*

*4.6.0-rc5*

Simulate INQUIRY VPD page 80, device serial number


Synopsis
========

.. c:function:: unsigned int ata_scsiop_inq_80( struct ata_scsi_args * args, u8 * rbuf )

Arguments
=========

``args``
    device IDENTIFY data / SCSI command of interest.

``rbuf``
    Response buffer, to which simulated SCSI cmd output is sent.


Description
===========

Returns ATA device serial number.


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
