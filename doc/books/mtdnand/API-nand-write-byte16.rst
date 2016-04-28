.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-write-byte16:

=================
nand_write_byte16
=================

*man nand_write_byte16(9)*

*4.6.0-rc5*

[DEFAULT] write single byte to a chip with width 16


Synopsis
========

.. c:function:: void nand_write_byte16( struct mtd_info * mtd, uint8_t byte )

Arguments
=========

``mtd``
    MTD device structure

``byte``
    value to write


Description
===========

Default function to write a byte to I/O[7:0] on a 16-bit wide chip.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
