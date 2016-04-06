
.. _API-nand-read-page-swecc:

====================
nand_read_page_swecc
====================

*man nand_read_page_swecc(9)*

*4.6.0-rc1*

[REPLACEABLE] software ECC based page read function


Synopsis
========

.. c:function:: int nand_read_page_swecc( struct mtd_info * mtd, struct nand_chip * chip, uint8_t * buf, int oob_required, int page )

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
