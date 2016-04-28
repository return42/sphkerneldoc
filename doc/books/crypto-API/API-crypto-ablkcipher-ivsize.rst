.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-ablkcipher-ivsize:

========================
crypto_ablkcipher_ivsize
========================

*man crypto_ablkcipher_ivsize(9)*

*4.6.0-rc5*

obtain IV size


Synopsis
========

.. c:function:: unsigned int crypto_ablkcipher_ivsize( struct crypto_ablkcipher * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The size of the IV for the ablkcipher referenced by the cipher handle is
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
