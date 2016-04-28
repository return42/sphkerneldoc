.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-ahash-reqsize:

====================
crypto_ahash_reqsize
====================

*man crypto_ahash_reqsize(9)*

*4.6.0-rc5*

obtain size of the request data structure


Synopsis
========

.. c:function:: unsigned int crypto_ahash_reqsize( struct crypto_ahash * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

Return the size of the ahash state size. With the crypto_ahash_export
function, the caller can export the state into a buffer whose size is
defined with this function.


Return
======

size of the ahash state


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
