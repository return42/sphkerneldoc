
.. _API-freeze-super:

============
freeze_super
============

*man freeze_super(9)*

*4.6.0-rc1*

lock the filesystem and force it into a consistent state


Synopsis
========

.. c:function:: int freeze_super( struct super_block * sb )

Arguments
=========

``sb``
    the super to lock


Description
===========

Syncs the super to make sure the filesystem is consistent and calls the fs's freeze_fs. Subsequent calls to this without first thawing the fs will return -EBUSY.

During this function, sb->s_writers.frozen goes through these values:


SB_UNFROZEN
===========

File system is normal, all writes progress as usual.


SB_FREEZE_WRITE
===============

The file system is in the process of being frozen. New writes should be blocked, though page faults are still allowed. We wait for all writes to complete and then proceed to the
next stage.


SB_FREEZE_PAGEFAULT
===================

Freezing continues. Now also page faults are blocked but internal fs threads can still modify the filesystem (although they should not dirty new pages or inodes), writeback can run
etc. After waiting for all running page faults we sync the filesystem which will clean all dirty pages and inodes (no new dirty pages or inodes can be created when sync is
running).


SB_FREEZE_FS
============

The file system is frozen. Now all internal sources of fs modification are blocked (e.g. XFS preallocation truncation on inode reclaim). This is usually implemented by blocking new
transactions for filesystems that have them and need this additional guard. After all internal writers are finished we call ->``freeze_fs`` to finish filesystem freezing. Then we
transition to SB_FREEZE_COMPLETE state. This state is mostly auxiliary for filesystems to verify they do not modify frozen fs.

sb->s_writers.frozen is protected by sb->s_umount.
