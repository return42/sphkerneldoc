.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/crypto/fname.c

.. _`fname_crypt_complete`:

fname_crypt_complete
====================

.. c:function:: void fname_crypt_complete(struct crypto_async_request *req, int res)

    completion callback for filename crypto

    :param struct crypto_async_request \*req:
        The asynchronous cipher request context

    :param int res:
        The result of the cipher operation

.. _`fname_encrypt`:

fname_encrypt
=============

.. c:function:: int fname_encrypt(struct inode *inode, const struct qstr *iname, struct fscrypt_str *oname)

    encrypt a filename

    :param struct inode \*inode:
        *undescribed*

    :param const struct qstr \*iname:
        *undescribed*

    :param struct fscrypt_str \*oname:
        *undescribed*

.. _`fname_encrypt.description`:

Description
-----------

The caller must have allocated sufficient memory for the \ ``oname``\  string.

.. _`fname_encrypt.return`:

Return
------

0 on success, -errno on failure

.. _`fname_decrypt`:

fname_decrypt
=============

.. c:function:: int fname_decrypt(struct inode *inode, const struct fscrypt_str *iname, struct fscrypt_str *oname)

    decrypt a filename

    :param struct inode \*inode:
        *undescribed*

    :param const struct fscrypt_str \*iname:
        *undescribed*

    :param struct fscrypt_str \*oname:
        *undescribed*

.. _`fname_decrypt.description`:

Description
-----------

The caller must have allocated sufficient memory for the \ ``oname``\  string.

.. _`fname_decrypt.return`:

Return
------

0 on success, -errno on failure

.. _`digest_encode`:

digest_encode
=============

.. c:function:: int digest_encode(const char *src, int len, char *dst)

    :param const char \*src:
        *undescribed*

    :param int len:
        *undescribed*

    :param char \*dst:
        *undescribed*

.. _`digest_encode.description`:

Description
-----------

Encodes the input digest using characters from the set [a-zA-Z0-9_+].
The encoded string is roughly 4/3 times the size of the input string.

.. _`fscrypt_fname_alloc_buffer`:

fscrypt_fname_alloc_buffer
==========================

.. c:function:: int fscrypt_fname_alloc_buffer(struct inode *inode, u32 ilen, struct fscrypt_str *crypto_str)

    :param struct inode \*inode:
        *undescribed*

    :param u32 ilen:
        *undescribed*

    :param struct fscrypt_str \*crypto_str:
        *undescribed*

.. _`fscrypt_fname_alloc_buffer.description`:

Description
-----------

Allocates an output buffer that is sufficient for the crypto operation
specified by the context and the direction.

.. _`fscrypt_fname_free_buffer`:

fscrypt_fname_free_buffer
=========================

.. c:function:: void fscrypt_fname_free_buffer(struct fscrypt_str *crypto_str)

    :param struct fscrypt_str \*crypto_str:
        *undescribed*

.. _`fscrypt_fname_free_buffer.description`:

Description
-----------

Frees the buffer allocated for crypto operation.

.. _`fscrypt_fname_disk_to_usr`:

fscrypt_fname_disk_to_usr
=========================

.. c:function:: int fscrypt_fname_disk_to_usr(struct inode *inode, u32 hash, u32 minor_hash, const struct fscrypt_str *iname, struct fscrypt_str *oname)

    converts a filename from disk space to user space

    :param struct inode \*inode:
        *undescribed*

    :param u32 hash:
        *undescribed*

    :param u32 minor_hash:
        *undescribed*

    :param const struct fscrypt_str \*iname:
        *undescribed*

    :param struct fscrypt_str \*oname:
        *undescribed*

.. _`fscrypt_fname_disk_to_usr.description`:

Description
-----------

The caller must have allocated sufficient memory for the \ ``oname``\  string.

.. _`fscrypt_fname_disk_to_usr.return`:

Return
------

0 on success, -errno on failure

.. _`fscrypt_fname_usr_to_disk`:

fscrypt_fname_usr_to_disk
=========================

.. c:function:: int fscrypt_fname_usr_to_disk(struct inode *inode, const struct qstr *iname, struct fscrypt_str *oname)

    converts a filename from user space to disk space

    :param struct inode \*inode:
        *undescribed*

    :param const struct qstr \*iname:
        *undescribed*

    :param struct fscrypt_str \*oname:
        *undescribed*

.. _`fscrypt_fname_usr_to_disk.description`:

Description
-----------

The caller must have allocated sufficient memory for the \ ``oname``\  string.

.. _`fscrypt_fname_usr_to_disk.return`:

Return
------

0 on success, -errno on failure

.. This file was automatic generated / don't edit.

