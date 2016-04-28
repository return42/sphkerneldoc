.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-block-checkbad:

===================
nand_block_checkbad
===================

*man nand_block_checkbad(9)*

*4.6.0-rc5*

[GENERIC] Check if a block is marked bad


Synopsis
========

.. c:function:: int nand_block_checkbad( struct mtd_info * mtd, loff_t ofs, int allowbbt )

Arguments
=========

``mtd``
    MTD device structure

``ofs``
    offset from device start

``allowbbt``
    1, if its allowed to access the bbt area


Description
===========

Check, if the block is bad. Either by reading the bad block table or
calling of the scan function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
