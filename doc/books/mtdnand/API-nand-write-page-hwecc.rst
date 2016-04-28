.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-write-page-hwecc:

=====================
nand_write_page_hwecc
=====================

*man nand_write_page_hwecc(9)*

*4.6.0-rc5*

[REPLACEABLE] hardware ECC based page write function


Synopsis
========

.. c:function:: int nand_write_page_hwecc( struct mtd_info * mtd, struct nand_chip * chip, const uint8_t * buf, int oob_required, int page )

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
