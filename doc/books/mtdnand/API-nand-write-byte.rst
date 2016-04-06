
.. _API-nand-write-byte:

===============
nand_write_byte
===============

*man nand_write_byte(9)*

*4.6.0-rc1*

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
