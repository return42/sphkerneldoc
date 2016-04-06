
.. _API-d-invalidate:

============
d_invalidate
============

*man d_invalidate(9)*

*4.6.0-rc1*

detach submounts, prune dcache, and drop


Synopsis
========

.. c:function:: void d_invalidate( struct dentry * dentry )

Arguments
=========

``dentry``
    dentry to invalidate (aka detach, prune and drop)


Description
===========

no dcache lock.

The final d_drop is done as an atomic operation relative to rename_lock ensuring there are no races with d_set_mounted. This ensures there are no unhashed dentries on the path
to a mountpoint.
