
.. _API-ahash-request-set-tfm:

=====================
ahash_request_set_tfm
=====================

*man ahash_request_set_tfm(9)*

*4.6.0-rc1*

update cipher handle reference in request


Synopsis
========

.. c:function:: void ahash_request_set_tfm( struct ahash_request * req, struct crypto_ahash * tfm )

Arguments
=========

``req``
    request handle to be modified

``tfm``
    cipher handle that shall be added to the request handle


Description
===========

Allow the caller to replace the existing ahash handle in the request data structure with a different one.
