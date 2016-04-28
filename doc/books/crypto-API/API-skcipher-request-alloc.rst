.. -*- coding: utf-8; mode: rst -*-

.. _API-skcipher-request-alloc:

======================
skcipher_request_alloc
======================

*man skcipher_request_alloc(9)*

*4.6.0-rc5*

allocate request data structure


Synopsis
========

.. c:function:: struct skcipher_request * skcipher_request_alloc( struct crypto_skcipher * tfm, gfp_t gfp )

Arguments
=========

``tfm``
    cipher handle to be registered with the request

``gfp``
    memory allocation flag that is handed to kmalloc by the API call.


Description
===========

Allocate the request data structure that must be used with the skcipher
encrypt and decrypt API calls. During the allocation, the provided
skcipher handle is registered in the request data structure.


Return
======

allocated request handle in case of success; ``IS_ERR`` is true in case
of an error, ``PTR_ERR`` returns the error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
