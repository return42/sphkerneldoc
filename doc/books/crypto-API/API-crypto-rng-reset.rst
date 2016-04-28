.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-rng-reset:

================
crypto_rng_reset
================

*man crypto_rng_reset(9)*

*4.6.0-rc5*

re-initialize the RNG


Synopsis
========

.. c:function:: int crypto_rng_reset( struct crypto_rng * tfm, const u8 * seed, unsigned int slen )

Arguments
=========

``tfm``
    cipher handle

``seed``
    seed input data

``slen``
    length of the seed input data


Description
===========

The reset function completely re-initializes the random number generator
referenced by the cipher handle by clearing the current state. The new
state is initialized with the caller provided seed or automatically,
depending on the random number generator type (the ANSI X9.31 RNG
requires caller-provided seed, the SP800-90A DRBGs perform an automatic
seeding). The seed is provided as a parameter to this function call. The
provided seed should have the length of the seed size defined for the
random number generator as defined by crypto_rng_seedsize.


Return
======

0 if the setting of the key was successful; < 0 if an error occurred


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
