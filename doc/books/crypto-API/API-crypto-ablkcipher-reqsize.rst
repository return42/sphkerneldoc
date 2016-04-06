
.. _API-crypto-ablkcipher-reqsize:

=========================
crypto_ablkcipher_reqsize
=========================

*man crypto_ablkcipher_reqsize(9)*

*4.6.0-rc1*

obtain size of the request data structure


Synopsis
========

.. c:function:: unsigned int crypto_ablkcipher_reqsize( struct crypto_ablkcipher * tfm )

Arguments
=========

``tfm``
    cipher handle


Return
======

number of bytes
