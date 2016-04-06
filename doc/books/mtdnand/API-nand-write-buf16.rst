
.. _API-nand-write-buf16:

================
nand_write_buf16
================

*man nand_write_buf16(9)*

*4.6.0-rc1*

[DEFAULT] write buffer to chip


Synopsis
========

.. c:function:: void nand_write_buf16( struct mtd_info * mtd, const uint8_t * buf, int len )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    data buffer

``len``
    number of bytes to write


Description
===========

Default write function for 16bit buswidth.
