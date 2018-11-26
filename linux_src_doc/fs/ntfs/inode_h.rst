.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/inode.h

.. _`ntfs_i`:

NTFS_I
======

.. c:function:: ntfs_inode *NTFS_I(struct inode *inode)

    return the ntfs inode given a vfs inode

    :param inode:
        VFS inode
    :type inode: struct inode \*

.. _`ntfs_i.description`:

Description
-----------

\ :c:func:`NTFS_I`\  returns the ntfs inode associated with the VFS \ ``inode``\ .

.. _`ntfs_attr`:

typedef ntfs_attr
=================

.. c:type:: typedef ntfs_attr

    ntfs in memory attribute structure

.. _`ntfs_attr.description`:

Description
-----------

This structure exists only to provide a small structure for the
ntfs_{attr_}iget()/ntfs_test_inode()/ntfs_init_locked_inode() mechanism.

.. _`ntfs_attr.note`:

NOTE
----

Elements are ordered by size to make the structure as compact as
possible on all architectures.

.. This file was automatic generated / don't edit.

