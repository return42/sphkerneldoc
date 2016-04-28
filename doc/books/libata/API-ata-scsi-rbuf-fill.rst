.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-rbuf-fill:

==================
ata_scsi_rbuf_fill
==================

*man ata_scsi_rbuf_fill(9)*

*4.6.0-rc5*

wrapper for SCSI command simulators


Synopsis
========

.. c:function:: void ata_scsi_rbuf_fill( struct ata_scsi_args * args, unsigned int (*actor) struct ata_scsi_args *args, u8 *rbuf )

Arguments
=========

``args``
    device IDENTIFY data / SCSI command of interest.

``actor``
    Callback hook for desired SCSI command simulator


Description
===========

Takes care of the hard work of simulating a SCSI command... Mapping the
response buffer, calling the command's handler, and handling the
handler's return value. This return value indicates whether the handler
wishes the SCSI command to be completed successfully (0), or not (in
which case cmd->result and sense buffer are assumed to be set).


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
