
.. _API-nand-memory-bbt:

===============
nand_memory_bbt
===============

*man nand_memory_bbt(9)*

*4.6.0-rc1*

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

The function creates a memory based bbt by scanning the device for manufacturer / software marked good / bad blocks.
