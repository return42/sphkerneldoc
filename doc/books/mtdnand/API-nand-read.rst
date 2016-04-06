
.. _API-nand-read:

=========
nand_read
=========

*man nand_read(9)*

*4.6.0-rc1*

[MTD Interface] MTD compatibility function for nand_do_read_ecc


Synopsis
========

.. c:function:: int nand_read( struct mtd_info * mtd, loff_t from, size_t len, size_t * retlen, uint8_t * buf )

Arguments
=========

``mtd``
    MTD device structure

``from``
    offset to read from

``len``
    number of bytes to read

``retlen``
    pointer to variable to store the number of read bytes

``buf``
    the databuffer to put data


Description
===========

Get hold of the chip and call nand_do_read.
