
.. _API---nand-calculate-ecc:

====================
__nand_calculate_ecc
====================

*man __nand_calculate_ecc(9)*

*4.6.0-rc1*

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
