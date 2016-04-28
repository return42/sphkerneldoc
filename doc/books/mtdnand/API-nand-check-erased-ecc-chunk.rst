.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-check-erased-ecc-chunk:

===========================
nand_check_erased_ecc_chunk
===========================

*man nand_check_erased_ecc_chunk(9)*

*4.6.0-rc5*

check if an ECC chunk contains (almost) only 0xff data


Synopsis
========

.. c:function:: int nand_check_erased_ecc_chunk( void * data, int datalen, void * ecc, int ecclen, void * extraoob, int extraooblen, int bitflips_threshold )

Arguments
=========

``data``
    data buffer to test

``datalen``
    data length

``ecc``
    ECC buffer

``ecclen``
    ECC length

``extraoob``
    extra OOB buffer

``extraooblen``
    extra OOB length

``bitflips_threshold``
    maximum number of bitflips


Description
===========

Check if a data buffer and its associated ECC and OOB data contains only
0xff pattern, which means the underlying region has been erased and is
ready to be programmed. The bitflips_threshold specify the maximum
number of bitflips before considering the region as not erased.


Note
====

1/ ECC algorithms are working on pre-defined block sizes which are
usually different from the NAND page size. When fixing bitflips, ECC
engines will report the number of errors per chunk, and the NAND core
infrastructure expect you to return the maximum number of bitflips for
the whole page. This is why you should always use this function on a
single chunk and not on the whole page. After checking each chunk you
should update your max_bitflips value accordingly. 2/ When checking for
bitflips in erased pages you should not only check the payload data but
also their associated ECC data, because a user might have programmed
almost all bits to 1 but a few. In this case, we shouldn't consider the
chunk as erased, and checking ECC bytes prevent this case. 3/ The
extraoob argument is optional, and should be used if some of your OOB
data are protected by the ECC engine. It could also be used if you
support subpages and want to attach some extra OOB data to an ECC chunk.

Returns a positive number of bitflips less than or equal to
bitflips_threshold, or -ERROR_CODE for bitflips in excess of the
threshold. In case of success, the passed buffers are filled with 0xff.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
