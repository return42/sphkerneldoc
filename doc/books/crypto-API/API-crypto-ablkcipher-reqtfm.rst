
.. _API-crypto-ablkcipher-reqtfm:

========================
crypto_ablkcipher_reqtfm
========================

*man crypto_ablkcipher_reqtfm(9)*

*4.6.0-rc1*

obtain cipher handle from request


Synopsis
========

.. c:function:: struct crypto_ablkcipher ⋆ crypto_ablkcipher_reqtfm( struct ablkcipher_request * req )

Arguments
=========

``req``
    ablkcipher_request out of which the cipher handle is to be obtained


Description
===========

Return the crypto_ablkcipher handle when furnishing an ablkcipher_request data structure.


Return
======

crypto_ablkcipher handle
