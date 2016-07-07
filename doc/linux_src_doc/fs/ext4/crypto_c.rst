.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/crypto.c

.. _`ext4_release_crypto_ctx`:

ext4_release_crypto_ctx
=======================

.. c:function:: void ext4_release_crypto_ctx(struct ext4_crypto_ctx *ctx)

    Releases an encryption context

    :param struct ext4_crypto_ctx \*ctx:
        The encryption context to release.

.. _`ext4_release_crypto_ctx.description`:

Description
-----------

If the encryption context was allocated from the pre-allocated pool, returns
it to that pool. Else, frees it.

If there's a bounce page in the context, this frees that.

.. _`ext4_get_crypto_ctx`:

ext4_get_crypto_ctx
===================

.. c:function:: struct ext4_crypto_ctx *ext4_get_crypto_ctx(struct inode *inode, gfp_t gfp_flags)

    Gets an encryption context

    :param struct inode \*inode:
        The inode for which we are doing the crypto

    :param gfp_t gfp_flags:
        *undescribed*

.. _`ext4_get_crypto_ctx.description`:

Description
-----------

Allocates and initializes an encryption context.

.. _`ext4_get_crypto_ctx.return`:

Return
------

An allocated and initialized encryption context on success; error
value or NULL otherwise.

.. _`ext4_exit_crypto`:

ext4_exit_crypto
================

.. c:function:: void ext4_exit_crypto( void)

    Shutdown the ext4 encryption system

    :param  void:
        no arguments

.. _`ext4_init_crypto`:

ext4_init_crypto
================

.. c:function:: int ext4_init_crypto( void)

    Set up for ext4 encryption.

    :param  void:
        no arguments

.. _`ext4_init_crypto.description`:

Description
-----------

We only call this when we start accessing encrypted files, since it
results in memory getting allocated that wouldn't otherwise be used.

.. _`ext4_init_crypto.return`:

Return
------

Zero on success, non-zero otherwise.

.. _`ext4_crypt_complete`:

ext4_crypt_complete
===================

.. c:function:: void ext4_crypt_complete(struct crypto_async_request *req, int res)

    The completion callback for page encryption

    :param struct crypto_async_request \*req:
        The asynchronous encryption request context

    :param int res:
        The result of the encryption operation

.. _`ext4_encrypt`:

ext4_encrypt
============

.. c:function:: struct page *ext4_encrypt(struct inode *inode, struct page *plaintext_page, gfp_t gfp_flags)

    Encrypts a page

    :param struct inode \*inode:
        The inode for which the encryption should take place

    :param struct page \*plaintext_page:
        The page to encrypt. Must be locked.

    :param gfp_t gfp_flags:
        *undescribed*

.. _`ext4_encrypt.description`:

Description
-----------

Allocates a ciphertext page and encrypts plaintext_page into it using the ctx
encryption context.

Called on the page write path.  The caller must call
\ :c:func:`ext4_restore_control_page`\  on the returned ciphertext page to
release the bounce buffer and the encryption context.

.. _`ext4_encrypt.return`:

Return
------

An allocated page with the encrypted content on success. Else, an
error value or NULL.

.. _`ext4_decrypt`:

ext4_decrypt
============

.. c:function:: int ext4_decrypt(struct page *page)

    Decrypts a page in-place

    :param struct page \*page:
        The page to decrypt. Must be locked.

.. _`ext4_decrypt.description`:

Description
-----------

Decrypts page in-place using the ctx encryption context.

Called from the read completion callback.

.. _`ext4_decrypt.return`:

Return
------

Zero on success, non-zero otherwise.

.. _`ext4_validate_encryption_key_size`:

ext4_validate_encryption_key_size
=================================

.. c:function:: uint32_t ext4_validate_encryption_key_size(uint32_t mode, uint32_t size)

    Validate the encryption key size

    :param uint32_t mode:
        The key mode.

    :param uint32_t size:
        The key size to validate.

.. _`ext4_validate_encryption_key_size.return`:

Return
------

The validated key size for \ ``mode``\ . Zero if invalid.

.. This file was automatic generated / don't edit.

