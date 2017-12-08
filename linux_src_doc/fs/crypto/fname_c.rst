.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/crypto/fname.c

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

.. c:function:: int fscrypt_fname_alloc_buffer(const struct inode *inode, u32 ilen, struct fscrypt_str *crypto_str)

    :param const struct inode \*inode:
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

If the key is available, we'll decrypt the disk name; otherwise, we'll encode
it for presentation.  Short names are directly base64-encoded, while long
names are encoded in fscrypt_digested_name format.

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

.. _`fscrypt_setup_filename`:

fscrypt_setup_filename
======================

.. c:function:: int fscrypt_setup_filename(struct inode *dir, const struct qstr *iname, int lookup, struct fscrypt_name *fname)

    prepare to search a possibly encrypted directory

    :param struct inode \*dir:
        the directory that will be searched

    :param const struct qstr \*iname:
        the user-provided filename being searched for

    :param int lookup:
        1 if we're allowed to proceed without the key because it's
        ->lookup() or we're finding the dir_entry for deletion; 0 if we cannot
        proceed without the key because we're going to create the dir_entry.

    :param struct fscrypt_name \*fname:
        the filename information to be filled in

.. _`fscrypt_setup_filename.description`:

Description
-----------

Given a user-provided filename \ ``iname``\ , this function sets \ ``fname``\ ->disk_name
to the name that would be stored in the on-disk directory entry, if possible.
If the directory is unencrypted this is simply \ ``iname``\ .  Else, if we have the
directory's encryption key, then \ ``iname``\  is the plaintext, so we encrypt it to
get the disk_name.

Else, for keyless \ ``lookup``\  operations, \ ``iname``\  is the presented ciphertext, so
we decode it to get either the ciphertext disk_name (for short names) or the
fscrypt_digested_name (for long names).  Non-@lookup operations will be
impossible in this case, so we fail them with ENOKEY.

If successful, \ :c:func:`fscrypt_free_filename`\  must be called later to clean up.

.. _`fscrypt_setup_filename.return`:

Return
------

0 on success, -errno on failure

.. This file was automatic generated / don't edit.

