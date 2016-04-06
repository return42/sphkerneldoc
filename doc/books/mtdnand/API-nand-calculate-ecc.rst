
.. _API-nand-calculate-ecc:

==================
nand_calculate_ecc
==================

*man nand_calculate_ecc(9)*

*4.6.0-rc1*

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
