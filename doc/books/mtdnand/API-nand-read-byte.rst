
.. _API-nand-read-byte:

==============
nand_read_byte
==============

*man nand_read_byte(9)*

*4.6.0-rc1*

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
