.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-rng-generate:

===================
crypto_rng_generate
===================

*man crypto_rng_generate(9)*

*4.6.0-rc5*

get random number


Synopsis
========

.. c:function:: int crypto_rng_generate( struct crypto_rng * tfm, const u8 * src, unsigned int slen, u8 * dst, unsigned int dlen )

Arguments
=========

``tfm``
    cipher handle

``src``
    Input buffer holding additional data, may be NULL

``slen``
    Length of additional data

``dst``
    output buffer holding the random numbers

``dlen``
    length of the output buffer


Description
===========

This function fills the caller-allocated buffer with random numbers
using the random number generator referenced by the cipher handle.


Return
======

0 function was successful; < 0 if an error occurred


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
