
.. _API-read-bbt:

========
read_bbt
========

*man read_bbt(9)*

*4.6.0-rc1*

[GENERIC] Read the bad block table starting from page


Synopsis
========

.. c:function:: int read_bbt( struct mtd_info * mtd, uint8_t * buf, int page, int num, struct nand_bbt_descr * td, int offs )

Arguments
=========

``mtd``
    MTD device structure

``buf``
    temporary buffer

``page``
    the starting page

``num``
    the number of bbt descriptors to read

``td``
    the bbt describtion table

``offs``
    block number offset in the table


Description
===========

Read the bad block table starting from page.
