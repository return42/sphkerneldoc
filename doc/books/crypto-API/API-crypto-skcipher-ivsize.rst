
.. _API-crypto-skcipher-ivsize:

======================
crypto_skcipher_ivsize
======================

*man crypto_skcipher_ivsize(9)*

*4.6.0-rc1*

obtain IV size


Synopsis
========

.. c:function:: unsigned int crypto_skcipher_ivsize( struct crypto_skcipher * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The size of the IV for the skcipher referenced by the cipher handle is returned. This IV size may be zero if the cipher does not need an IV.


Return
======

IV size in bytes
