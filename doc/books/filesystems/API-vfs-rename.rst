.. -*- coding: utf-8; mode: rst -*-

.. _API-vfs-rename:

==========
vfs_rename
==========

*man vfs_rename(9)*

*4.6.0-rc5*

rename a filesystem object


Synopsis
========

.. c:function:: int vfs_rename( struct inode * old_dir, struct dentry * old_dentry, struct inode * new_dir, struct dentry * new_dentry, struct inode ** delegated_inode, unsigned int flags )

Arguments
=========

``old_dir``
    parent of source

``old_dentry``
    source

``new_dir``
    parent of destination

``new_dentry``
    destination

``delegated_inode``
    returns an inode needing a delegation break

``flags``
    rename flags


Description
===========

The caller must hold multiple mutexes--see ``lock_rename``).

If vfs_rename discovers a delegation in need of breaking at either the
source or destination, it will return -EWOULDBLOCK and return a
reference to the inode in delegated_inode. The caller should then break
the delegation and retry. Because breaking a delegation may take a long
time, the caller should drop all locks before doing so.

Alternatively, a caller may pass NULL for delegated_inode. This may be
appropriate for callers that expect the underlying filesystem not to be
NFS exported.

The worst of all namespace operations - renaming directory. “Perverted”
doesn't even start to describe it. Somebody in UCB had a heck of a
trip...


Problems
========

a) we can get into loop creation. b) race potential - two innocent
renames can create a loop together. That's where 4.4 screws up. Current
fix: serialization on sb->s_vfs_rename_mutex. We might be more
accurate, but that's another story. c) we have to lock _four_ objects
- parents and victim (if it exists), and source (if it is not a
directory). And that - after we got ->i_mutex on parents (until then we
don't know whether the target exists). Solution: try to be smart with
locking order for inodes. We rely on the fact that tree topology may
change only under ->s_vfs_rename_mutex _and_ that parent of the
object we move will be locked. Thus we can rank directories by the tree
(ancestors first) and rank all non-directories after them. That works
since everybody except rename does “lock parent, lookup, lock child” and
rename is under ->s_vfs_rename_mutex. HOWEVER, it relies on the
assumption that any object with ->``lookup`` has no more than 1 dentry.
If “hybrid” objects will ever appear, we'd better make sure that there's
no link(2) for them. d) conversion from fhandle to dentry may come in
the wrong moment - when we are removing the target. Solution: we will
have to grab ->i_mutex in the fhandle_to_dentry code. [FIXME -
current nfsfh.c relies on ->i_mutex on parents, which works but leads
to some truly excessive locking].


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
