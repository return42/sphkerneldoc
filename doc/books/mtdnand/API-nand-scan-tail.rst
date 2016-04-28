.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-scan-tail:

==============
nand_scan_tail
==============

*man nand_scan_tail(9)*

*4.6.0-rc5*

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

This is the second phase of the normal ``nand_scan`` function. It fills
out all the uninitialized function pointers with the defaults and scans
for a bad block table if appropriate.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
