
.. _API-nand-block-markbad-lowlevel:

===========================
nand_block_markbad_lowlevel
===========================

*man nand_block_markbad_lowlevel(9)*

*4.6.0-rc1*

mark a block bad


Synopsis
========

.. c:function:: int nand_block_markbad_lowlevel( struct mtd_info * mtd, loff_t ofs )

Arguments
=========

``mtd``
    MTD device structure

``ofs``
    offset from device start


Description
===========

This function performs the generic NAND bad block marking steps (i.e., bad block table(s) and/or marker(s)). We only allow the hardware driver to specify how to write bad block
markers to OOB (chip->block_markbad).


We try operations in the following order
========================================

(1) erase the affected block, to allow OOB marker to be written cleanly (2) write bad block marker to OOB area of affected block (unless flag NAND_BBT_NO_OOB_BBM is present)
(3) update the BBT Note that we retain the first error encountered in (2) or (3), finish the procedures, and dump the error in the end.
