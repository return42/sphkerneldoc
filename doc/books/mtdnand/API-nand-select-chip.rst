.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-select-chip:

================
nand_select_chip
================

*man nand_select_chip(9)*

*4.6.0-rc5*

[DEFAULT] control CE line


Synopsis
========

.. c:function:: void nand_select_chip( struct mtd_info * mtd, int chipnr )

Arguments
=========

``mtd``
    MTD device structure

``chipnr``
    chipnumber to select, -1 for deselect


Description
===========

Default select function for 1 chip devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
