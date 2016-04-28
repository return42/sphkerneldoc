.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-verify-xlat:

====================
ata_scsi_verify_xlat
====================

*man ata_scsi_verify_xlat(9)*

*4.6.0-rc5*

Translate SCSI VERIFY command into an ATA one


Synopsis
========

.. c:function:: unsigned int ata_scsi_verify_xlat( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Storage for translated ATA taskfile


Description
===========

Converts SCSI VERIFY command to an ATA READ VERIFY command.


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
