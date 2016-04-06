
.. _API-nand-scan-tail:

==============
nand_scan_tail
==============

*man nand_scan_tail(9)*

*4.6.0-rc1*

[NAND Interface] Scan for the NAND device


Synopsis
========

.. c:function:: int nand_scan_tail( struct mtd_info * mtd )

Arguments
=========

``mtd``
    MTD device structure


Description
===========

This is the second phase of the normal ``nand_scan`` function. It fills out all the uninitialized function pointers with the defaults and scans for a bad block table if
appropriate.
