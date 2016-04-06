
.. _API-single-erase:

============
single_erase
============

*man single_erase(9)*

*4.6.0-rc1*

[GENERIC] NAND standard block erase command function


Synopsis
========

.. c:function:: int single_erase( struct mtd_info * mtd, int page )

Arguments
=========

``mtd``
    MTD device structure

``page``
    the page address of the block which will be erased


Description
===========

Standard erase command for NAND chips. Returns NAND status.
