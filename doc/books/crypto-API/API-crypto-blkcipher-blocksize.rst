
.. _API-crypto-blkcipher-blocksize:

==========================
crypto_blkcipher_blocksize
==========================

*man crypto_blkcipher_blocksize(9)*

*4.6.0-rc1*

obtain block size of cipher


Synopsis
========

.. c:function:: unsigned int crypto_blkcipher_blocksize( struct crypto_blkcipher * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The block size for the block cipher referenced with the cipher handle is returned. The caller may use that information to allocate appropriate memory for the data returned by the
encryption or decryption operation.


Return
======

block size of cipher
