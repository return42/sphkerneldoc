.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-memory-bbt:

===============
nand_memory_bbt
===============

*man nand_memory_bbt(9)*

*4.6.0-rc5*

[GENERIC] create a memory based bad block table


Synopsis
========

.. c:function:: int nand_memory_bbt( struct mtd_info * mtd, struct nand_bbt_descr * bd )

Arguments
=========

``mtd``
    MTD device structure

``bd``
    descriptor for the good/bad block search pattern


Description
===========

The function creates a memory based bbt by scanning the device for
manufacturer / software marked good / bad blocks.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
