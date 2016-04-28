.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-shash-digestsize:

=======================
crypto_shash_digestsize
=======================

*man crypto_shash_digestsize(9)*

*4.6.0-rc5*

obtain message digest size


Synopsis
========

.. c:function:: unsigned int crypto_shash_digestsize( struct crypto_shash * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The size for the message digest created by the message digest cipher
referenced with the cipher handle is returned.


Return
======

digest size of cipher


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
