.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-block-when-processing-errors:

=================================
scsi_block_when_processing_errors
=================================

*man scsi_block_when_processing_errors(9)*

*4.6.0-rc5*

Prevent cmds from being queued.


Synopsis
========

.. c:function:: int scsi_block_when_processing_errors( struct scsi_device * sdev )

Arguments
=========

``sdev``
    Device on which we are performing recovery.


Description
===========

We block until the host is out of error recovery, and then check to see
whether the host or the device is offline.


Return value
============

0 when dev was taken offline by error recovery. 1 OK to proceed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
