.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-blkcipher-decrypt:

========================
crypto_blkcipher_decrypt
========================

*man crypto_blkcipher_decrypt(9)*

*4.6.0-rc5*

decrypt ciphertext


Synopsis
========

.. c:function:: int crypto_blkcipher_decrypt( struct blkcipher_desc * desc, struct scatterlist * dst, struct scatterlist * src, unsigned int nbytes )

Arguments
=========

``desc``
    reference to the block cipher handle with meta data

``dst``
    scatter/gather list that is filled by the cipher operation with the
    plaintext

``src``
    scatter/gather list that holds the ciphertext

``nbytes``
    number of bytes of the ciphertext to decrypt.


Description
===========

Decrypt ciphertext data using the IV set by the caller with a preceding
call of crypto_blkcipher_set_iv.

The blkcipher_desc data structure must be filled by the caller as
documented for the crypto_blkcipher_encrypt call above.


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
