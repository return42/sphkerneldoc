
.. _API-nand-block-bad:

==============
nand_block_bad
==============

*man nand_block_bad(9)*

*4.6.0-rc1*

[DEFAULT] Read bad block marker from the chip


Synopsis
========

.. c:function:: int nand_block_bad( struct mtd_info * mtd, loff_t ofs )

Arguments
=========

``mtd``
    MTD device structure

``ofs``
    offset from device start


Description
===========

Check, if the block is bad.
