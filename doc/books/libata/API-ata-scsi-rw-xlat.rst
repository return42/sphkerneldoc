.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-rw-xlat:

================
ata_scsi_rw_xlat
================

*man ata_scsi_rw_xlat(9)*

*4.6.0-rc5*

Translate SCSI r/w command into an ATA one


Synopsis
========

.. c:function:: unsigned int ata_scsi_rw_xlat( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Storage for translated ATA taskfile


Description
===========

Converts any of six SCSI read/write commands into the ATA counterpart,
including starting sector (LBA), sector count, and taking into account
the device's LBA48 support.

Commands ``READ_6``, ``READ_10``, ``READ_16``, ``WRITE_6``,
``WRITE_10``, and ``WRITE_16`` are currently supported.


LOCKING
=======

spin_lock_irqsave(host lock)


RETURNS
=======

Zero on success, non-zero on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
