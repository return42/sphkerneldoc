.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-block-bad:

==============
nand_block_bad
==============

*man nand_block_bad(9)*

*4.6.0-rc5*

[DEFAULT] Read bad block marker from the chip


Synopsis
========

.. c:function:: int nand_block_bad( struct mtd_info * mtd, loff_t ofs )

Arguments
=========

``mtd``
    MTD device structure

``ofs``
    offset from device start


Description
===========

Check, if the block is bad.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
