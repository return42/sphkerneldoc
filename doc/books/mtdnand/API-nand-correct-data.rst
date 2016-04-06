
.. _API-nand-correct-data:

=================
nand_correct_data
=================

*man nand_correct_data(9)*

*4.6.0-rc1*

[NAND Interface] Detect and correct bit error(s)


Synopsis
========

.. c:function:: int nand_correct_data( struct mtd_info * mtd, unsigned char * buf, unsigned char * read_ecc, unsigned char * calc_ecc )

Arguments
=========

``mtd``
    MTD block structure

``buf``
    raw data read from the chip

``read_ecc``
    ECC from the chip

``calc_ecc``
    the ECC calculated from raw data


Description
===========

Detect and correct a 1 bit error for 256/512 byte block
