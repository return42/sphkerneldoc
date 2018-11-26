.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ocfs2/refcounttree.c

.. _`ocfs2_vfs_reflink`:

ocfs2_vfs_reflink
=================

.. c:function:: int ocfs2_vfs_reflink(struct dentry *old_dentry, struct inode *dir, struct dentry *new_dentry, bool preserve)

    Create a reference-counted link

    :param old_dentry:
        source dentry + inode
    :type old_dentry: struct dentry \*

    :param dir:
        directory to create the target
    :type dir: struct inode \*

    :param new_dentry:
        target dentry
    :type new_dentry: struct dentry \*

    :param preserve:
        if true, preserve all file attributes
    :type preserve: bool

.. This file was automatic generated / don't edit.

