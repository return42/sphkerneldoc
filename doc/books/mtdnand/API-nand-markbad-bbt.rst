
.. _API-nand-markbad-bbt:

================
nand_markbad_bbt
================

*man nand_markbad_bbt(9)*

*4.6.0-rc1*

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
