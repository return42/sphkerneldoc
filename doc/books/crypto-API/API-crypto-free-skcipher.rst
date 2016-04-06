
.. _API-crypto-free-skcipher:

====================
crypto_free_skcipher
====================

*man crypto_free_skcipher(9)*

*4.6.0-rc1*

zeroize and free cipher handle


Synopsis
========

.. c:function:: void crypto_free_skcipher( struct crypto_skcipher * tfm )

Arguments
=========

``tfm``
    cipher handle to be freed
