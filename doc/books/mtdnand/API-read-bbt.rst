.. -*- coding: utf-8; mode: rst -*-

.. _API-read-bbt:

========
read_bbt
========

*man read_bbt(9)*

*4.6.0-rc5*

[GENERIC] Read the bad block table starting from page


Synopsis
========

.. c:function:: int read_bbt( struct mtd_info * mtd, uint8_t * buf, int page, int num, struct nand_bbt_descr * td, int offs )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    temporary buffer

``page``
    the starting page

``num``
    the number of bbt descriptors to read

``td``
    the bbt describtion table

``offs``
    block number offset in the table


Description
===========

Read the bad block table starting from page.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
