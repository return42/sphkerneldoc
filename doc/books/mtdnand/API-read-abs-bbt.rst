.. -*- coding: utf-8; mode: rst -*-

.. _API-read-abs-bbt:

============
read_abs_bbt
============

*man read_abs_bbt(9)*

*4.6.0-rc5*

[GENERIC] Read the bad block table starting at a given page


Synopsis
========

.. c:function:: int read_abs_bbt( struct mtd_info * mtd, uint8_t * buf, struct nand_bbt_descr * td, int chip )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    temporary buffer

``td``
    descriptor for the bad block table

``chip``
    read the table for a specific chip, -1 read all chips; applies only
    if NAND_BBT_PERCHIP option is set


Description
===========

Read the bad block table for all chips starting at a given page. We
assume that the bbt bits are in consecutive order.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
