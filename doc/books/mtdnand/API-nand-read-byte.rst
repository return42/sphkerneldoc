.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-read-byte:

==============
nand_read_byte
==============

*man nand_read_byte(9)*

*4.6.0-rc5*

[DEFAULT] read one byte from the chip


Synopsis
========

.. c:function:: uint8_t nand_read_byte( struct mtd_info * mtd )

Arguments
=========

``mtd``
    MTD device structure


Description
===========

Default read function for 8bit buswidth


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
