
.. _API-nand-write-oob-syndrome:

=======================
nand_write_oob_syndrome
=======================

*man nand_write_oob_syndrome(9)*

*4.6.0-rc1*

[REPLACEABLE] OOB data write function for HW ECC with syndrome - only for large page flash


Synopsis
========

.. c:function:: int nand_write_oob_syndrome( struct mtd_info * mtd, struct nand_chip * chip, int page )

Arguments
=========

``mtd``
    mtd info structure

``chip``
    nand chip info structure

``page``
    page number to write
