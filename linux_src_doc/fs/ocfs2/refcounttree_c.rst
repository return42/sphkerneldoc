.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ocfs2/refcounttree.c

.. _`ocfs2_vfs_reflink`:

ocfs2_vfs_reflink
=================

.. c:function:: int ocfs2_vfs_reflink(struct dentry *old_dentry, struct inode *dir, struct dentry *new_dentry, bool preserve)

    Create a reference-counted link

    :param struct dentry \*old_dentry:
        source dentry + inode

    :param struct inode \*dir:
        directory to create the target

    :param struct dentry \*new_dentry:
        target dentry

    :param bool preserve:
        if true, preserve all file attributes

.. This file was automatic generated / don't edit.

