.. -*- coding: utf-8; mode: rst -*-

.. _API-vfs-cancel-lock:

===============
vfs_cancel_lock
===============

*man vfs_cancel_lock(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
