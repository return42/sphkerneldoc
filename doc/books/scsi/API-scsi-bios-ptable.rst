.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-bios-ptable:

================
scsi_bios_ptable
================

*man scsi_bios_ptable(9)*

*4.6.0-rc5*

Read PC partition table out of first sector of device.


Synopsis
========

.. c:function:: unsigned char * scsi_bios_ptable( struct block_device * dev )

Arguments
=========

``dev``
    from this device


Description
===========

Reads the first sector from the device and returns ``0x42`` bytes
starting at offset ``0x1be``.


Returns
=======

partition table in kmalloc(GFP_KERNEL) memory, or NULL on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
