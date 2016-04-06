
.. _API-nand-read-oob:

=============
nand_read_oob
=============

*man nand_read_oob(9)*

*4.6.0-rc1*

[MTD Interface] NAND read data and/or out-of-band


Synopsis
========

.. c:function:: int nand_read_oob( struct mtd_info * mtd, loff_t from, struct mtd_oob_ops * ops )

Arguments
=========

``mtd``
    MTD device structure

``from``
    offset to read from

``ops``
    oob operation description structure


Description
===========

NAND read data and/or out-of-band data.
