.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-start-stop-xlat:

========================
ata_scsi_start_stop_xlat
========================

*man ata_scsi_start_stop_xlat(9)*

*4.6.0-rc5*

Translate SCSI START STOP UNIT command


Synopsis
========

.. c:function:: unsigned int ata_scsi_start_stop_xlat( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    Storage for translated ATA taskfile


Description
===========

Sets up an ATA taskfile to issue STANDBY (to stop) or READ VERIFY (to
start). Perhaps these commands should be preceded by CHECK POWER MODE to
see what power mode the device is already in. [See SAT revision 5 at
www.t10.org]


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
