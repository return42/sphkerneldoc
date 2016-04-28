.. -*- coding: utf-8; mode: rst -*-

.. _API-iscsi-block-scsi-eh:

===================
iscsi_block_scsi_eh
===================

*man iscsi_block_scsi_eh(9)*

*4.6.0-rc5*

block scsi eh until session state has transistioned


Synopsis
========

.. c:function:: int iscsi_block_scsi_eh( struct scsi_cmnd * cmd )

Arguments
=========

``cmd``
    scsi cmd passed to scsi eh handler


Description
===========

If the session is down this function will wait for the recovery timer to
fire or for the session to be logged back in. If the recovery timer
fires then FAST_IO_FAIL is returned. The caller should pass this error
value to the scsi eh.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
