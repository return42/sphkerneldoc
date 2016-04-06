
.. _API-nand-isreserved-bbt:

===================
nand_isreserved_bbt
===================

*man nand_isreserved_bbt(9)*

*4.6.0-rc1*

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
