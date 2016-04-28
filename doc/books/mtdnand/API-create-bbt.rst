.. -*- coding: utf-8; mode: rst -*-

.. _API-create-bbt:

==========
create_bbt
==========

*man create_bbt(9)*

*4.6.0-rc5*

[GENERIC] Create a bad block table by scanning the device


Synopsis
========

.. c:function:: int create_bbt( struct mtd_info * mtd, uint8_t * buf, struct nand_bbt_descr * bd, int chip )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    temporary buffer

``bd``
    descriptor for the good/bad block search pattern

``chip``
    create the table for a specific chip, -1 read all chips; applies
    only if NAND_BBT_PERCHIP option is set


Description
===========

Create a bad block table by scanning the device for the given good/bad
block identify pattern.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
