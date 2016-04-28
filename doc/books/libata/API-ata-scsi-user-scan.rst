.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-user-scan:

==================
ata_scsi_user_scan
==================

*man ata_scsi_user_scan(9)*

*4.6.0-rc5*

indication for user-initiated bus scan


Synopsis
========

.. c:function:: int ata_scsi_user_scan( struct Scsi_Host * shost, unsigned int channel, unsigned int id, u64 lun )

Arguments
=========

``shost``
    SCSI host to scan

``channel``
    Channel to scan

``id``
    ID to scan

``lun``
    LUN to scan


Description
===========

This function is called when user explicitly requests bus scan. Set
probe pending flag and invoke EH.


LOCKING
=======

SCSI layer (we don't care)


RETURNS
=======

Zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
