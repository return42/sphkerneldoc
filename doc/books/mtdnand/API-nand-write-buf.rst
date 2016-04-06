
.. _API-nand-write-buf:

==============
nand_write_buf
==============

*man nand_write_buf(9)*

*4.6.0-rc1*

[DEFAULT] write buffer to chip


Synopsis
========

.. c:function:: void nand_write_buf( struct mtd_info * mtd, const uint8_t * buf, int len )

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

Default write function for 8bit buswidth.
