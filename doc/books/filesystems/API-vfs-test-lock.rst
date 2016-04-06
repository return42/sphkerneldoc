
.. _API-vfs-test-lock:

=============
vfs_test_lock
=============

*man vfs_test_lock(9)*

*4.6.0-rc1*

test file byte range lock


Synopsis
========

.. c:function:: int vfs_test_lock( struct file * filp, struct file_lock * fl )

Arguments
=========

``filp``
    The file to test lock for

``fl``
    The lock to test; also used to hold result


Description
===========

Returns -ERRNO on failure. Indicates presence of conflicting lock by setting conf->fl_type to something other than F_UNLCK.
