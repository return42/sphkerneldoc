
.. _API-nand-write:

==========
nand_write
==========

*man nand_write(9)*

*4.6.0-rc1*

[MTD Interface] NAND write with ECC


Synopsis
========

.. c:function:: int nand_write( struct mtd_info * mtd, loff_t to, size_t len, size_t * retlen, const uint8_t * buf )

Arguments
=========

``mtd``
    MTD device structure

``to``
    offset to write to

``len``
    number of bytes to write

``retlen``
    pointer to variable to store the number of written bytes

``buf``
    the data to write


Description
===========

NAND write with ECC.
