.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-skcipher-blocksize:

=========================
crypto_skcipher_blocksize
=========================

*man crypto_skcipher_blocksize(9)*

*4.6.0-rc5*

obtain block size of cipher


Synopsis
========

.. c:function:: unsigned int crypto_skcipher_blocksize( struct crypto_skcipher * tfm )

Arguments
=========

``tfm``
    cipher handle


Description
===========

The block size for the skcipher referenced with the cipher handle is
returned. The caller may use that information to allocate appropriate
memory for the data returned by the encryption or decryption operation


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
