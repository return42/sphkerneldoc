.. -*- coding: utf-8; mode: rst -*-

.. _API-check-create:

============
check_create
============

*man check_create(9)*

*4.6.0-rc5*

[GENERIC] create and write bbt(s) if necessary


Synopsis
========

.. c:function:: int check_create( struct mtd_info * mtd, uint8_t * buf, struct nand_bbt_descr * bd )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    temporary buffer

``bd``
    descriptor for the good/bad block search pattern


Description
===========

The function checks the results of the previous call to read_bbt and
creates / updates the bbt(s) if necessary. Creation is necessary if no
bbt was found for the chip/device. Update is necessary if one of the
tables is missing or the version nr. of one table is less than the
other.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
