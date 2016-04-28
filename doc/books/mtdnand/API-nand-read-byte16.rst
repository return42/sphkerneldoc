.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-read-byte16:

================
nand_read_byte16
================

*man nand_read_byte16(9)*

*4.6.0-rc5*

[DEFAULT] read one byte endianness aware from the chip


Synopsis
========

.. c:function:: uint8_t nand_read_byte16( struct mtd_info * mtd )

Arguments
=========

``mtd``
    MTD device structure


Description
===========

Default read function for 16bit buswidth with endianness conversion.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
