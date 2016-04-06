
.. _API-crypto-ahash-reqsize:

====================
crypto_ahash_reqsize
====================

*man crypto_ahash_reqsize(9)*

*4.6.0-rc1*

obtain size of the request data structure


Synopsis
========

.. c:function:: unsigned int crypto_ahash_reqsize( struct crypto_ahash * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

Return the size of the ahash state size. With the crypto_ahash_export function, the caller can export the state into a buffer whose size is defined with this function.


Return
======

size of the ahash state
