
.. _API-vfs-cancel-lock:

===============
vfs_cancel_lock
===============

*man vfs_cancel_lock(9)*

*4.6.0-rc1*

file byte range unblock lock


Synopsis
========

.. c:function:: int vfs_cancel_lock( struct file * filp, struct file_lock * fl )

Arguments
=========

``filp``
    The file to apply the unblock to

``fl``
    The lock to be unblocked


Description
===========

Used by lock managers to cancel blocked requests
