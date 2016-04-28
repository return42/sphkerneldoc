.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsiop-inq-00:

=================
ata_scsiop_inq_00
=================

*man ata_scsiop_inq_00(9)*

*4.6.0-rc5*

Simulate INQUIRY VPD page 0, list of pages


Synopsis
========

.. c:function:: unsigned int ata_scsiop_inq_00( struct ata_scsi_args * args, u8 * rbuf )

Arguments
=========

``args``
    device IDENTIFY data / SCSI command of interest.

``rbuf``
    Response buffer, to which simulated SCSI cmd output is sent.


Description
===========

Returns list of inquiry VPD pages available.


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
