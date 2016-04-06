
.. _API---nand-correct-data:

===================
__nand_correct_data
===================

*man __nand_correct_data(9)*

*4.6.0-rc1*

[NAND Interface] Detect and correct bit error(s)


Synopsis
========

.. c:function:: int __nand_correct_data( unsigned char * buf, unsigned char * read_ecc, unsigned char * calc_ecc, unsigned int eccsize )

Arguments
=========

``buf``
    raw data read from the chip

``read_ecc``
    ECC from the chip

``calc_ecc``
    the ECC calculated from raw data

``eccsize``
    data bytes per ECC step (256 or 512)


Description
===========

Detect and correct a 1 bit error for eccsize byte block
