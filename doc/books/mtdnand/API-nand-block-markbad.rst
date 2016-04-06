
.. _API-nand-block-markbad:

==================
nand_block_markbad
==================

*man nand_block_markbad(9)*

*4.6.0-rc1*

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
