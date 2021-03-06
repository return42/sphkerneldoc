.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/aes_generic.c

.. _`crypto_aes_expand_key`:

crypto_aes_expand_key
=====================

.. c:function:: int crypto_aes_expand_key(struct crypto_aes_ctx *ctx, const u8 *in_key, unsigned int key_len)

    Expands the AES key as described in FIPS-197

    :param ctx:
        The location where the computed key will be stored.
    :type ctx: struct crypto_aes_ctx \*

    :param in_key:
        The supplied key.
    :type in_key: const u8 \*

    :param key_len:
        The length of the supplied key.
    :type key_len: unsigned int

.. _`crypto_aes_expand_key.description`:

Description
-----------

Returns 0 on success. The function fails only if an invalid key size (or
pointer) is supplied.
The expanded key size is 240 bytes (max of 14 rounds with a unique 16 bytes
key schedule plus a 16 bytes key which is used before the first round).
The decryption key is prepared for the "Equivalent Inverse Cipher" as
described in FIPS-197. The first slot (16 bytes) of each key (enc or dec) is
for the initial combination, the second slot for the first round and so on.

.. _`crypto_aes_set_key`:

crypto_aes_set_key
==================

.. c:function:: int crypto_aes_set_key(struct crypto_tfm *tfm, const u8 *in_key, unsigned int key_len)

    Set the AES key.

    :param tfm:
        The \ ``crypto_tfm``\  that is used in the context.
    :type tfm: struct crypto_tfm \*

    :param in_key:
        The input key.
    :type in_key: const u8 \*

    :param key_len:
        The size of the key.
    :type key_len: unsigned int

.. _`crypto_aes_set_key.description`:

Description
-----------

Returns 0 on success, on failure the \ ``CRYPTO_TFM_RES_BAD_KEY_LEN``\  flag in tfm
is set. The function uses \ :c:func:`crypto_aes_expand_key`\  to expand the key.
\ :c:type:`struct crypto_aes_ctx <crypto_aes_ctx>`\  \_must\_ be the private data embedded in \ ``tfm``\  which is
retrieved with \ :c:func:`crypto_tfm_ctx`\ .

.. This file was automatic generated / don't edit.

