
.. _API-nand-block-isbad:

================
nand_block_isbad
================

*man nand_block_isbad(9)*

*4.6.0-rc1*

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
