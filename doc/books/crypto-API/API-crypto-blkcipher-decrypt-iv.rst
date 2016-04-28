.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-blkcipher-decrypt-iv:

===========================
crypto_blkcipher_decrypt_iv
===========================

*man crypto_blkcipher_decrypt_iv(9)*

*4.6.0-rc5*

decrypt ciphertext with dedicated IV


Synopsis
========

.. c:function:: int crypto_blkcipher_decrypt_iv( struct blkcipher_desc * desc, struct scatterlist * dst, struct scatterlist * src, unsigned int nbytes )

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

Decrypt ciphertext data with the use of an IV that is solely used for
this cipher operation. Any previously set IV is not used.

The blkcipher_desc data structure must be filled by the caller as
documented for the crypto_blkcipher_encrypt_iv call above.


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
