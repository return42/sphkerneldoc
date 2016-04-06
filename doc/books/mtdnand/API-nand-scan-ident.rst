
.. _API-nand-scan-ident:

===============
nand_scan_ident
===============

*man nand_scan_ident(9)*

*4.6.0-rc1*

[NAND Interface] Scan for the NAND device


Synopsis
========

.. c:function:: int nand_scan_ident( struct mtd_info * mtd, int maxchips, struct nand_flash_dev * table )

Arguments
=========

``mtd``
    MTD device structure

``maxchips``
    number of chips to scan for

``table``
    alternative NAND ID table


Description
===========

This is the first phase of the normal ``nand_scan`` function. It reads the flash ID and sets up MTD fields accordingly.

The mtd->owner field must be set to the module of the caller.
