
.. _API-nand-read-page-hwecc:

====================
nand_read_page_hwecc
====================

*man nand_read_page_hwecc(9)*

*4.6.0-rc1*

[REPLACEABLE] hardware ECC based page read function


Synopsis
========

.. c:function:: int nand_read_page_hwecc( struct mtd_info * mtd, struct nand_chip * chip, uint8_t * buf, int oob_required, int page )

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

Not for syndrome calculating ECC controllers which need a special oob layout.
