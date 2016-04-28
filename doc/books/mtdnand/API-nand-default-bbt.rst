.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-default-bbt:

================
nand_default_bbt
================

*man nand_default_bbt(9)*

*4.6.0-rc5*

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

This function selects the default bad block table support for the device
and calls the nand_scan_bbt function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
