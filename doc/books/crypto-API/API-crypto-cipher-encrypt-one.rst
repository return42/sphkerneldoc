.. -*- coding: utf-8; mode: rst -*-

.. _API-crypto-cipher-encrypt-one:

=========================
crypto_cipher_encrypt_one
=========================

*man crypto_cipher_encrypt_one(9)*

*4.6.0-rc5*

encrypt one block of plaintext


Synopsis
========

.. c:function:: void crypto_cipher_encrypt_one( struct crypto_cipher * tfm, u8 * dst, const u8 * src )

Arguments
=========

``tfm``
    cipher handle

``dst``
    points to the buffer that will be filled with the ciphertext

``src``
    buffer holding the plaintext to be encrypted


Description
===========

Invoke the encryption operation of one block. The caller must ensure
that the plaintext and ciphertext buffers are at least one block in
size.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
