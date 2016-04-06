
.. _API-nand-do-read-ops:

================
nand_do_read_ops
================

*man nand_do_read_ops(9)*

*4.6.0-rc1*

[INTERN] Read data with ECC


Synopsis
========

.. c:function:: int nand_do_read_ops( struct mtd_info * mtd, loff_t from, struct mtd_oob_ops * ops )

Arguments
=========

``mtd``
    MTD device structure

``from``
    offset to read from

``ops``
    oob ops structure


Description
===========

Internal function. Called with chip held.
