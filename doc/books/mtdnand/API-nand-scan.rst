.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-scan:

=========
nand_scan
=========

*man nand_scan(9)*

*4.6.0-rc5*

[NAND Interface] Scan for the NAND device


Synopsis
========

.. c:function:: int nand_scan( struct mtd_info * mtd, int maxchips )

Arguments
=========

``mtd``
    MTD device structure

``maxchips``
    number of chips to scan for


Description
===========

This fills out all the uninitialized function pointers with the
defaults. The flash ID is read and the mtd/chip structures are filled
with the appropriate values.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
