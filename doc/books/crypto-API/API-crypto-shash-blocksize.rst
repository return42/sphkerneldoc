
.. _API-crypto-shash-blocksize:

======================
crypto_shash_blocksize
======================

*man crypto_shash_blocksize(9)*

*4.6.0-rc1*

obtain block size for cipher


Synopsis
========

.. c:function:: unsigned int crypto_shash_blocksize( struct crypto_shash * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The block size for the message digest cipher referenced with the cipher handle is returned.


Return
======

block size of cipher
