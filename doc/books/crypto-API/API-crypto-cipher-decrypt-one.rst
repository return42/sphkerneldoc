
.. _API-crypto-cipher-decrypt-one:

=========================
crypto_cipher_decrypt_one
=========================

*man crypto_cipher_decrypt_one(9)*

*4.6.0-rc1*

decrypt one block of ciphertext


Synopsis
========

.. c:function:: void crypto_cipher_decrypt_one( struct crypto_cipher * tfm, u8 * dst, const u8 * src )

Arguments
=========

``tfm``
    cipher handle

``dst``
    points to the buffer that will be filled with the plaintext

``src``
    buffer holding the ciphertext to be decrypted


Description
===========

Invoke the decryption operation of one block. The caller must ensure that the plaintext and ciphertext buffers are at least one block in size.
