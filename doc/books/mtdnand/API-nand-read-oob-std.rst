
.. _API-nand-read-oob-std:

=================
nand_read_oob_std
=================

*man nand_read_oob_std(9)*

*4.6.0-rc1*

[REPLACEABLE] the most common OOB data read function


Synopsis
========

.. c:function:: int nand_read_oob_std( struct mtd_info * mtd, struct nand_chip * chip, int page )

Arguments
=========

``mtd``
    mtd info structure

``chip``
    nand chip info structure

``page``
    page number to read
