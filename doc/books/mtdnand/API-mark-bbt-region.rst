
.. _API-mark-bbt-region:

===============
mark_bbt_region
===============

*man mark_bbt_region(9)*

*4.6.0-rc1*

[GENERIC] mark the bad block table regions


Synopsis
========

.. c:function:: void mark_bbt_region( struct mtd_info * mtd, struct nand_bbt_descr * td )

Arguments
=========

``mtd``
    MTD device structure

``td``
    bad block table descriptor


Description
===========

The bad block table regions are marked as “bad” to prevent accidental erasures / writes. The regions are identified by the mark 0x02.
