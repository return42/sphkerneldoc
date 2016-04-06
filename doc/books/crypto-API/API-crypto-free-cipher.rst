
.. _API-crypto-free-cipher:

==================
crypto_free_cipher
==================

*man crypto_free_cipher(9)*

*4.6.0-rc1*

zeroize and free the single block cipher handle


Synopsis
========

.. c:function:: void crypto_free_cipher( struct crypto_cipher * tfm )

Arguments
=========

``tfm``
    cipher handle to be freed
