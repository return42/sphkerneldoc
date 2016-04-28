.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-ahash-import:

===================
crypto_ahash_import
===================

*man crypto_ahash_import(9)*

*4.6.0-rc5*

import message digest state


Synopsis
========

.. c:function:: int crypto_ahash_import( struct ahash_request * req, const void * in )

Arguments
=========

``req``
    reference to ahash_request handle the state is imported into

``in``
    buffer holding the state


Description
===========

This function imports the hash state into the ahash_request handle from
the input buffer. That buffer should have been generated with the
crypto_ahash_export function.


Return
======

0 if the import was successful; < 0 if an error occurred


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
