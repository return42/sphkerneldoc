.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsiop-inq-std:

==================
ata_scsiop_inq_std
==================

*man ata_scsiop_inq_std(9)*

*4.6.0-rc5*

Simulate INQUIRY command


Synopsis
========

.. c:function:: unsigned int ata_scsiop_inq_std( struct ata_scsi_args * args, u8 * rbuf )

Arguments
=========

``args``
    device IDENTIFY data / SCSI command of interest.

``rbuf``
    Response buffer, to which simulated SCSI cmd output is sent.


Description
===========

Returns standard device identification data associated with non-VPD
INQUIRY command output.


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
