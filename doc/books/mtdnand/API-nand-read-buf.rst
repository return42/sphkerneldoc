
.. _API-nand-read-buf:

=============
nand_read_buf
=============

*man nand_read_buf(9)*

*4.6.0-rc1*

[DEFAULT] read chip data into buffer


Synopsis
========

.. c:function:: void nand_read_buf( struct mtd_info * mtd, uint8_t * buf, int len )

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

Default read function for 8bit buswidth.
