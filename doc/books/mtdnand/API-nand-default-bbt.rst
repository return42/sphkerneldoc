
.. _API-nand-default-bbt:

================
nand_default_bbt
================

*man nand_default_bbt(9)*

*4.6.0-rc1*

[NAND Interface] Select a default bad block table for the device


Synopsis
========

.. c:function:: int nand_default_bbt( struct mtd_info * mtd )

Arguments
=========

``mtd``
    MTD device structure


Description
===========

This function selects the default bad block table support for the device and calls the nand_scan_bbt function.
