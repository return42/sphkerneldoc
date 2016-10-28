.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/crypto_fname.c

.. _`ext4_dir_crypt_complete`:

ext4_dir_crypt_complete
=======================

.. c:function:: void ext4_dir_crypt_complete(struct crypto_async_request *req, int res)

    :param struct crypto_async_request \*req:
        *undescribed*

    :param int res:
        *undescribed*

.. _`ext4_fname_encrypt`:

ext4_fname_encrypt
==================

.. c:function:: int ext4_fname_encrypt(struct inode *inode, const struct qstr *iname, struct ext4_str *oname)

    :param struct inode \*inode:
        *undescribed*

    :param const struct qstr \*iname:
        *undescribed*

    :param struct ext4_str \*oname:
        *undescribed*

.. _`ext4_fname_encrypt.description`:

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

.. _`ext4_fname_crypto_round_up`:

ext4_fname_crypto_round_up
==========================

.. c:function:: u32 ext4_fname_crypto_round_up(u32 size, u32 blksize)

    :param u32 size:
        *undescribed*

    :param u32 blksize:
        *undescribed*

.. _`ext4_fname_crypto_round_up.return`:

Return
------

The next multiple of block size

.. _`ext4_fname_crypto_free_buffer`:

ext4_fname_crypto_free_buffer
=============================

.. c:function:: void ext4_fname_crypto_free_buffer(struct ext4_str *crypto_str)

    :param struct ext4_str \*crypto_str:
        *undescribed*

.. _`ext4_fname_crypto_free_buffer.description`:

Description
-----------

Frees the buffer allocated for crypto operation.

.. _`_ext4_fname_disk_to_usr`:

_ext4_fname_disk_to_usr
=======================

.. c:function:: int _ext4_fname_disk_to_usr(struct inode *inode, struct dx_hash_info *hinfo, const struct ext4_str *iname, struct ext4_str *oname)

    converts a filename from disk space to user space

    :param struct inode \*inode:
        *undescribed*

    :param struct dx_hash_info \*hinfo:
        *undescribed*

    :param const struct ext4_str \*iname:
        *undescribed*

    :param struct ext4_str \*oname:
        *undescribed*

.. _`ext4_fname_usr_to_disk`:

ext4_fname_usr_to_disk
======================

.. c:function:: int ext4_fname_usr_to_disk(struct inode *inode, const struct qstr *iname, struct ext4_str *oname)

    converts a filename from user space to disk space

    :param struct inode \*inode:
        *undescribed*

    :param const struct qstr \*iname:
        *undescribed*

    :param struct ext4_str \*oname:
        *undescribed*

.. This file was automatic generated / don't edit.

