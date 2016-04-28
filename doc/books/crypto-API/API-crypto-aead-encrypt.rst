.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-aead-encrypt:

===================
crypto_aead_encrypt
===================

*man crypto_aead_encrypt(9)*

*4.6.0-rc5*

encrypt plaintext


Synopsis
========

.. c:function:: int crypto_aead_encrypt( struct aead_request * req )

Arguments
=========

``req``
    reference to the aead_request handle that holds all information
    needed to perform the cipher operation


Description
===========

Encrypt plaintext data using the aead_request handle. That data
structure and how it is filled with data is discussed with the
aead_request_* functions.

IMPORTANT NOTE The encryption operation creates the authentication data
/ tag. That data is concatenated with the created ciphertext. The
ciphertext memory size is therefore the given number of block cipher
blocks + the size defined by the crypto_aead_setauthsize invocation.
The caller must ensure that sufficient memory is available for the
ciphertext and the authentication tag.


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
