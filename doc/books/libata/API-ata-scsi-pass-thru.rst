
.. _API-ata-scsi-pass-thru:

==================
ata_scsi_pass_thru
==================

*man ata_scsi_pass_thru(9)*

*4.6.0-rc1*

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
