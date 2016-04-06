
.. _API-nand-update-bbt:

===============
nand_update_bbt
===============

*man nand_update_bbt(9)*

*4.6.0-rc1*

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
