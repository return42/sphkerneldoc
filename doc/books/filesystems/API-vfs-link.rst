
.. _API-vfs-link:

========
vfs_link
========

*man vfs_link(9)*

*4.6.0-rc1*

create a new link


Synopsis
========

.. c:function:: int vfs_link( struct dentry * old_dentry, struct inode * dir, struct dentry * new_dentry, struct inode ** delegated_inode )

Arguments
=========

``old_dentry``
    object to be linked

``dir``
    new parent

``new_dentry``
    where to create the new link

``delegated_inode``
    returns inode needing a delegation break


Description
===========

The caller must hold dir->i_mutex

If vfs_link discovers a delegation on the to-be-linked file in need of breaking, it will return -EWOULDBLOCK and return a reference to the inode in delegated_inode. The caller
should then break the delegation and retry. Because breaking a delegation may take a long time, the caller should drop the i_mutex before doing so.

Alternatively, a caller may pass NULL for delegated_inode. This may be appropriate for callers that expect the underlying filesystem not to be NFS exported.
