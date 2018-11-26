.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/sm4_generic.c

.. _`crypto_sm4_expand_key`:

crypto_sm4_expand_key
=====================

.. c:function:: int crypto_sm4_expand_key(struct crypto_sm4_ctx *ctx, const u8 *in_key, unsigned int key_len)

    Expands the SM4 key as described in GB/T 32907-2016

    :param ctx:
        The location where the computed key will be stored.
    :type ctx: struct crypto_sm4_ctx \*

    :param in_key:
        The supplied key.
    :type in_key: const u8 \*

    :param key_len:
        The length of the supplied key.
    :type key_len: unsigned int

.. _`crypto_sm4_expand_key.description`:

Description
-----------

Returns 0 on success. The function fails only if an invalid key size (or
pointer) is supplied.

.. _`crypto_sm4_set_key`:

crypto_sm4_set_key
==================

.. c:function:: int crypto_sm4_set_key(struct crypto_tfm *tfm, const u8 *in_key, unsigned int key_len)

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

.. _`crypto_sm4_set_key.description`:

Description
-----------

Returns 0 on success, on failure the \ ``CRYPTO_TFM_RES_BAD_KEY_LEN``\  flag in tfm
is set. The function uses \ :c:func:`crypto_sm4_expand_key`\  to expand the key.
\ :c:type:`struct crypto_sm4_ctx <crypto_sm4_ctx>`\  \_must\_ be the private data embedded in \ ``tfm``\  which is
retrieved with \ :c:func:`crypto_tfm_ctx`\ .

.. This file was automatic generated / don't edit.

