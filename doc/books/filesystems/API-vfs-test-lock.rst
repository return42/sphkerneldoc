.. -*- coding: utf-8; mode: rst -*-

.. _API-vfs-test-lock:

=============
vfs_test_lock
=============

*man vfs_test_lock(9)*

*4.6.0-rc5*

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

Returns -ERRNO on failure. Indicates presence of conflicting lock by
setting conf->fl_type to something other than F_UNLCK.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
