.. -*- coding: utf-8; mode: rst -*-

.. _API---d-drop:

========
__d_drop
========

*man __d_drop(9)*

*4.6.0-rc5*

drop a dentry


Synopsis
========

.. c:function:: void __d_drop( struct dentry * dentry )

Arguments
=========

``dentry``
    dentry to drop


Description
===========

``d_drop`` unhashes the entry from the parent dentry hashes, so that it
won't be found through a VFS lookup any more. Note that this is
different from deleting the dentry - d_delete will try to mark the
dentry negative if possible, giving a successful _negative_ lookup,
while d_drop will just make the cache lookup fail.

``d_drop`` is used mainly for stuff that wants to invalidate a dentry
for some reason (NFS timeouts or autofs deletes).

__d_drop requires dentry->d_lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
