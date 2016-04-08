
.. _API-ata-scsi-user-scan:

==================
ata_scsi_user_scan
==================

*man ata_scsi_user_scan(9)*

*4.6.0-rc1*

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

This function is called when user explicitly requests bus scan. Set probe pending flag and invoke EH.


LOCKING
=======

SCSI layer (we don't care)


RETURNS
=======

Zero.
