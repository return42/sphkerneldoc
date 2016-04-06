
.. _API-crypto-ahash-digestsize:

=======================
crypto_ahash_digestsize
=======================

*man crypto_ahash_digestsize(9)*

*4.6.0-rc1*

obtain message digest size


Synopsis
========

.. c:function:: unsigned int crypto_ahash_digestsize( struct crypto_ahash * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The size for the message digest created by the message digest cipher referenced with the cipher handle is returned.


Return
======

message digest size of cipher
