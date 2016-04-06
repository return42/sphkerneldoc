
.. _API-read-abs-bbts:

=============
read_abs_bbts
=============

*man read_abs_bbts(9)*

*4.6.0-rc1*

[GENERIC] Read the bad block table(s) for all chips starting at a given page


Synopsis
========

.. c:function:: void read_abs_bbts( struct mtd_info * mtd, uint8_t * buf, struct nand_bbt_descr * td, struct nand_bbt_descr * md )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    temporary buffer

``td``
    descriptor for the bad block table

``md``
    descriptor for the bad block table mirror


Description
===========

Read the bad block table(s) for all chips starting at a given page. We assume that the bbt bits are in consecutive order.
