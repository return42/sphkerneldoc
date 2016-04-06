
.. _API-ahash-request-alloc:

===================
ahash_request_alloc
===================

*man ahash_request_alloc(9)*

*4.6.0-rc1*

allocate request data structure


Synopsis
========

.. c:function:: struct ahash_request ⋆ ahash_request_alloc( struct crypto_ahash * tfm, gfp_t gfp )

Arguments
=========

``tfm``
    cipher handle to be registered with the request

``gfp``
    memory allocation flag that is handed to kmalloc by the API call.


Description
===========

Allocate the request data structure that must be used with the ahash message digest API calls. During the allocation, the provided ahash handle is registered in the request data
structure.


Return
======

allocated request handle in case of success; ``IS_ERR`` is true in case of an error, ``PTR_ERR`` returns the error code.
