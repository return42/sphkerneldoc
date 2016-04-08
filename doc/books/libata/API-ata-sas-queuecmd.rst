
.. _API-ata-sas-queuecmd:

================
ata_sas_queuecmd
================

*man ata_sas_queuecmd(9)*

*4.6.0-rc1*

Issue SCSI cdb to libata-managed device


Synopsis
========

.. c:function:: int ata_sas_queuecmd( struct scsi_cmnd * cmd, struct ata_port * ap )

Arguments
=========

``cmd``
    SCSI command to be sent

``ap``
    ATA port to which the command is being sent


RETURNS
=======

Return value from ``__ata_scsi_queuecmd`` if ``cmd`` can be queued, 0 otherwise.
