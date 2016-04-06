
.. _API-nand-read-page-hwecc-oob-first:

==============================
nand_read_page_hwecc_oob_first
==============================

*man nand_read_page_hwecc_oob_first(9)*

*4.6.0-rc1*

[REPLACEABLE] hw ecc, read oob first


Synopsis
========

.. c:function:: int nand_read_page_hwecc_oob_first( struct mtd_info * mtd, struct nand_chip * chip, uint8_t * buf, int oob_required, int page )

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

Hardware ECC for large page chips, require OOB to be read first. For this ECC mode, the write_page method is re-used from ECC_HW. These methods read/write ECC from the OOB area,
unlike the ECC_HW_SYNDROME support with multiple ECC steps, follows the “infix ECC” scheme and reads/writes ECC from the data area, by overwriting the NAND manufacturer bad block
markings.
