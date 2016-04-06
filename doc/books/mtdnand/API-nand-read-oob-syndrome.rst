
.. _API-nand-read-oob-syndrome:

======================
nand_read_oob_syndrome
======================

*man nand_read_oob_syndrome(9)*

*4.6.0-rc1*

[REPLACEABLE] OOB data read function for HW ECC with syndromes


Synopsis
========

.. c:function:: int nand_read_oob_syndrome( struct mtd_info * mtd, struct nand_chip * chip, int page )

Arguments
=========

``mtd``
    mtd info structure

``chip``
    nand chip info structure

``page``
    page number to read
