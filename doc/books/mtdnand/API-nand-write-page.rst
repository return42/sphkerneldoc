
.. _API-nand-write-page:

===============
nand_write_page
===============

*man nand_write_page(9)*

*4.6.0-rc1*

[REPLACEABLE] write one page


Synopsis
========

.. c:function:: int nand_write_page( struct mtd_info * mtd, struct nand_chip * chip, uint32_t offset, int data_len, const uint8_t * buf, int oob_required, int page, int cached, int raw )

Arguments
=========

``mtd``
    MTD device structure

``chip``
    NAND chip descriptor

``offset``
    address offset within the page

``data_len``
    length of actual data to be written

``buf``
    the data to write

``oob_required``
    must write chip->oob_poi to OOB

``page``
    page number to write

``cached``
    cached programming

``raw``
    use _raw version of write_page
