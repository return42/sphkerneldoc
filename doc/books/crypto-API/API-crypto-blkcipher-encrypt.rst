.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-blkcipher-encrypt:

========================
crypto_blkcipher_encrypt
========================

*man crypto_blkcipher_encrypt(9)*

*4.6.0-rc5*

encrypt plaintext


Synopsis
========

.. c:function:: int crypto_blkcipher_encrypt( struct blkcipher_desc * desc, struct scatterlist * dst, struct scatterlist * src, unsigned int nbytes )

Arguments
=========

``desc``
    reference to the block cipher handle with meta data

``dst``
    scatter/gather list that is filled by the cipher operation with the
    ciphertext

``src``
    scatter/gather list that holds the plaintext

``nbytes``
    number of bytes of the plaintext to encrypt.


Description
===========

Encrypt plaintext data using the IV set by the caller with a preceding
call of crypto_blkcipher_set_iv.

The blkcipher_desc data structure must be filled by the caller and can
reside on the stack. The caller must fill desc as follows: desc.tfm is
filled with the block cipher handle; desc.flags is filled with either
CRYPTO_TFM_REQ_MAY_SLEEP or 0.


Return
======

0 if the cipher operation was successful; < 0 if an error occurred


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
