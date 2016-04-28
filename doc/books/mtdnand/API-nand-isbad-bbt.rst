.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-isbad-bbt:

==============
nand_isbad_bbt
==============

*man nand_isbad_bbt(9)*

*4.6.0-rc5*

[NAND Interface] Check if a block is bad


Synopsis
========

.. c:function:: int nand_isbad_bbt( struct mtd_info * mtd, loff_t offs, int allowbbt )

Arguments
=========

``mtd``
    MTD device structure

``offs``
    offset in the device

``allowbbt``
    allow access to bad block table region


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
