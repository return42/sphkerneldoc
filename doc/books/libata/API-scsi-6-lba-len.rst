.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-6-lba-len:

==============
scsi_6_lba_len
==============

*man scsi_6_lba_len(9)*

*4.6.0-rc5*

Get LBA and transfer length


Synopsis
========

.. c:function:: void scsi_6_lba_len( const u8 * cdb, u64 * plba, u32 * plen )

Arguments
=========

``cdb``
    SCSI command to translate

``plba``
    the LBA

``plen``
    the transfer length


Description
===========

Calculate LBA and transfer length for 6-byte commands.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
