.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/unlink.c

.. _`nfs_free_unlinkdata`:

nfs_free_unlinkdata
===================

.. c:function:: void nfs_free_unlinkdata(struct nfs_unlinkdata *data)

    release data from a sillydelete operation.

    :param data:
        pointer to unlink structure.
    :type data: struct nfs_unlinkdata \*

.. _`nfs_async_unlink_done`:

nfs_async_unlink_done
=====================

.. c:function:: void nfs_async_unlink_done(struct rpc_task *task, void *calldata)

    Sillydelete post-processing

    :param task:
        rpc_task of the sillydelete
    :type task: struct rpc_task \*

    :param calldata:
        *undescribed*
    :type calldata: void \*

.. _`nfs_async_unlink_done.description`:

Description
-----------

Do the directory attribute update.

.. _`nfs_async_unlink_release`:

nfs_async_unlink_release
========================

.. c:function:: void nfs_async_unlink_release(void *calldata)

    Release the sillydelete data.

    :param calldata:
        *undescribed*
    :type calldata: void \*

.. _`nfs_async_unlink_release.description`:

Description
-----------

We need to call nfs_put_unlinkdata as a 'tk_release' task since the
rpc_task would be freed too.

.. _`nfs_async_unlink`:

nfs_async_unlink
================

.. c:function:: int nfs_async_unlink(struct dentry *dentry, const struct qstr *name)

    asynchronous unlinking of a file

    :param dentry:
        dentry to unlink
    :type dentry: struct dentry \*

    :param name:
        *undescribed*
    :type name: const struct qstr \*

.. _`nfs_complete_unlink`:

nfs_complete_unlink
===================

.. c:function:: void nfs_complete_unlink(struct dentry *dentry, struct inode *inode)

    Initialize completion of the sillydelete

    :param dentry:
        dentry to delete
    :type dentry: struct dentry \*

    :param inode:
        inode
    :type inode: struct inode \*

.. _`nfs_complete_unlink.description`:

Description
-----------

Since we're most likely to be called by \ :c:func:`dentry_iput`\ , we
only use the dentry to find the sillydelete. We then copy the name
into the qstr.

.. _`nfs_async_rename_done`:

nfs_async_rename_done
=====================

.. c:function:: void nfs_async_rename_done(struct rpc_task *task, void *calldata)

    Sillyrename post-processing

    :param task:
        rpc_task of the sillyrename
    :type task: struct rpc_task \*

    :param calldata:
        nfs_renamedata for the sillyrename
    :type calldata: void \*

.. _`nfs_async_rename_done.description`:

Description
-----------

Do the directory attribute updates and the d_move

.. _`nfs_async_rename_release`:

nfs_async_rename_release
========================

.. c:function:: void nfs_async_rename_release(void *calldata)

    Release the sillyrename data.

    :param calldata:
        the struct nfs_renamedata to be released
    :type calldata: void \*

.. _`nfs_async_rename`:

nfs_async_rename
================

.. c:function:: struct rpc_task *nfs_async_rename(struct inode *old_dir, struct inode *new_dir, struct dentry *old_dentry, struct dentry *new_dentry, void (*complete)(struct rpc_task *, struct nfs_renamedata *))

    perform an asynchronous rename operation

    :param old_dir:
        directory that currently holds the dentry to be renamed
    :type old_dir: struct inode \*

    :param new_dir:
        target directory for the rename
    :type new_dir: struct inode \*

    :param old_dentry:
        original dentry to be renamed
    :type old_dentry: struct dentry \*

    :param new_dentry:
        dentry to which the old_dentry should be renamed
    :type new_dentry: struct dentry \*

    :param void (\*complete)(struct rpc_task \*, struct nfs_renamedata \*):
        *undescribed*

.. _`nfs_async_rename.description`:

Description
-----------

It's expected that valid references to the dentries and inodes are held

.. _`nfs_sillyrename`:

nfs_sillyrename
===============

.. c:function:: int nfs_sillyrename(struct inode *dir, struct dentry *dentry)

    Perform a silly-rename of a dentry

    :param dir:
        inode of directory that contains dentry
    :type dir: struct inode \*

    :param dentry:
        dentry to be sillyrenamed
    :type dentry: struct dentry \*

.. _`nfs_sillyrename.description`:

Description
-----------

NFSv2/3 is stateless and the server doesn't know when the client is
holding a file open. To prevent application problems when a file is
unlinked while it's still open, the client performs a "silly-rename".
That is, it renames the file to a hidden file in the same directory,
and only performs the unlink once the last reference to it is put.

The final cleanup is done during dentry_iput.

(Note: NFSv4 is stateful, and has opens, so in theory an NFSv4 server
could take responsibility for keeping open files referenced.  The server
would also need to ensure that opened-but-deleted files were kept over
reboots.  However, we may not assume a server does so.  (RFC 5661
does provide an OPEN4_RESULT_PRESERVE_UNLINKED flag that a server can
use to advertise that it does this; some day we may take advantage of
it.))

.. This file was automatic generated / don't edit.

