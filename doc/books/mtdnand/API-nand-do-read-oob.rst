
.. _API-nand-do-read-oob:

================
nand_do_read_oob
================

*man nand_do_read_oob(9)*

*4.6.0-rc1*

[INTERN] NAND read out-of-band


Synopsis
========

.. c:function:: int nand_do_read_oob( struct mtd_info * mtd, loff_t from, struct mtd_oob_ops * ops )

Arguments
=========

``mtd``
    MTD device structure

``from``
    offset to read from

``ops``
    oob operations description structure


Description
===========

NAND read out-of-band data from the spare area.
