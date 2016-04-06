
.. _API-unregister-filesystem:

=====================
unregister_filesystem
=====================

*man unregister_filesystem(9)*

*4.6.0-rc1*

unregister a file system


Synopsis
========

.. c:function:: int unregister_filesystem( struct file_system_type * fs )

Arguments
=========

``fs``
    filesystem to unregister


Description
===========

Remove a file system that was previously successfully registered with the kernel. An error is returned if the file system is not found. Zero is returned on a success.

Once this function has returned the ``struct file_system_type`` structure may be freed or reused.
