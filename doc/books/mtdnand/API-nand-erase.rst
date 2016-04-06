
.. _API-nand-erase:

==========
nand_erase
==========

*man nand_erase(9)*

*4.6.0-rc1*

[MTD Interface] erase block(s)


Synopsis
========

.. c:function:: int nand_erase( struct mtd_info * mtd, struct erase_info * instr )

Arguments
=========

``mtd``
    MTD device structure

``instr``
    erase instruction


Description
===========

Erase one ore more blocks.
