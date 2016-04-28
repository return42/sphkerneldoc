.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-ahash-digest:

===================
crypto_ahash_digest
===================

*man crypto_ahash_digest(9)*

*4.6.0-rc5*

calculate message digest for a buffer


Synopsis
========

.. c:function:: int crypto_ahash_digest( struct ahash_request * req )

Arguments
=========

``req``
    reference to the ahash_request handle that holds all information
    needed to perform the cipher operation


Description
===========

This function is a “short-hand” for the function calls of
crypto_ahash_init, crypto_ahash_update and crypto_ahash_final. The
parameters have the same meaning as discussed for those separate three
functions.


Return
======

0 if the message digest creation was successful; < 0 if an error
occurred


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
