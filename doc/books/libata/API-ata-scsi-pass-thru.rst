.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-pass-thru:

==================
ata_scsi_pass_thru
==================

*man ata_scsi_pass_thru(9)*

*4.6.0-rc5*

convert ATA pass-thru CDB to taskfile


Synopsis
========

.. c:function:: unsigned int ata_scsi_pass_thru( struct ata_queued_cmd * qc )

Arguments
=========

``qc``
    command structure to be initialized


Description
===========

Handles either 12 or 16-byte versions of the CDB.


RETURNS
=======

Zero on success, non-zero on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
