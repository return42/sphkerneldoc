
.. _API-crypto-aead-ivsize:

==================
crypto_aead_ivsize
==================

*man crypto_aead_ivsize(9)*

*4.6.0-rc1*

obtain IV size


Synopsis
========

.. c:function:: unsigned int crypto_aead_ivsize( struct crypto_aead * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The size of the IV for the aead referenced by the cipher handle is returned. This IV size may be zero if the cipher does not need an IV.


Return
======

IV size in bytes
