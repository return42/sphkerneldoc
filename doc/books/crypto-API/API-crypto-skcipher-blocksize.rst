
.. _API-crypto-skcipher-blocksize:

=========================
crypto_skcipher_blocksize
=========================

*man crypto_skcipher_blocksize(9)*

*4.6.0-rc1*

obtain block size of cipher


Synopsis
========

.. c:function:: unsigned int crypto_skcipher_blocksize( struct crypto_skcipher * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The block size for the skcipher referenced with the cipher handle is returned. The caller may use that information to allocate appropriate memory for the data returned by the
encryption or decryption operation


Return
======

block size of cipher
