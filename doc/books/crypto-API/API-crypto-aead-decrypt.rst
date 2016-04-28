.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-aead-decrypt:

===================
crypto_aead_decrypt
===================

*man crypto_aead_decrypt(9)*

*4.6.0-rc5*

decrypt ciphertext


Synopsis
========

.. c:function:: int crypto_aead_decrypt( struct aead_request * req )

Arguments
=========

``req``
    reference to the ablkcipher_request handle that holds all
    information needed to perform the cipher operation


Description
===========

Decrypt ciphertext data using the aead_request handle. That data
structure and how it is filled with data is discussed with the
aead_request_* functions.

IMPORTANT NOTE The caller must concatenate the ciphertext followed by
the authentication data / tag. That authentication data / tag must have
the size defined by the crypto_aead_setauthsize invocation.


Return
======

0 if the cipher operation was successful; -EBADMSG: The AEAD cipher
operation performs the authentication of the data during the decryption
operation. Therefore, the function returns this error if the
authentication of the ciphertext was unsuccessful (i.e. the integrity of
the ciphertext or the associated data was violated); < 0 if an error
occurred.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
