.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/fscrypt.h

.. _`fscrypt_require_key`:

fscrypt_require_key
===================

.. c:function:: int fscrypt_require_key(struct inode *inode)

    require an inode's encryption key

    :param struct inode \*inode:
        the inode we need the key for

.. _`fscrypt_require_key.description`:

Description
-----------

If the inode is encrypted, set up its encryption key if not already done.
Then require that the key be present and return -ENOKEY otherwise.

No locks are needed, and the key will live as long as the struct inode --- so
it won't go away from under you.

.. _`fscrypt_require_key.return`:

Return
------

0 on success, -ENOKEY if the key is missing, or another -errno code
if a problem occurred while setting up the encryption key.

.. _`fscrypt_prepare_link`:

fscrypt_prepare_link
====================

.. c:function:: int fscrypt_prepare_link(struct dentry *old_dentry, struct inode *dir, struct dentry *dentry)

    prepare to link an inode into a possibly-encrypted directory

    :param struct dentry \*old_dentry:
        an existing dentry for the inode being linked

    :param struct inode \*dir:
        the target directory

    :param struct dentry \*dentry:
        negative dentry for the target filename

.. _`fscrypt_prepare_link.description`:

Description
-----------

A new link can only be added to an encrypted directory if the directory's
encryption key is available --- since otherwise we'd have no way to encrypt
the filename.  Therefore, we first set up the directory's encryption key (if
not already done) and return an error if it's unavailable.

We also verify that the link will not violate the constraint that all files
in an encrypted directory tree use the same encryption policy.

.. _`fscrypt_prepare_link.return`:

Return
------

0 on success, -ENOKEY if the directory's encryption key is missing,
-EPERM if the link would result in an inconsistent encryption policy, or
another -errno code.

.. _`fscrypt_prepare_rename`:

fscrypt_prepare_rename
======================

.. c:function:: int fscrypt_prepare_rename(struct inode *old_dir, struct dentry *old_dentry, struct inode *new_dir, struct dentry *new_dentry, unsigned int flags)

    prepare for a rename between possibly-encrypted directories

    :param struct inode \*old_dir:
        source directory

    :param struct dentry \*old_dentry:
        dentry for source file

    :param struct inode \*new_dir:
        target directory

    :param struct dentry \*new_dentry:
        dentry for target location (may be negative unless exchanging)

    :param unsigned int flags:
        rename flags (we care at least about \ ``RENAME_EXCHANGE``\ )

.. _`fscrypt_prepare_rename.description`:

Description
-----------

Prepare for ->rename() where the source and/or target directories may be
encrypted.  A new link can only be added to an encrypted directory if the
directory's encryption key is available --- since otherwise we'd have no way
to encrypt the filename.  A rename to an existing name, on the other hand,
\*is\* cryptographically possible without the key.  However, we take the more
conservative approach and just forbid all no-key renames.

We also verify that the rename will not violate the constraint that all files
in an encrypted directory tree use the same encryption policy.

.. _`fscrypt_prepare_rename.return`:

Return
------

0 on success, -ENOKEY if an encryption key is missing, -EPERM if the
rename would cause inconsistent encryption policies, or another -errno code.

.. _`fscrypt_prepare_lookup`:

fscrypt_prepare_lookup
======================

.. c:function:: int fscrypt_prepare_lookup(struct inode *dir, struct dentry *dentry, unsigned int flags)

    prepare to lookup a name in a possibly-encrypted directory

    :param struct inode \*dir:
        directory being searched

    :param struct dentry \*dentry:
        filename being looked up

    :param unsigned int flags:
        lookup flags

.. _`fscrypt_prepare_lookup.description`:

Description
-----------

Prepare for ->lookup() in a directory which may be encrypted.  Lookups can be
done with or without the directory's encryption key; without the key,
filenames are presented in encrypted form.  Therefore, we'll try to set up
the directory's encryption key, but even without it the lookup can continue.

To allow invalidating stale dentries if the directory's encryption key is
added later, we also install a custom ->d_revalidate() method and use the
DCACHE_ENCRYPTED_WITH_KEY flag to indicate whether a given dentry is a
plaintext name (flag set) or a ciphertext name (flag cleared).

