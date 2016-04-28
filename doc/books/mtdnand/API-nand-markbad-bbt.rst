.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-markbad-bbt:

================
nand_markbad_bbt
================

*man nand_markbad_bbt(9)*

*4.6.0-rc5*

[NAND Interface] Mark a block bad in the BBT


Synopsis
========

.. c:function:: int nand_markbad_bbt( struct mtd_info * mtd, loff_t offs )

Arguments
=========

``mtd``
    MTD device structure

``offs``
    offset of the bad block


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
