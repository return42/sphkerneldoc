
.. _API-nand-erase-nand:

===============
nand_erase_nand
===============

*man nand_erase_nand(9)*

*4.6.0-rc1*

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
