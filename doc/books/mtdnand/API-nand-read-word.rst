.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-read-word:

==============
nand_read_word
==============

*man nand_read_word(9)*

*4.6.0-rc5*

[DEFAULT] read one word from the chip


Synopsis
========

.. c:function:: u16 nand_read_word( struct mtd_info * mtd )

Arguments
=========

``mtd``
    MTD device structure


Description
===========

Default read function for 16bit buswidth without endianness conversion.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
