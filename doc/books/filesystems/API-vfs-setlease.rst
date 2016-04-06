
.. _API-vfs-setlease:

============
vfs_setlease
============

*man vfs_setlease(9)*

*4.6.0-rc1*

sets a lease on an open file


Synopsis
========

.. c:function:: int vfs_setlease( struct file * filp, long arg, struct file_lock ** lease, void ** priv )

Arguments
=========

``filp``
    file pointer

``arg``
    type of lease to obtain

``lease``
    file_lock to use when adding a lease

``priv``
    private info for lm_setup when adding a lease (may be NULL if lm_setup doesn't require it)


Description
===========

Call this to establish a lease on the file. The “lease” argument is not used for F_UNLCK requests and may be NULL. For commands that set or alter an existing lease, the
(⋆lease)->fl_lmops->lm_break operation must be set; if not, this function will return -ENOLCK (and generate a scary-looking stack trace).

The “priv” pointer is passed directly to the lm_setup function as-is. It may be NULL if the lm_setup operation doesn't require it.
