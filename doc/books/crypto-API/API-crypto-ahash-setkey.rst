
.. _API-crypto-ahash-setkey:

===================
crypto_ahash_setkey
===================

*man crypto_ahash_setkey(9)*

*4.6.0-rc1*

set key for cipher handle


Synopsis
========

.. c:function:: int crypto_ahash_setkey( struct crypto_ahash * tfm, const u8 * key, unsigned int keylen )

Arguments
=========

``tfm``
    cipher handle

``key``
    buffer holding the key

``keylen``
    length of the key in bytes


Description
===========

The caller provided key is set for the ahash cipher. The cipher handle must point to a keyed hash in order for this function to succeed.


Return
======

0 if the setting of the key was successful; < 0 if an error occurred
