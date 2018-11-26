.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/crypto/fname.c

.. _`fname_encrypt`:

fname_encrypt
=============

.. c:function:: int fname_encrypt(struct inode *inode, const struct qstr *iname, u8 *out, unsigned int olen)

    encrypt a filename

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param iname:
        *undescribed*
    :type iname: const struct qstr \*

    :param out:
        *undescribed*
    :type out: u8 \*

    :param olen:
        *undescribed*
    :type olen: unsigned int

.. _`fname_encrypt.description`:

Description
-----------

The output buffer must be at least as large as the input buffer.
Any extra space is filled with NUL padding before encryption.

.. _`fname_encrypt.return`:

Return
------

0 on success, -errno on failure

.. _`fname_decrypt`:

fname_decrypt
=============

.. c:function:: int fname_decrypt(struct inode *inode, const struct fscrypt_str *iname, struct fscrypt_str *oname)

    decrypt a filename

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param iname:
        *undescribed*
    :type iname: const struct fscrypt_str \*

    :param oname:
        *undescribed*
    :type oname: struct fscrypt_str \*

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

    :param src:
        *undescribed*
    :type src: const char \*

    :param len:
        *undescribed*
    :type len: int

    :param dst:
        *undescribed*
    :type dst: char \*

.. _`digest_encode.description`:

Description
-----------

Encodes the input digest using characters from the set [a-zA-Z0-9_+].
The encoded string is roughly 4/3 times the size of the input string.

.. _`fscrypt_fname_alloc_buffer`:

fscrypt_fname_alloc_buffer
==========================

.. c:function:: int fscrypt_fname_alloc_buffer(const struct inode *inode, u32 max_encrypted_len, struct fscrypt_str *crypto_str)

    allocate a buffer for presented filenames

    :param inode:
        *undescribed*
    :type inode: const struct inode \*

    :param max_encrypted_len:
        *undescribed*
    :type max_encrypted_len: u32

    :param crypto_str:
        *undescribed*
    :type crypto_str: struct fscrypt_str \*

.. _`fscrypt_fname_alloc_buffer.description`:

Description
-----------

Allocate a buffer that is large enough to hold any decrypted or encoded
filename (null-terminated), for the given maximum encrypted filename length.

.. _`fscrypt_fname_alloc_buffer.return`:

Return
------

0 on success, -errno on failure

.. _`fscrypt_fname_free_buffer`:

fscrypt_fname_free_buffer
=========================

.. c:function:: void fscrypt_fname_free_buffer(struct fscrypt_str *crypto_str)

    free the buffer for presented filenames

    :param crypto_str:
        *undescribed*
    :type crypto_str: struct fscrypt_str \*

.. _`fscrypt_fname_free_buffer.description`:

Description
-----------

Free the buffer allocated by \ :c:func:`fscrypt_fname_alloc_buffer`\ .

.. _`fscrypt_fname_disk_to_usr`:

fscrypt_fname_disk_to_usr
=========================

.. c:function:: int fscrypt_fname_disk_to_usr(struct inode *inode, u32 hash, u32 minor_hash, const struct fscrypt_str *iname, struct fscrypt_str *oname)

    converts a filename from disk space to user space

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param hash:
        *undescribed*
    :type hash: u32

    :param minor_hash:
        *undescribed*
    :type minor_hash: u32

    :param iname:
        *undescribed*
    :type iname: const struct fscrypt_str \*

    :param oname:
        *undescribed*
    :type oname: struct fscrypt_str \*

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

.. _`fscrypt_setup_filename`:

fscrypt_setup_filename
======================

.. c:function:: int fscrypt_setup_filename(struct inode *dir, const struct qstr *iname, int lookup, struct fscrypt_name *fname)

    prepare to search a possibly encrypted directory

    :param dir:
        the directory that will be searched
    :type dir: struct inode \*

    :param iname:
        the user-provided filename being searched for
    :type iname: const struct qstr \*

    :param lookup:
        1 if we're allowed to proceed without the key because it's
        ->lookup() or we're finding the dir_entry for deletion; 0 if we cannot
        proceed without the key because we're going to create the dir_entry.
    :type lookup: int

    :param fname:
        the filename information to be filled in
    :type fname: struct fscrypt_name \*

.. _`fscrypt_setup_filename.description`:

Description
-----------

Given a user-provided filename \ ``iname``\ , this function sets \ ``fname->disk_name``\ 
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

