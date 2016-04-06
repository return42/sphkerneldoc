
.. _API-crypto-akcipher-set-pub-key:

===========================
crypto_akcipher_set_pub_key
===========================

*man crypto_akcipher_set_pub_key(9)*

*4.6.0-rc1*

Invoke set public key operation


Synopsis
========

.. c:function:: int crypto_akcipher_set_pub_key( struct crypto_akcipher * tfm, const void * key, unsigned int keylen )

Arguments
=========

``tfm``
    tfm handle

``key``
    BER encoded public key

``keylen``
    length of the key


Description
===========

Function invokes the algorithm specific set key function, which knows how to decode and interpret the encoded key


Return
======

zero on success; error code in case of error
