
.. _API-crypto-aead-reqsize:

===================
crypto_aead_reqsize
===================

*man crypto_aead_reqsize(9)*

*4.6.0-rc1*

obtain size of the request data structure


Synopsis
========

.. c:function:: unsigned int crypto_aead_reqsize( struct crypto_aead * tfm )

Arguments
=========

``tfm``
    cipher handle


Return
======

number of bytes
