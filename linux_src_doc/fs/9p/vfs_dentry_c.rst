.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/vfs_dentry.c

.. _`v9fs_cached_dentry_delete`:

v9fs_cached_dentry_delete
=========================

.. c:function:: int v9fs_cached_dentry_delete(const struct dentry *dentry)

    called when dentry refcount equals 0

    :param const struct dentry \*dentry:
        dentry in question

.. _`v9fs_dentry_release`:

v9fs_dentry_release
===================

.. c:function:: void v9fs_dentry_release(struct dentry *dentry)

    called when dentry is going to be freed

    :param struct dentry \*dentry:
        dentry that is being release

.. This file was automatic generated / don't edit.

