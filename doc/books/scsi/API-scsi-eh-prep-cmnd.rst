.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-eh-prep-cmnd:

=================
scsi_eh_prep_cmnd
=================

*man scsi_eh_prep_cmnd(9)*

*4.6.0-rc5*

Save a scsi command info as part of error recovery


Synopsis
========

.. c:function:: void scsi_eh_prep_cmnd( struct scsi_cmnd * scmd, struct scsi_eh_save * ses, unsigned char * cmnd, int cmnd_size, unsigned sense_bytes )

Arguments
=========

``scmd``
    SCSI command structure to hijack

``ses``
    structure to save restore information

``cmnd``
    CDB to send. Can be NULL if no new cmnd is needed

``cmnd_size``
    size in bytes of ``cmnd`` (must be <= BLK_MAX_CDB)

``sense_bytes``
    size of sense data to copy. or 0 (if != 0 ``cmnd`` is ignored)


Description
===========

This function is used to save a scsi command information before
re-execution as part of the error recovery process. If ``sense_bytes``
is 0 the command sent must be one that does not transfer any data. If
``sense_bytes`` != 0 ``cmnd`` is ignored and this functions sets up a
REQUEST_SENSE command and cmnd buffers to read ``sense_bytes`` into
``scmd``->sense_buffer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
