.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-ablkcipher-setkey:

========================
crypto_ablkcipher_setkey
========================

*man crypto_ablkcipher_setkey(9)*

*4.6.0-rc5*

set key for cipher


Synopsis
========

.. c:function:: int crypto_ablkcipher_setkey( struct crypto_ablkcipher * tfm, const u8 * key, unsigned int keylen )

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

The caller provided key is set for the ablkcipher referenced by the
cipher handle.

Note, the key length determines the cipher type. Many block ciphers
implement different cipher modes depending on the key size, such as
AES-128 vs AES-192 vs. AES-256. When providing a 16 byte key for an AES
cipher handle, AES-128 is performed.


Return
======

0 if the setting of the key was successful; < 0 if an error occurred


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
