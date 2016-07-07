.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/crypto/fname.c

.. _`dir_crypt_complete`:

dir_crypt_complete
==================

.. c:function:: void dir_crypt_complete(struct crypto_async_request *req, int res)

    :param struct crypto_async_request \*req:
        *undescribed*

    :param int res:
        *undescribed*

.. _`fname_encrypt`:

fname_encrypt
=============

.. c:function:: int fname_encrypt(struct inode *inode, const struct qstr *iname, struct fscrypt_str *oname)

    :param struct inode \*inode:
        *undescribed*

    :param const struct qstr \*iname:
        *undescribed*

    :param struct fscrypt_str \*oname:
        *undescribed*

.. _`fname_encrypt.description`:

Description
-----------

This function encrypts the input filename, and returns the length of the
ciphertext. Errors are returned as negative numbers.  We trust the caller to
allocate sufficient memory to oname string.

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

.. This file was automatic generated / don't edit.

