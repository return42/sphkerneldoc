.. -*- coding: utf-8; mode: rst -*-

.. _API-search-read-bbts:

================
search_read_bbts
================

*man search_read_bbts(9)*

*4.6.0-rc5*

[GENERIC] scan the device for bad block table(s)


Synopsis
========

.. c:function:: void search_read_bbts( struct mtd_info * mtd, uint8_t * buf, struct nand_bbt_descr * td, struct nand_bbt_descr * md )

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

Search and read the bad block table(s).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
