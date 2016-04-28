.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-blkcipher-encrypt-iv:

===========================
crypto_blkcipher_encrypt_iv
===========================

*man crypto_blkcipher_encrypt_iv(9)*

*4.6.0-rc5*

encrypt plaintext with dedicated IV


Synopsis
========

.. c:function:: int crypto_blkcipher_encrypt_iv( struct blkcipher_desc * desc, struct scatterlist * dst, struct scatterlist * src, unsigned int nbytes )

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

Encrypt plaintext data with the use of an IV that is solely used for
this cipher operation. Any previously set IV is not used.

The blkcipher_desc data structure must be filled by the caller and can
reside on the stack. The caller must fill desc as follows: desc.tfm is
filled with the block cipher handle; desc.info is filled with the IV to
be used for the current operation; desc.flags is filled with either
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
