
.. _API-crypto-free-blkcipher:

=====================
crypto_free_blkcipher
=====================

*man crypto_free_blkcipher(9)*

*4.6.0-rc1*

zeroize and free the block cipher handle


Synopsis
========

.. c:function:: void crypto_free_blkcipher( struct crypto_blkcipher * tfm )

Arguments
=========

``tfm``
    cipher handle to be freed
