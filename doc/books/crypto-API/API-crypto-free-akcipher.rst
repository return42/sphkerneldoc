
.. _API-crypto-free-akcipher:

====================
crypto_free_akcipher
====================

*man crypto_free_akcipher(9)*

*4.6.0-rc1*

free AKCIPHER tfm handle


Synopsis
========

.. c:function:: void crypto_free_akcipher( struct crypto_akcipher * tfm )

Arguments
=========

``tfm``
    AKCIPHER tfm handle allocated with ``crypto_alloc_akcipher``
