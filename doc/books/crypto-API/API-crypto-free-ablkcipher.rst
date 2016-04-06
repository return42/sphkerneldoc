
.. _API-crypto-free-ablkcipher:

======================
crypto_free_ablkcipher
======================

*man crypto_free_ablkcipher(9)*

*4.6.0-rc1*

zeroize and free cipher handle


Synopsis
========

.. c:function:: void crypto_free_ablkcipher( struct crypto_ablkcipher * tfm )

Arguments
=========

``tfm``
    cipher handle to be freed
