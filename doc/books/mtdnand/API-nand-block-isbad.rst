.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-block-isbad:

================
nand_block_isbad
================

*man nand_block_isbad(9)*

*4.6.0-rc5*

[MTD Interface] Check if block at offset is bad


Synopsis
========

.. c:function:: int nand_block_isbad( struct mtd_info * mtd, loff_t offs )

Arguments
=========

``mtd``
    MTD device structure

``offs``
    offset relative to mtd start


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
