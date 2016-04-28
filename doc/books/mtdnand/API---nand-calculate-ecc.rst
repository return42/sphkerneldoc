.. -*- coding: utf-8; mode: rst -*-

.. _API---nand-calculate-ecc:

====================
__nand_calculate_ecc
====================

*man __nand_calculate_ecc(9)*

*4.6.0-rc5*

[NAND Interface] Calculate 3-byte ECC for 256/512-byte block


Synopsis
========

.. c:function:: void __nand_calculate_ecc( const unsigned char * buf, unsigned int eccsize, unsigned char * code )

Arguments
=========

``buf``
    input buffer with raw data

``eccsize``
    data bytes per ECC step (256 or 512)

``code``
    output buffer with ECC


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
