
.. _API-scsi-16-lba-len:

===============
scsi_16_lba_len
===============

*man scsi_16_lba_len(9)*

*4.6.0-rc1*

Get LBA and transfer length


Synopsis
========

.. c:function:: void scsi_16_lba_len( const u8 * cdb, u64 * plba, u32 * plen )

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

Calculate LBA and transfer length for 16-byte commands.
