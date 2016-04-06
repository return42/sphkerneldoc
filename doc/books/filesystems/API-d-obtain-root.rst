
.. _API-d-obtain-root:

=============
d_obtain_root
=============

*man d_obtain_root(9)*

*4.6.0-rc1*

find or allocate a dentry for a given inode


Synopsis
========

.. c:function:: struct dentry ⋆ d_obtain_root( struct inode * inode )

Arguments
=========

``inode``
    inode to allocate the dentry for


Description
===========

Obtain an IS_ROOT dentry for the root of a filesystem.

We must ensure that directory inodes only ever have one dentry. If a dentry is found, that is returned instead of allocating a new one.

On successful return, the reference to the inode has been transferred to the dentry. In case of an error the reference on the inode is released. A ``NULL`` or IS_ERR inode may be
passed in and will be the error will be propagate to the return value, with a ``NULL`` ``inode`` replaced by ERR_PTR(-ESTALE).
