
.. _API-ata-scsiop-read-cap:

===================
ata_scsiop_read_cap
===================

*man ata_scsiop_read_cap(9)*

*4.6.0-rc1*

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
