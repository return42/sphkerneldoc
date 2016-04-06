
.. _API-nand-read-word:

==============
nand_read_word
==============

*man nand_read_word(9)*

*4.6.0-rc1*

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
