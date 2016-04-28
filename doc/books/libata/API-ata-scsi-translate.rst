.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-scsi-translate:

==================
ata_scsi_translate
==================

*man ata_scsi_translate(9)*

*4.6.0-rc5*

Translate then issue SCSI command to ATA device


Synopsis
========

.. c:function:: int ata_scsi_translate( struct ata_device * dev, struct scsi_cmnd * cmd, ata_xlat_func_t xlat_func )

Arguments
=========

``dev``
    ATA device to which the command is addressed

``cmd``
    SCSI command to execute

``xlat_func``
    Actor which translates ``cmd`` to an ATA taskfile


Description
===========

Our ->``queuecommand`` function has decided that the SCSI command issued
can be directly translated into an ATA command, rather than handled
internally.

This function sets up an ata_queued_cmd structure for the SCSI
command, and sends that ata_queued_cmd to the hardware.

The xlat_func argument (actor) returns 0 if ready to execute ATA
command, else 1 to finish translation. If 1 is returned then cmd->result
(and possibly cmd->sense_buffer) are assumed to be set reflecting an
error condition or clean (early) termination.


LOCKING
=======

spin_lock_irqsave(host lock)


RETURNS
=======

0 on success, SCSI_ML_QUEUE_DEVICE_BUSY if the command needs to be
deferred.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
