.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-read-native-max-address:

===========================
ata_read_native_max_address
===========================

*man ata_read_native_max_address(9)*

*4.6.0-rc5*

Read native max address


Synopsis
========

.. c:function:: int ata_read_native_max_address( struct ata_device * dev, u64 * max_sectors )

Arguments
=========

``dev``
    target device

``max_sectors``
    out parameter for the result native max address


Description
===========

Perform an LBA48 or LBA28 native size query upon the device in question.


RETURNS
=======

0 on success, -EACCES if command is aborted by the drive. -EIO on other
errors.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
