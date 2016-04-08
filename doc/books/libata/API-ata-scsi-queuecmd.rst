
.. _API-ata-scsi-queuecmd:

=================
ata_scsi_queuecmd
=================

*man ata_scsi_queuecmd(9)*

*4.6.0-rc1*

Issue SCSI cdb to libata-managed device


Synopsis
========

.. c:function:: int ata_scsi_queuecmd( struct Scsi_Host * shost, struct scsi_cmnd * cmd )

Arguments
=========

``shost``
    SCSI host of command to be sent

``cmd``
    SCSI command to be sent


Description
===========

In some cases, this function translates SCSI commands into ATA taskfiles, and queues the taskfiles to be sent to hardware. In other cases, this function simulates a SCSI device by
evaluating and responding to certain SCSI commands. This creates the overall effect of ATA and ATAPI devices appearing as SCSI devices.


LOCKING
=======

ATA host lock


RETURNS
=======

Return value from ``__ata_scsi_queuecmd`` if ``cmd`` can be queued, 0 otherwise.
