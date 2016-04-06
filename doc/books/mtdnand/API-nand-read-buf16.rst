
.. _API-nand-read-buf16:

===============
nand_read_buf16
===============

*man nand_read_buf16(9)*

*4.6.0-rc1*

[DEFAULT] read chip data into buffer


Synopsis
========

.. c:function:: void nand_read_buf16( struct mtd_info * mtd, uint8_t * buf, int len )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    buffer to store date

``len``
    number of bytes to read


Description
===========

Default read function for 16bit buswidth.
