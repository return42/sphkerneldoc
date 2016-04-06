
.. _API-crypto-rng-get-bytes:

====================
crypto_rng_get_bytes
====================

*man crypto_rng_get_bytes(9)*

*4.6.0-rc1*

get random number


Synopsis
========

.. c:function:: int crypto_rng_get_bytes( struct crypto_rng * tfm, u8 * rdata, unsigned int dlen )

Arguments
=========

``tfm``
    cipher handle

``rdata``
    output buffer holding the random numbers

``dlen``
    length of the output buffer


Description
===========

This function fills the caller-allocated buffer with random numbers using the random number generator referenced by the cipher handle.


Return
======

0 function was successful; < 0 if an error occurred
