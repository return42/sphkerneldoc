.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/file.c

.. _`nfs_revalidate_file_size`:

nfs_revalidate_file_size
========================

.. c:function:: int nfs_revalidate_file_size(struct inode *inode, struct file *filp)

    Revalidate the file size \ ``inode``\  - pointer to inode struct \ ``file``\  - pointer to struct file

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*filp:
        *undescribed*

.. _`nfs_revalidate_file_size.description`:

Description
-----------

Revalidates the file length. This is basically a wrapper around
\ :c:func:`nfs_revalidate_inode`\  that takes into account the fact that we may
have cached writes (in which case we don't care about the server's
idea of what the file length is), or O_DIRECT (in which case we
shouldn't trust the cache).

.. This file was automatic generated / don't edit.

