
.. _API-nand-do-write-ops:

=================
nand_do_write_ops
=================

*man nand_do_write_ops(9)*

*4.6.0-rc1*

[INTERN] NAND write with ECC


Synopsis
========

.. c:function:: int nand_do_write_ops( struct mtd_info * mtd, loff_t to, struct mtd_oob_ops * ops )

Arguments
=========

``mtd``
    MTD device structure

``to``
    offset to write to

``ops``
    oob operations description structure


Description
===========

NAND write with ECC.
