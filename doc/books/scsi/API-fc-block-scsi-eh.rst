.. -*- coding: utf-8; mode: rst -*-

.. _API-fc-block-scsi-eh:

================
fc_block_scsi_eh
================

*man fc_block_scsi_eh(9)*

*4.6.0-rc5*

Block SCSI eh thread for blocked fc_rport


Synopsis
========

.. c:function:: int fc_block_scsi_eh( struct scsi_cmnd * cmnd )

Arguments
=========

``cmnd``
    SCSI command that scsi_eh is trying to recover


Description
===========

This routine can be called from a FC LLD scsi_eh callback. It blocks
the scsi_eh thread until the fc_rport leaves the
FC_PORTSTATE_BLOCKED, or the fast_io_fail_tmo fires. This is
necessary to avoid the scsi_eh failing recovery actions for blocked
rports which would lead to offlined SCSI devices.


Returns
=======

0 if the fc_rport left the state FC_PORTSTATE_BLOCKED. FAST_IO_FAIL
if the fast_io_fail_tmo fired, this should be passed back to
scsi_eh.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
