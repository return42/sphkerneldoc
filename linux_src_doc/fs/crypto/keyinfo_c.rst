.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/crypto/keyinfo.c

.. _`derive_key_aes`:

derive_key_aes
==============

.. c:function:: int derive_key_aes(u8 deriving_key, const struct fscrypt_key *source_key, u8 derived_raw_key)

    Derive a key using AES-128-ECB

    :param u8 deriving_key:
        Encryption key used for derivation.

    :param const struct fscrypt_key \*source_key:
        Source key to which to apply derivation.

    :param u8 derived_raw_key:
        Derived raw key.

.. _`derive_key_aes.return`:

Return
------

Zero on success; non-zero otherwise.

.. This file was automatic generated / don't edit.

