
.. _API-crypto-shash-setkey:

===================
crypto_shash_setkey
===================

*man crypto_shash_setkey(9)*

*4.6.0-rc1*

set key for message digest


Synopsis
========

.. c:function:: int crypto_shash_setkey( struct crypto_shash * tfm, const u8 * key, unsigned int keylen )

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

The caller provided key is set for the keyed message digest cipher. The cipher handle must point to a keyed message digest cipher in order for this function to succeed.


Return
======

0 if the setting of the key was successful; < 0 if an error occurred
