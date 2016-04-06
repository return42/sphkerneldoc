
.. _API-scsi-bios-ptable:

================
scsi_bios_ptable
================

*man scsi_bios_ptable(9)*

*4.6.0-rc1*

Read PC partition table out of first sector of device.


Synopsis
========

.. c:function:: unsigned char ⋆ scsi_bios_ptable( struct block_device * dev )

Arguments
=========

``dev``
    from this device


Description
===========

Reads the first sector from the device and returns ``0x42`` bytes starting at offset ``0x1be``.


Returns
=======

partition table in kmalloc(GFP_KERNEL) memory, or NULL on error.
