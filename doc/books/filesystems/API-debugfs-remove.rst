
.. _API-debugfs-remove:

==============
debugfs_remove
==============

*man debugfs_remove(9)*

*4.6.0-rc1*

removes a file or directory from the debugfs filesystem


Synopsis
========

.. c:function:: void debugfs_remove( struct dentry * dentry )

Arguments
=========

``dentry``
    a pointer to a the dentry of the file or directory to be removed. If this parameter is NULL or an error value, nothing will be done.


Description
===========

This function removes a file or directory in debugfs that was previously created with a call to another debugfs function (like ``debugfs_create_file`` or variants thereof.)

This function is required to be called in order for the file to be removed, no automatic cleanup of files will happen when a module is removed, you are responsible here.
