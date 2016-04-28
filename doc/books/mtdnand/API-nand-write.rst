.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-write:

==========
nand_write
==========

*man nand_write(9)*

*4.6.0-rc5*

[MTD Interface] NAND write with ECC


Synopsis
========

.. c:function:: int nand_write( struct mtd_info * mtd, loff_t to, size_t len, size_t * retlen, const uint8_t * buf )

Arguments
=========

``mtd``
    MTD device structure

``to``
    offset to write to

``len``
    number of bytes to write

``retlen``
    pointer to variable to store the number of written bytes

``buf``
    the data to write


Description
===========

NAND write with ECC.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
