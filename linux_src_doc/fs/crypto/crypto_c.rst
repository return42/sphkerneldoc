.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/crypto/crypto.c

.. _`fscrypt_release_ctx`:

fscrypt_release_ctx
===================

.. c:function:: void fscrypt_release_ctx(struct fscrypt_ctx *ctx)

    Releases an encryption context

    :param ctx:
        The encryption context to release.
    :type ctx: struct fscrypt_ctx \*

.. _`fscrypt_release_ctx.description`:

Description
-----------

If the encryption context was allocated from the pre-allocated pool, returns
it to that pool. Else, frees it.

If there's a bounce page in the context, this frees that.

.. _`fscrypt_get_ctx`:

fscrypt_get_ctx
===============

.. c:function:: struct fscrypt_ctx *fscrypt_get_ctx(const struct inode *inode, gfp_t gfp_flags)

    Gets an encryption context

    :param inode:
        The inode for which we are doing the crypto
    :type inode: const struct inode \*

    :param gfp_flags:
        The gfp flag for memory allocation
    :type gfp_flags: gfp_t

.. _`fscrypt_get_ctx.description`:

Description
-----------

Allocates and initializes an encryption context.

.. _`fscrypt_get_ctx.return`:

Return
------

An allocated and initialized encryption context on success; error
value or NULL otherwise.

.. _`fscrypt_encrypt_page`:

fscrypt_encrypt_page
====================

.. c:function:: struct page *fscrypt_encrypt_page(const struct inode *inode, struct page *page, unsigned int len, unsigned int offs, u64 lblk_num, gfp_t gfp_flags)

    Encrypts a page

    :param inode:
        The inode for which the encryption should take place
    :type inode: const struct inode \*

    :param page:
        The page to encrypt. Must be locked for bounce-page
        encryption.
    :type page: struct page \*

    :param len:
        Length of data to encrypt in \ ``page``\  and encrypted
        data in returned page.
    :type len: unsigned int

    :param offs:
        Offset of data within \ ``page``\  and returned
        page holding encrypted data.
    :type offs: unsigned int

    :param lblk_num:
        Logical block number. This must be unique for multiple
        calls with same inode, except when overwriting
        previously written data.
    :type lblk_num: u64

    :param gfp_flags:
        The gfp flag for memory allocation
    :type gfp_flags: gfp_t

.. _`fscrypt_encrypt_page.description`:

Description
-----------

Encrypts \ ``page``\  using the ctx encryption context. Performs encryption
either in-place or into a newly allocated bounce page.
Called on the page write path.

Bounce page allocation is the default.
In this case, the contents of \ ``page``\  are encrypted and stored in an
allocated bounce page. \ ``page``\  has to be locked and the caller must call
\ :c:func:`fscrypt_restore_control_page`\  on the returned ciphertext page to
release the bounce buffer and the encryption context.

In-place encryption is used by setting the FS_CFLG_OWN_PAGES flag in
fscrypt_operations. Here, the input-page is returned with its content
encrypted.

.. _`fscrypt_encrypt_page.return`:

Return
------

A page with the encrypted content on success. Else, an
error value or NULL.

.. _`fscrypt_decrypt_page`:

fscrypt_decrypt_page
====================

.. c:function:: int fscrypt_decrypt_page(const struct inode *inode, struct page *page, unsigned int len, unsigned int offs, u64 lblk_num)

    Decrypts a page in-place

    :param inode:
        The corresponding inode for the page to decrypt.
    :type inode: const struct inode \*

    :param page:
        The page to decrypt. Must be locked in case
        it is a writeback page (FS_CFLG_OWN_PAGES unset).
    :type page: struct page \*

    :param len:
        Number of bytes in \ ``page``\  to be decrypted.
    :type len: unsigned int

    :param offs:
        Start of data in \ ``page``\ .
    :type offs: unsigned int

    :param lblk_num:
        Logical block number.
    :type lblk_num: u64

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

.. c:function:: int fscrypt_initialize(unsigned int cop_flags)

    allocate major buffers for fs encryption.

    :param cop_flags:
        fscrypt operations flags
    :type cop_flags: unsigned int

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

    :param void:
        no arguments
    :type void: 

.. _`fscrypt_exit`:

fscrypt_exit
============

.. c:function:: void __exit fscrypt_exit( void)

    Shutdown the fs encryption system

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

