.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-write-oob-std:

==================
nand_write_oob_std
==================

*man nand_write_oob_std(9)*

*4.6.0-rc5*

[REPLACEABLE] the most common OOB data write function


Synopsis
========

.. c:function:: int nand_write_oob_std( struct mtd_info * mtd, struct nand_chip * chip, int page )

Arguments
=========

``mtd``
    mtd info structure

``chip``
    nand chip info structure

``page``
    page number to write


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
