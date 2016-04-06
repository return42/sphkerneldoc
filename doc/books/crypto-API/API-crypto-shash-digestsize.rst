
.. _API-crypto-shash-digestsize:

=======================
crypto_shash_digestsize
=======================

*man crypto_shash_digestsize(9)*

*4.6.0-rc1*

obtain message digest size


Synopsis
========

.. c:function:: unsigned int crypto_shash_digestsize( struct crypto_shash * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The size for the message digest created by the message digest cipher referenced with the cipher handle is returned.


Return
======

digest size of cipher
