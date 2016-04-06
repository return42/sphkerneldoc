
.. _API-nand-default-block-markbad:

==========================
nand_default_block_markbad
==========================

*man nand_default_block_markbad(9)*

*4.6.0-rc1*

[DEFAULT] mark a block bad via bad block marker


Synopsis
========

.. c:function:: int nand_default_block_markbad( struct mtd_info * mtd, loff_t ofs )

Arguments
=========

``mtd``
    MTD device structure

``ofs``
    offset from device start


Description
===========

This is the default implementation, which can be overridden by a hardware specific driver. It provides the details for writing a bad block marker to a block.
