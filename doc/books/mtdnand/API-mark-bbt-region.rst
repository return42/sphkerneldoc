.. -*- coding: utf-8; mode: rst -*-

.. _API-mark-bbt-region:

===============
mark_bbt_region
===============

*man mark_bbt_region(9)*

*4.6.0-rc5*

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

The bad block table regions are marked as “bad” to prevent accidental
erasures / writes. The regions are identified by the mark 0x02.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
