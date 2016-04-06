
.. _API-nand-read-byte16:

================
nand_read_byte16
================

*man nand_read_byte16(9)*

*4.6.0-rc1*

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
