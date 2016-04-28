.. -*- coding: utf-8; mode: rst -*-

.. _API-d-add:

=====
d_add
=====

*man d_add(9)*

*4.6.0-rc5*

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

This adds the entry to the hash queues and initializes ``inode``. The
entry was actually filled in earlier during ``d_alloc``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
