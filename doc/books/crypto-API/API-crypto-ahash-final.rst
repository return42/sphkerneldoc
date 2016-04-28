.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-ahash-final:

==================
crypto_ahash_final
==================

*man crypto_ahash_final(9)*

*4.6.0-rc5*

calculate message digest


Synopsis
========

.. c:function:: int crypto_ahash_final( struct ahash_request * req )

Arguments
=========

``req``
    reference to the ahash_request handle that holds all information
    needed to perform the cipher operation


Description
===========

Finalize the message digest operation and create the message digest
based on all data added to the cipher handle. The message digest is
placed into the output buffer registered with the ahash_request handle.


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
