.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-add-lun:

============
scsi_add_lun
============

*man scsi_add_lun(9)*

*4.6.0-rc5*

allocate and fully initialze a scsi_device


Synopsis
========

.. c:function:: int scsi_add_lun( struct scsi_device * sdev, unsigned char * inq_result, int * bflags, int async )

Arguments
=========

``sdev``
    holds information to be stored in the new scsi_device

``inq_result``
    holds the result of a previous INQUIRY to the LUN

``bflags``
    black/white list flag

``async``
    1 if this device is being scanned asynchronously


Description
===========

Initialize the scsi_device ``sdev``. Optionally set fields based on
values in *\ ``bflags``.


SCSI_SCAN_NO_RESPONSE
=====================

could not allocate or setup a scsi_device


SCSI_SCAN_LUN_PRESENT
=====================

a new scsi_device was allocated and initialized


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
