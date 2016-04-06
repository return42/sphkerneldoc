
.. _API-crypto-cipher-blocksize:

=======================
crypto_cipher_blocksize
=======================

*man crypto_cipher_blocksize(9)*

*4.6.0-rc1*

obtain block size for cipher


Synopsis
========

.. c:function:: unsigned int crypto_cipher_blocksize( struct crypto_cipher * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The block size for the single block cipher referenced with the cipher handle tfm is returned. The caller may use that information to allocate appropriate memory for the data
returned by the encryption or decryption operation


Return
======

block size of cipher
