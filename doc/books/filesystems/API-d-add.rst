
.. _API-d-add:

=====
d_add
=====

*man d_add(9)*

*4.6.0-rc1*

add dentry to hash queues


Synopsis
========

.. c:function:: void d_add( struct dentry * entry, struct inode * inode )

Arguments
=========

``entry``
    dentry to add

``inode``
    The inode to attach to this dentry


Description
===========

This adds the entry to the hash queues and initializes ``inode``. The entry was actually filled in earlier during ``d_alloc``.
