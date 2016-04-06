
.. _API-debugfs-rename:

==============
debugfs_rename
==============

*man debugfs_rename(9)*

*4.6.0-rc1*

rename a file/directory in the debugfs filesystem


Synopsis
========

.. c:function:: struct dentry ⋆ debugfs_rename( struct dentry * old_dir, struct dentry * old_dentry, struct dentry * new_dir, const char * new_name )

Arguments
=========

``old_dir``
    a pointer to the parent dentry for the renamed object. This should be a directory dentry.

``old_dentry``
    dentry of an object to be renamed.

``new_dir``
    a pointer to the parent dentry where the object should be moved. This should be a directory dentry.

``new_name``
    a pointer to a string containing the target name.


Description
===========

This function renames a file/directory in debugfs. The target must not exist for rename to succeed.

This function will return a pointer to old_dentry (which is updated to reflect renaming) if it succeeds. If an error occurs, ``NULL`` will be returned.

If debugfs is not enabled in the kernel, the value -``ENODEV`` will be returned.
