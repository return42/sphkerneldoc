.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-erase:

==========
nand_erase
==========

*man nand_erase(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
