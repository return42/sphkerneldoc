.. -*- coding: utf-8; mode: rst -*-

.. _API---nand-unlock:

=============
__nand_unlock
=============

*man __nand_unlock(9)*

*4.6.0-rc5*

[REPLACEABLE] unlocks specified locked blocks


Synopsis
========

.. c:function:: int __nand_unlock( struct mtd_info * mtd, loff_t ofs, uint64_t len, int invert )

Arguments
=========

``mtd``
    mtd info

``ofs``
    offset to start unlock from

``len``
    length to unlock

``invert``
    when = 0, unlock the range of blocks within the lower and upper
    boundary address when = 1, unlock the range of blocks outside the
    boundaries of the lower and upper boundary address


Description
===========

Returs unlock status.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
