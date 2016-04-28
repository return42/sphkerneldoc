.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-update-bbt:

===============
nand_update_bbt
===============

*man nand_update_bbt(9)*

*4.6.0-rc5*

update bad block table(s)


Synopsis
========

.. c:function:: int nand_update_bbt( struct mtd_info * mtd, loff_t offs )

Arguments
=========

``mtd``
    MTD device structure

``offs``
    the offset of the newly marked block


Description
===========

The function updates the bad block table(s).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
