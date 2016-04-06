
.. _API-d-obtain-alias:

==============
d_obtain_alias
==============

*man d_obtain_alias(9)*

*4.6.0-rc1*

find or allocate a DISCONNECTED dentry for a given inode


Synopsis
========

.. c:function:: struct dentry ⋆ d_obtain_alias( struct inode * inode )

Arguments
=========

``inode``
    inode to allocate the dentry for


Description
===========

Obtain a dentry for an inode resulting from NFS filehandle conversion or similar open by handle operations. The returned dentry may be anonymous, or may have a full name (if the
inode was already in the cache).

When called on a directory inode, we must ensure that the inode only ever has one dentry. If a dentry is found, that is returned instead of allocating a new one.

On successful return, the reference to the inode has been transferred to the dentry. In case of an error the reference on the inode is released. To make it easier to use in export
operations a ``NULL`` or IS_ERR inode may be passed in and the error will be propagated to the return value, with a ``NULL`` ``inode`` replaced by ERR_PTR(-ESTALE).
