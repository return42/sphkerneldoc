.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/crypto/hooks.c

.. _`fscrypt_file_open`:

fscrypt_file_open
=================

.. c:function:: int fscrypt_file_open(struct inode *inode, struct file *filp)

    prepare to open a possibly-encrypted regular file

    :param struct inode \*inode:
        the inode being opened

    :param struct file \*filp:
        the struct file being set up

.. _`fscrypt_file_open.description`:

Description
-----------

Currently, an encrypted regular file can only be opened if its encryption key
is available; access to the raw encrypted contents is not supported.
Therefore, we first set up the inode's encryption key (if not already done)
and return an error if it's unavailable.

We also verify that if the parent directory (from the path via which the file
is being opened) is encrypted, then the inode being opened uses the same
encryption policy.  This is needed as part of the enforcement that all files
in an encrypted directory tree use the same encryption policy, as a
protection against certain types of offline attacks.  Note that this check is
needed even when opening an \*unencrypted\* file, since it's forbidden to have
an unencrypted file in an encrypted directory.

.. _`fscrypt_file_open.return`:

Return
------

0 on success, -ENOKEY if the key is missing, or another -errno code

.. This file was automatic generated / don't edit.

