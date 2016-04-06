
.. _API-nand-write-page-swecc:

=====================
nand_write_page_swecc
=====================

*man nand_write_page_swecc(9)*

*4.6.0-rc1*

[REPLACEABLE] software ECC based page write function


Synopsis
========

.. c:function:: int nand_write_page_swecc( struct mtd_info * mtd, struct nand_chip * chip, const uint8_t * buf, int oob_required, int page )

Arguments
=========

``mtd``
    mtd info structure

``chip``
    nand chip info structure

``buf``
    data buffer

``oob_required``
    must write chip->oob_poi to OOB

``page``
    page number to write
