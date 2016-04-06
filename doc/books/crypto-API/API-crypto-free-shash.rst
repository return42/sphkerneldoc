
.. _API-crypto-free-shash:

=================
crypto_free_shash
=================

*man crypto_free_shash(9)*

*4.6.0-rc1*

zeroize and free the message digest handle


Synopsis
========

.. c:function:: void crypto_free_shash( struct crypto_shash * tfm )

Arguments
=========

``tfm``
    cipher handle to be freed
