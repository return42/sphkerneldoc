.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-block-markbad:

==================
nand_block_markbad
==================

*man nand_block_markbad(9)*

*4.6.0-rc5*

[MTD Interface] Mark block at the given offset as bad


Synopsis
========

.. c:function:: int nand_block_markbad( struct mtd_info * mtd, loff_t ofs )

Arguments
=========

``mtd``
    MTD device structure

``ofs``
    offset relative to mtd start


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
