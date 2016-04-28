.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsiop-read-cap:

===================
ata_scsiop_read_cap
===================

*man ata_scsiop_read_cap(9)*

*4.6.0-rc5*

Simulate READ CAPACITY[ 16] commands


Synopsis
========

.. c:function:: unsigned int ata_scsiop_read_cap( struct ata_scsi_args * args, u8 * rbuf )

Arguments
=========

``args``
    device IDENTIFY data / SCSI command of interest.

``rbuf``
    Response buffer, to which simulated SCSI cmd output is sent.


Description
===========

Simulate READ CAPACITY commands.


LOCKING
=======

None.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
