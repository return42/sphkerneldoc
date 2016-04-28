.. -*- coding: utf-8; mode: rst -*-

.. _API-single-erase:

============
single_erase
============

*man single_erase(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
