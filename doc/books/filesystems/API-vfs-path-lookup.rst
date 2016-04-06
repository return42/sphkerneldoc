
.. _API-vfs-path-lookup:

===============
vfs_path_lookup
===============

*man vfs_path_lookup(9)*

*4.6.0-rc1*

lookup a file path relative to a dentry-vfsmount pair


Synopsis
========

.. c:function:: int vfs_path_lookup( struct dentry * dentry, struct vfsmount * mnt, const char * name, unsigned int flags, struct path * path )

Arguments
=========

``dentry``
    pointer to dentry of the base directory

``mnt``
    pointer to vfs mount of the base directory

``name``
    pointer to file name

``flags``
    lookup flags

``path``
    pointer to struct path to fill
