.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-read-page-raw-syndrome:

===========================
nand_read_page_raw_syndrome
===========================

*man nand_read_page_raw_syndrome(9)*

*4.6.0-rc5*

[INTERN] read raw page data without ecc


Synopsis
========

.. c:function:: int nand_read_page_raw_syndrome( struct mtd_info * mtd, struct nand_chip * chip, uint8_t * buf, int oob_required, int page )

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

We need a special oob layout and handling even when OOB isn't used.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
