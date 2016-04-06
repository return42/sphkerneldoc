
.. _API-nand-scan-bbt:

=============
nand_scan_bbt
=============

*man nand_scan_bbt(9)*

*4.6.0-rc1*

[NAND Interface] scan, find, read and maybe create bad block table(s)


Synopsis
========

.. c:function:: int nand_scan_bbt( struct mtd_info * mtd, struct nand_bbt_descr * bd )

Arguments
=========

``mtd``
    MTD device structure

``bd``
    descriptor for the good/bad block search pattern


Description
===========

The function checks, if a bad block table(s) is/are already available. If not it scans the device for manufacturer marked good / bad blocks and writes the bad block table(s) to the
selected place.

The bad block table memory is allocated here. It must be freed by calling the nand_free_bbt function.
