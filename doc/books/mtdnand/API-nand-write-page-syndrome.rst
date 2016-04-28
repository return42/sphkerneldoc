.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-write-page-syndrome:

========================
nand_write_page_syndrome
========================

*man nand_write_page_syndrome(9)*

*4.6.0-rc5*

[REPLACEABLE] hardware ECC syndrome based page write


Synopsis
========

.. c:function:: int nand_write_page_syndrome( struct mtd_info * mtd, struct nand_chip * chip, const uint8_t * buf, int oob_required, int page )

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


Description
===========

The hw generator calculates the error syndrome automatically. Therefore
we need a special oob layout and handling.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
