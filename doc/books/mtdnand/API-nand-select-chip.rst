
.. _API-nand-select-chip:

================
nand_select_chip
================

*man nand_select_chip(9)*

*4.6.0-rc1*

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
