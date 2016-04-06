
.. _API-crypto-skcipher-reqsize:

=======================
crypto_skcipher_reqsize
=======================

*man crypto_skcipher_reqsize(9)*

*4.6.0-rc1*

obtain size of the request data structure


Synopsis
========

.. c:function:: unsigned int crypto_skcipher_reqsize( struct crypto_skcipher * tfm )

Arguments
=========

``tfm``
    cipher handle


Return
======

number of bytes
