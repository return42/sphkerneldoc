
.. _API-crypto-shash-descsize:

=====================
crypto_shash_descsize
=====================

*man crypto_shash_descsize(9)*

*4.6.0-rc1*

obtain the operational state size


Synopsis
========

.. c:function:: unsigned int crypto_shash_descsize( struct crypto_shash * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The size of the operational state the cipher needs during operation is returned for the hash referenced with the cipher handle. This size is required to calculate the memory
requirements to allow the caller allocating sufficient memory for operational state.

The operational state is defined with struct shash_desc where the size of that data structure is to be calculated as sizeof(struct shash_desc) + crypto_shash_descsize(alg)


Return
======

size of the operational state
