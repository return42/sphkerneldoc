.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/crypto/policy.c

.. _`fscrypt_has_permitted_context`:

fscrypt_has_permitted_context
=============================

.. c:function:: int fscrypt_has_permitted_context(struct inode *parent, struct inode *child)

    is a file's encryption policy permitted within its directory?

    :param parent:
        inode for parent directory
    :type parent: struct inode \*

    :param child:
        inode for file being looked up, opened, or linked into \ ``parent``\ 
    :type child: struct inode \*

.. _`fscrypt_has_permitted_context.description`:

Description
-----------

Filesystems must call this before permitting access to an inode in a
situation where the parent directory is encrypted (either before allowing
->lookup() to succeed, or for a regular file before allowing it to be opened)
and before any operation that involves linking an inode into an encrypted
directory, including link, rename, and cross rename.  It enforces the
constraint that within a given encrypted directory tree, all files use the
same encryption policy.  The pre-access check is needed to detect potentially
malicious offline violations of this constraint, while the link and rename
checks are needed to prevent online violations of this constraint.

.. _`fscrypt_has_permitted_context.return`:

Return
------

1 if permitted, 0 if forbidden.  If forbidden, the caller must fail
the filesystem operation with EPERM.

.. _`fscrypt_inherit_context`:

fscrypt_inherit_context
=======================

.. c:function:: int fscrypt_inherit_context(struct inode *parent, struct inode *child, void *fs_data, bool preload)

    Sets a child context from its parent

    :param parent:
        Parent inode from which the context is inherited.
    :type parent: struct inode \*

    :param child:
        Child inode that inherits the context from \ ``parent``\ .
    :type child: struct inode \*

    :param fs_data:
        private data given by FS.
    :type fs_data: void \*

    :param preload:
        preload child i_crypt_info if true
    :type preload: bool

.. _`fscrypt_inherit_context.return`:

Return
------

0 on success, -errno on failure

.. This file was automatic generated / don't edit.

