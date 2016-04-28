.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-block-isreserved:

=====================
nand_block_isreserved
=====================

*man nand_block_isreserved(9)*

*4.6.0-rc5*

[GENERIC] Check if a block is marked reserved.


Synopsis
========

.. c:function:: int nand_block_isreserved( struct mtd_info * mtd, loff_t ofs )

Arguments
=========

``mtd``
    MTD device structure

``ofs``
    offset from device start


Description
===========

Check if the block is marked as reserved.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
