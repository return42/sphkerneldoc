
.. _API-crypto-ablkcipher-blocksize:

===========================
crypto_ablkcipher_blocksize
===========================

*man crypto_ablkcipher_blocksize(9)*

*4.6.0-rc1*

obtain block size of cipher


Synopsis
========

.. c:function:: unsigned int crypto_ablkcipher_blocksize( struct crypto_ablkcipher * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The block size for the ablkcipher referenced with the cipher handle is returned. The caller may use that information to allocate appropriate memory for the data returned by the
encryption or decryption operation


Return
======

block size of cipher
