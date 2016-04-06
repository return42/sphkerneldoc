
.. _API-nand-read-page-syndrome:

=======================
nand_read_page_syndrome
=======================

*man nand_read_page_syndrome(9)*

*4.6.0-rc1*

[REPLACEABLE] hardware ECC syndrome based page read


Synopsis
========

.. c:function:: int nand_read_page_syndrome( struct mtd_info * mtd, struct nand_chip * chip, uint8_t * buf, int oob_required, int page )

Arguments
=========

``mtd``
    mtd info structure

``chip``
    nand chip info structure

``buf``
    buffer to store read data

``oob_required``
    caller requires OOB data read to chip->oob_poi

``page``
    page number to read


Description
===========

The hw generator calculates the error syndrome automatically. Therefore we need a special oob layout and handling.
