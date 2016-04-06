
.. _API-crypto-ahash-reqtfm:

===================
crypto_ahash_reqtfm
===================

*man crypto_ahash_reqtfm(9)*

*4.6.0-rc1*

obtain cipher handle from request


Synopsis
========

.. c:function:: struct crypto_ahash ⋆ crypto_ahash_reqtfm( struct ahash_request * req )

Arguments
=========

``req``
    asynchronous request handle that contains the reference to the ahash cipher handle


Description
===========

Return the ahash cipher handle that is registered with the asynchronous request handle ahash_request.


Return
======

ahash cipher handle
