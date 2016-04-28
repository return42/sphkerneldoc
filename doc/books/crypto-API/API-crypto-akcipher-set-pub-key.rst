.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-akcipher-set-pub-key:

===========================
crypto_akcipher_set_pub_key
===========================

*man crypto_akcipher_set_pub_key(9)*

*4.6.0-rc5*

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

Function invokes the algorithm specific set key function, which knows
how to decode and interpret the encoded key


Return
======

zero on success; error code in case of error


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