.. _`fscrypt_prepare_lookup.return`:

Return
------

0 on success, -errno if a problem occurred while setting up the
encryption key

.. _`fscrypt_prepare_setattr`:

fscrypt_prepare_setattr
=======================

.. c:function:: int fscrypt_prepare_setattr(struct dentry *dentry, struct iattr *attr)

    prepare to change a possibly-encrypted inode's attributes

    :param struct dentry \*dentry:
        dentry through which the inode is being changed

    :param struct iattr \*attr:
        attributes to change

.. _`fscrypt_prepare_setattr.description`:

Description
-----------

Prepare for ->setattr() on a possibly-encrypted inode.  On an encrypted file,
most attribute changes are allowed even without the encryption key.  However,
without the encryption key we do have to forbid truncates.  This is needed
because the size being truncated to may not be a multiple of the filesystem
block size, and in that case we'd have to decrypt the final block, zero the
portion past i_size, and re-encrypt it.  (We \*could\* allow truncating to a
filesystem block boundary, but it's simpler to just forbid all truncates ---
and we already forbid all other contents modifications without the key.)

.. _`fscrypt_prepare_setattr.return`:

Return
------

0 on success, -ENOKEY if the key is missing, or another -errno code
if a problem occurred while setting up the encryption key.

.. _`fscrypt_prepare_symlink`:

fscrypt_prepare_symlink
=======================

.. c:function:: int fscrypt_prepare_symlink(struct inode *dir, const char *target, unsigned int len, unsigned int max_len, struct fscrypt_str *disk_link)

    prepare to create a possibly-encrypted symlink

    :param struct inode \*dir:
        directory in which the symlink is being created

    :param const char \*target:
        plaintext symlink target

    :param unsigned int len:
        length of \ ``target``\  excluding null terminator

    :param unsigned int max_len:
        space the filesystem has available to store the symlink target

    :param struct fscrypt_str \*disk_link:
        (out) the on-disk symlink target being prepared

.. _`fscrypt_prepare_symlink.description`:

Description
-----------

This function computes the size the symlink target will require on-disk,
stores it in \ ``disk_link``\ ->len, and validates it against \ ``max_len``\ .  An
encrypted symlink may be longer than the original.

Additionally, \ ``disk_link``\ ->name is set to \ ``target``\  if the symlink will be
unencrypted, but left NULL if the symlink will be encrypted.  For encrypted
symlinks, the filesystem must call \ :c:func:`fscrypt_encrypt_symlink`\  to create the
on-disk target later.  (The reason for the two-step process is that some
filesystems need to know the size of the symlink target before creating the
inode, e.g. to determine whether it will be a "fast" or "slow" symlink.)

.. _`fscrypt_prepare_symlink.return`:

Return
------

0 on success, -ENAMETOOLONG if the symlink target is too long,
-ENOKEY if the encryption key is missing, or another -errno code if a problem
occurred while setting up the encryption key.

.. _`fscrypt_encrypt_symlink`:

fscrypt_encrypt_symlink
=======================

.. c:function:: int fscrypt_encrypt_symlink(struct inode *inode, const char *target, unsigned int len, struct fscrypt_str *disk_link)

    encrypt the symlink target if needed

    :param struct inode \*inode:
        symlink inode

    :param const char \*target:
        plaintext symlink target

    :param unsigned int len:
        length of \ ``target``\  excluding null terminator

    :param struct fscrypt_str \*disk_link:
        (in/out) the on-disk symlink target being prepared

.. _`fscrypt_encrypt_symlink.description`:

Description
-----------

If the symlink target needs to be encrypted, then this function encrypts it
into \ ``disk_link``\ ->name.  \ :c:func:`fscrypt_prepare_symlink`\  must have been called
previously to compute \ ``disk_link``\ ->len.  If the filesystem did not allocate a
buffer for \ ``disk_link``\ ->name after calling \ :c:func:`fscrypt_prepare_link`\ , then one
will be \ :c:func:`kmalloc`\ 'ed and the filesystem will be responsible for freeing it.

.. _`fscrypt_encrypt_symlink.return`:

Return
------

0 on success, -errno on failure

.. This file was automatic generated / don't edit.

