.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/attr.c

.. _`setattr_prepare`:

setattr_prepare
===============

.. c:function:: int setattr_prepare(struct dentry *dentry, struct iattr *attr)

    check if attribute changes to a dentry are allowed

    :param dentry:
        dentry to check
    :type dentry: struct dentry \*

    :param attr:
        attributes to change
    :type attr: struct iattr \*

.. _`setattr_prepare.description`:

Description
-----------

Check if we are allowed to change the attributes contained in \ ``attr``\ 
in the given dentry.  This includes the normal unix access permission
checks, as well as checks for rlimits and others. The function also clears
SGID bit from mode if user is not allowed to set it. Also file capabilities
and IMA extended attributes are cleared if ATTR_KILL_PRIV is set.

Should be called as the first thing in ->setattr implementations,
possibly after taking additional locks.

.. _`inode_newsize_ok`:

inode_newsize_ok
================

.. c:function:: int inode_newsize_ok(const struct inode *inode, loff_t offset)

    may this inode be truncated to a given size

    :param inode:
        the inode to be truncated
    :type inode: const struct inode \*

    :param offset:
        the new size to assign to the inode
    :type offset: loff_t

.. _`inode_newsize_ok.description`:

Description
-----------

inode_newsize_ok must be called with i_mutex held.

inode_newsize_ok will check filesystem limits and ulimits to check that the
new inode size is within limits. inode_newsize_ok will also send SIGXFSZ
when necessary. Caller must not proceed with inode size change if failure is
returned. \ ``inode``\  must be a file (not directory), with appropriate
permissions to allow truncate (inode_newsize_ok does NOT check these
conditions).

.. _`inode_newsize_ok.return`:

Return
------

0 on success, -ve errno on failure

.. _`setattr_copy`:

setattr_copy
============

.. c:function:: void setattr_copy(struct inode *inode, const struct iattr *attr)

    copy simple metadata updates into the generic inode

    :param inode:
        the inode to be updated
    :type inode: struct inode \*

    :param attr:
        the new attributes
    :type attr: const struct iattr \*

.. _`setattr_copy.description`:

Description
-----------

setattr_copy must be called with i_mutex held.

setattr_copy updates the inode's metadata with that specified
in attr. Noticeably missing is inode size update, which is more complex
as it requires pagecache updates.

The inode is not marked as dirty after this operation. The rationale is
that for "simple" filesystems, the struct inode is the inode storage.
The caller is free to mark the inode dirty afterwards if needed.

.. _`notify_change`:

notify_change
=============

.. c:function:: int notify_change(struct dentry *dentry, struct iattr *attr, struct inode **delegated_inode)

    modify attributes of a filesytem object

    :param dentry:
        object affected
    :type dentry: struct dentry \*

    :param attr:
        new attributes
    :type attr: struct iattr \*

    :param delegated_inode:
        returns inode, if the inode is delegated
    :type delegated_inode: struct inode \*\*

.. _`notify_change.description`:

Description
-----------

The caller must hold the i_mutex on the affected object.

If notify_change discovers a delegation in need of breaking,
it will return -EWOULDBLOCK and return a reference to the inode in
delegated_inode.  The caller should then break the delegation and
retry.  Because breaking a delegation may take a long time, the
caller should drop the i_mutex before doing so.

Alternatively, a caller may pass NULL for delegated_inode.  This may
be appropriate for callers that expect the underlying filesystem not
to be NFS exported.  Also, passing NULL is fine for callers holding
the file open for write, as there can be no conflicting delegation in
that case.

.. This file was automatic generated / don't edit.

