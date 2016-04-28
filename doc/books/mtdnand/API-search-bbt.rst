.. -*- coding: utf-8; mode: rst -*-

.. _API-search-bbt:

==========
search_bbt
==========

*man search_bbt(9)*

*4.6.0-rc5*

[GENERIC] scan the device for a specific bad block table


Synopsis
========

.. c:function:: int search_bbt( struct mtd_info * mtd, uint8_t * buf, struct nand_bbt_descr * td )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    temporary buffer

``td``
    descriptor for the bad block table


Description
===========

Read the bad block table by searching for a given ident pattern. Search
is preformed either from the beginning up or from the end of the device
downwards. The search starts always at the start of a block. If the
option NAND_BBT_PERCHIP is given, each chip is searched for a bbt,
which contains the bad block information of this chip. This is necessary
to provide support for certain DOC devices.

The bbt ident pattern resides in the oob area of the first page in a
block.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
