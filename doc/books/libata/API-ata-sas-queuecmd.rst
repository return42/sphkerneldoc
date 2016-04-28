.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-sas-queuecmd:

================
ata_sas_queuecmd
================

*man ata_sas_queuecmd(9)*

*4.6.0-rc5*

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

Return value from ``__ata_scsi_queuecmd`` if ``cmd`` can be queued, 0
otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
