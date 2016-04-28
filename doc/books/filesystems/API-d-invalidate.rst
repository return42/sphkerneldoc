.. -*- coding: utf-8; mode: rst -*-

.. _API-d-invalidate:

============
d_invalidate
============

*man d_invalidate(9)*

*4.6.0-rc5*

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

The final d_drop is done as an atomic operation relative to
rename_lock ensuring there are no races with d_set_mounted. This
ensures there are no unhashed dentries on the path to a mountpoint.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
