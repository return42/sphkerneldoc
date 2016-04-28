.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-unlock:

===========
nand_unlock
===========

*man nand_unlock(9)*

*4.6.0-rc5*

[REPLACEABLE] unlocks specified locked blocks


Synopsis
========

.. c:function:: int nand_unlock( struct mtd_info * mtd, loff_t ofs, uint64_t len )

Arguments
=========

``mtd``
    mtd info

``ofs``
    offset to start unlock from

``len``
    length to unlock


Description
===========

Returns unlock status.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
