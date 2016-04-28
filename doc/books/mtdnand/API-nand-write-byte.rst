.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-write-byte:

===============
nand_write_byte
===============

*man nand_write_byte(9)*

*4.6.0-rc5*

[DEFAULT] write single byte to chip


Synopsis
========

.. c:function:: void nand_write_byte( struct mtd_info * mtd, uint8_t byte )

Arguments
=========

``mtd``
    MTD device structure

``byte``
    value to write


Description
===========

Default function to write a byte to I/O[7:0]


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
