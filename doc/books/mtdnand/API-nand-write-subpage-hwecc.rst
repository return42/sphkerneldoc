
.. _API-nand-write-subpage-hwecc:

========================
nand_write_subpage_hwecc
========================

*man nand_write_subpage_hwecc(9)*

*4.6.0-rc1*

[REPLACEABLE] hardware ECC based subpage write


Synopsis
========

.. c:function:: int nand_write_subpage_hwecc( struct mtd_info * mtd, struct nand_chip * chip, uint32_t offset, uint32_t data_len, const uint8_t * buf, int oob_required, int page )

Arguments
=========

``mtd``
    mtd info structure

``chip``
    nand chip info structure

``offset``
    column address of subpage within the page

``data_len``
    data length

``buf``
    data buffer

``oob_required``
    must write chip->oob_poi to OOB

``page``
    page number to write
