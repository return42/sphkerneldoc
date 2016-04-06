
.. _API-crypto-blkcipher-setkey:

=======================
crypto_blkcipher_setkey
=======================

*man crypto_blkcipher_setkey(9)*

*4.6.0-rc1*

set key for cipher


Synopsis
========

.. c:function:: int crypto_blkcipher_setkey( struct crypto_blkcipher * tfm, const u8 * key, unsigned int keylen )

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

The caller provided key is set for the block cipher referenced by the cipher handle.

Note, the key length determines the cipher type. Many block ciphers implement different cipher modes depending on the key size, such as AES-128 vs AES-192 vs. AES-256. When
providing a 16 byte key for an AES cipher handle, AES-128 is performed.


Return
======

0 if the setting of the key was successful; < 0 if an error occurred
