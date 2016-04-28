.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-read-subpage:

=================
nand_read_subpage
=================

*man nand_read_subpage(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
