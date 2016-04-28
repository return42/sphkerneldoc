.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-calculate-ecc:

==================
nand_calculate_ecc
==================

*man nand_calculate_ecc(9)*

*4.6.0-rc5*

[NAND Interface] Calculate 3-byte ECC for 256/512-byte block


Synopsis
========

.. c:function:: int nand_calculate_ecc( struct mtd_info * mtd, const unsigned char * buf, unsigned char * code )

Arguments
=========

``mtd``
    MTD block structure

``buf``
    input buffer with raw data

``code``
    output buffer with ECC


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
