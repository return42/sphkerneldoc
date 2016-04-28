.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-shash-blocksize:

======================
crypto_shash_blocksize
======================

*man crypto_shash_blocksize(9)*

*4.6.0-rc5*

obtain block size for cipher


Synopsis
========

.. c:function:: unsigned int crypto_shash_blocksize( struct crypto_shash * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The block size for the message digest cipher referenced with the cipher
handle is returned.


Return
======

block size of cipher


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
