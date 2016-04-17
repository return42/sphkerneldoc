.. -*- coding: utf-8; mode: rst -*-

=============
aes_generic.c
=============


.. _`crypto_aes_expand_key`:

crypto_aes_expand_key
=====================

.. c:function:: int crypto_aes_expand_key (struct crypto_aes_ctx *ctx, const u8 *in_key, unsigned int key_len)

    Expands the AES key as described in FIPS-197

    :param struct crypto_aes_ctx \*ctx:
        The location where the computed key will be stored.

    :param const u8 \*in_key:
        The supplied key.

    :param unsigned int key_len:
        The length of the supplied key.



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

.. c:function:: int crypto_aes_set_key (struct crypto_tfm *tfm, const u8 *in_key, unsigned int key_len)

    Set the AES key.

    :param struct crypto_tfm \*tfm:
        The ``crypto_tfm`` that is used in the context.

    :param const u8 \*in_key:
        The input key.

    :param unsigned int key_len:
        The size of the key.



.. _`crypto_aes_set_key.description`:

Description
-----------

Returns 0 on success, on failure the ``CRYPTO_TFM_RES_BAD_KEY_LEN`` flag in tfm
is set. The function uses :c:func:`crypto_aes_expand_key` to expand the key.
:c:type:`struct crypto_aes_ctx <crypto_aes_ctx>` _must_ be the private data embedded in ``tfm`` which is
retrieved with :c:func:`crypto_tfm_ctx`.

