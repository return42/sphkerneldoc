
.. _API-securityfs-remove:

=================
securityfs_remove
=================

*man securityfs_remove(9)*

*4.6.0-rc1*

removes a file or directory from the securityfs filesystem


Synopsis
========

.. c:function:: void securityfs_remove( struct dentry * dentry )

Arguments
=========

``dentry``
    a pointer to a the dentry of the file or directory to be removed.


Description
===========

This function removes a file or directory in securityfs that was previously created with a call to another securityfs function (like ``securityfs_create_file`` or variants
thereof.)

This function is required to be called in order for the file to be removed. No automatic cleanup of files will happen when a module is removed; you are responsible here.
