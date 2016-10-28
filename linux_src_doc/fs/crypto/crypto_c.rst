.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/crypto/crypto.c

.. _`fscrypt_release_ctx`:

fscrypt_release_ctx
===================

.. c:function:: void fscrypt_release_ctx(struct fscrypt_ctx *ctx)

    Releases an encryption context

    :param struct fscrypt_ctx \*ctx:
        The encryption context to release.

.. _`fscrypt_release_ctx.description`:

Description
-----------

If the encryption context was allocated from the pre-allocated pool, returns
it to that pool. Else, frees it.

If there's a bounce page in the context, this frees that.

.. _`fscrypt_get_ctx`:

fscrypt_get_ctx
===============

.. c:function:: struct fscrypt_ctx *fscrypt_get_ctx(struct inode *inode, gfp_t gfp_flags)

    Gets an encryption context

    :param struct inode \*inode:
        The inode for which we are doing the crypto

    :param gfp_t gfp_flags:
        The gfp flag for memory allocation

.. _`fscrypt_get_ctx.description`:

Description
-----------

Allocates and initializes an encryption context.

.. _`fscrypt_get_ctx.return`:

Return
------

An allocated and initialized encryption context on success; error
value or NULL otherwise.

.. _`fscrypt_complete`:

fscrypt_complete
================

.. c:function:: void fscrypt_complete(struct crypto_async_request *req, int res)

    The completion callback for page encryption

    :param struct crypto_async_request \*req:
        The asynchronous encryption request context

    :param int res:
        The result of the encryption operation

.. _`fscrypt_encrypt_page`:

fscrypt_encrypt_page
====================

.. c:function:: struct page *fscrypt_encrypt_page(struct inode *inode, struct page *plaintext_page, gfp_t gfp_flags)

    Encrypts a page

    :param struct inode \*inode:
        The inode for which the encryption should take place

    :param struct page \*plaintext_page:
        The page to encrypt. Must be locked.

    :param gfp_t gfp_flags:
        The gfp flag for memory allocation

.. _`fscrypt_encrypt_page.description`:

Description
-----------

Allocates a ciphertext page and encrypts plaintext_page into it using the ctx
encryption context.

Called on the page write path.  The caller must call
\ :c:func:`fscrypt_restore_control_page`\  on the returned ciphertext page to
release the bounce buffer and the encryption context.

.. _`fscrypt_encrypt_page.return`:

Return
------

An allocated page with the encrypted content on success. Else, an
error value or NULL.

.. _`fscrypt_decrypt_page`:

fscrypt_decrypt_page
====================

.. c:function:: int fscrypt_decrypt_page(struct page *page)

    Decrypts a page in-place

    :param struct page \*page:
        The page to decrypt. Must be locked.

.. _`fscrypt_decrypt_page.description`:

Description
-----------

Decrypts page in-place using the ctx encryption context.

Called from the read completion callback.

.. _`fscrypt_decrypt_page.return`:

Return
------

Zero on success, non-zero otherwise.

.. _`fscrypt_initialize`:

fscrypt_initialize
==================

.. c:function:: int fscrypt_initialize( void)

    allocate major buffers for fs encryption.

    :param  void:
        no arguments

.. _`fscrypt_initialize.description`:

Description
-----------

We only call this when we start accessing encrypted files, since it
results in memory getting allocated that wouldn't otherwise be used.

.. _`fscrypt_initialize.return`:

Return
------

Zero on success, non-zero otherwise.

.. _`fscrypt_init`:

fscrypt_init
============

.. c:function:: int fscrypt_init( void)

    Set up for fs encryption.

    :param  void:
        no arguments

.. _`fscrypt_exit`:

fscrypt_exit
============

.. c:function:: void __exit fscrypt_exit( void)

    Shutdown the fs encryption system

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

