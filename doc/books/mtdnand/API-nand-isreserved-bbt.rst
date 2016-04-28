.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-isreserved-bbt:

===================
nand_isreserved_bbt
===================

*man nand_isreserved_bbt(9)*

*4.6.0-rc5*

[NAND Interface] Check if a block is reserved


Synopsis
========

.. c:function:: int nand_isreserved_bbt( struct mtd_info * mtd, loff_t offs )

Arguments
=========

``mtd``
    MTD device structure

``offs``
    offset in the device


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
