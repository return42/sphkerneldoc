.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/super.c

.. _`ecryptfs_alloc_inode`:

ecryptfs_alloc_inode
====================

.. c:function:: struct inode *ecryptfs_alloc_inode(struct super_block *sb)

    allocate an ecryptfs inode

    :param struct super_block \*sb:
        Pointer to the ecryptfs super block

.. _`ecryptfs_alloc_inode.description`:

Description
-----------

Called to bring an inode into existence.

Only handle allocation, setting up structures should be done in
ecryptfs_read_inode. This is because the kernel, between now and
then, will 0 out the private data pointer.

Returns a pointer to a newly allocated inode, NULL otherwise

.. _`ecryptfs_destroy_inode`:

ecryptfs_destroy_inode
======================

.. c:function:: void ecryptfs_destroy_inode(struct inode *inode)

    :param struct inode \*inode:
        The ecryptfs inode

.. _`ecryptfs_destroy_inode.description`:

Description
-----------

This is used during the final destruction of the inode.  All
allocation of memory related to the inode, including allocated
memory in the crypt_stat struct, will be released here.
There should be no chance that this deallocation will be missed.

.. _`ecryptfs_statfs`:

ecryptfs_statfs
===============

.. c:function:: int ecryptfs_statfs(struct dentry *dentry, struct kstatfs *buf)

    :param struct dentry \*dentry:
        *undescribed*

    :param struct kstatfs \*buf:
        The struct kstatfs to fill in with stats

.. _`ecryptfs_statfs.description`:

Description
-----------

Get the filesystem statistics. Currently, we let this pass right through
to the lower filesystem and take no action ourselves.

.. _`ecryptfs_evict_inode`:

ecryptfs_evict_inode
====================

.. c:function:: void ecryptfs_evict_inode(struct inode *inode)

    @inode - The ecryptfs inode

    :param struct inode \*inode:
        *undescribed*

.. _`ecryptfs_evict_inode.description`:

Description
-----------

Called by \ :c:func:`iput`\  when the inode reference count reached zero
and the inode is not hashed anywhere.  Used to clear anything
that needs to be, before the inode is completely destroyed and put
on the inode free list. We use this to drop out reference to the
lower inode.

.. _`ecryptfs_show_options`:

ecryptfs_show_options
=====================

.. c:function:: int ecryptfs_show_options(struct seq_file *m, struct dentry *root)

    :param struct seq_file \*m:
        *undescribed*

    :param struct dentry \*root:
        *undescribed*

.. _`ecryptfs_show_options.description`:

Description
-----------

Prints the mount options for a given superblock.
Returns zero; does not fail.

.. This file was automatic generated / don't edit.

