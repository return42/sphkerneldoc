
.. _API-crypto-ahash-export:

===================
crypto_ahash_export
===================

*man crypto_ahash_export(9)*

*4.6.0-rc1*

extract current message digest state


Synopsis
========

.. c:function:: int crypto_ahash_export( struct ahash_request * req, void * out )

Arguments
=========

``req``
    reference to the ahash_request handle whose state is exported

``out``
    output buffer of sufficient size that can hold the hash state


Description
===========

This function exports the hash state of the ahash_request handle into the caller-allocated output buffer out which must have sufficient size (e.g. by calling
crypto_ahash_reqsize).


Return
======

0 if the export was successful; < 0 if an error occurred
