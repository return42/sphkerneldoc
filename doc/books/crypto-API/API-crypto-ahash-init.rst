.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-ahash-init:

=================
crypto_ahash_init
=================

*man crypto_ahash_init(9)*

*4.6.0-rc5*

(re)initialize message digest handle


Synopsis
========

.. c:function:: int crypto_ahash_init( struct ahash_request * req )

Arguments
=========

``req``
    ahash_request handle that already is initialized with all necessary
    data using the ahash_request_* API functions


Description
===========

The call (re-)initializes the message digest referenced by the
ahash_request handle. Any potentially existing state created by
previous operations is discarded.


Return
======

0 if the message digest initialization was successful; < 0 if an error
occurred


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
