.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-aead-ivsize:

==================
crypto_aead_ivsize
==================

*man crypto_aead_ivsize(9)*

*4.6.0-rc5*

obtain IV size


Synopsis
========

.. c:function:: unsigned int crypto_aead_ivsize( struct crypto_aead * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The size of the IV for the aead referenced by the cipher handle is
returned. This IV size may be zero if the cipher does not need an IV.


Return
======

IV size in bytes


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
