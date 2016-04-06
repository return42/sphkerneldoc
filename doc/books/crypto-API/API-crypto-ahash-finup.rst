
.. _API-crypto-ahash-finup:

==================
crypto_ahash_finup
==================

*man crypto_ahash_finup(9)*

*4.6.0-rc1*

update and finalize message digest


Synopsis
========

.. c:function:: int crypto_ahash_finup( struct ahash_request * req )

Arguments
=========

``req``
    reference to the ahash_request handle that holds all information needed to perform the cipher operation


Description
===========

This function is a “short-hand” for the function calls of crypto_ahash_update and crypto_shash_final. The parameters have the same meaning as discussed for those separate
functions.


Return
======

0 if the message digest creation was successful; < 0 if an error occurred
