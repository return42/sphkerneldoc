
.. _API-nand-read-subpage:

=================
nand_read_subpage
=================

*man nand_read_subpage(9)*

*4.6.0-rc1*

[REPLACEABLE] ECC based sub-page read function


Synopsis
========

.. c:function:: int nand_read_subpage( struct mtd_info * mtd, struct nand_chip * chip, uint32_t data_offs, uint32_t readlen, uint8_t * bufpoi, int page )

Arguments
=========

``mtd``
    mtd info structure

``chip``
    nand chip info structure

``data_offs``
    offset of requested data within the page

``readlen``
    data length

``bufpoi``
    buffer to store read data

``page``
    page number to read
