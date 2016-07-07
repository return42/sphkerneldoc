.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/crypto_key.c

.. _`ext4_derive_key_aes`:

ext4_derive_key_aes
===================

.. c:function:: int ext4_derive_key_aes(char deriving_key[EXT4_AES_128_ECB_KEY_SIZE], char source_key[EXT4_AES_256_XTS_KEY_SIZE], char derived_key[EXT4_AES_256_XTS_KEY_SIZE])

    Derive a key using AES-128-ECB

    :param char deriving_key:
        Encryption key used for derivation.

    :param char source_key:
        Source key to which to apply derivation.

    :param char derived_key:
        Derived key.

.. _`ext4_derive_key_aes.return`:

Return
------

Zero on success; non-zero otherwise.

.. This file was automatic generated / don't edit.

