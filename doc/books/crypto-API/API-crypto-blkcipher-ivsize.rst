
.. _API-crypto-blkcipher-ivsize:

=======================
crypto_blkcipher_ivsize
=======================

*man crypto_blkcipher_ivsize(9)*

*4.6.0-rc1*

obtain IV size


Synopsis
========

.. c:function:: unsigned int crypto_blkcipher_ivsize( struct crypto_blkcipher * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The size of the IV for the block cipher referenced by the cipher handle is returned. This IV size may be zero if the cipher does not need an IV.


Return
======

IV size in bytes
