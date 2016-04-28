.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-erase-nand:

===============
nand_erase_nand
===============

*man nand_erase_nand(9)*

*4.6.0-rc5*

[INTERN] erase block(s)


Synopsis
========

.. c:function:: int nand_erase_nand( struct mtd_info * mtd, struct erase_info * instr, int allowbbt )

Arguments
=========

``mtd``
    MTD device structure

``instr``
    erase instruction

``allowbbt``
    allow erasing the bbt area


Description
===========

Erase one ore more blocks.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
