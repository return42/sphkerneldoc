.. -*- coding: utf-8; mode: rst -*-

=========
keyinfo.c
=========


.. _`derive_key_aes`:

derive_key_aes
==============

.. c:function:: int derive_key_aes (u8 deriving_key[FS_AES_128_ECB_KEY_SIZE], u8 source_key[FS_AES_256_XTS_KEY_SIZE], u8 derived_key[FS_AES_256_XTS_KEY_SIZE])

    Derive a key using AES-128-ECB

    :param u8 deriving_key:
        Encryption key used for derivation.

    :param u8 source_key:
        Source key to which to apply derivation.

    :param u8 derived_key:
        Derived key.



.. _`derive_key_aes.return`:

Return
------

Zero on success; non-zero otherwise.

