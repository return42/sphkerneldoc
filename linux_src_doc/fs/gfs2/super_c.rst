.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/super.c

.. _`gfs2_mount_args`:

gfs2_mount_args
===============

.. c:function:: int gfs2_mount_args(struct gfs2_args *args, char *options)

    Parse mount options

    :param args:
        The structure into which the parsed options will be written
    :type args: struct gfs2_args \*

    :param options:
        The options to parse
    :type options: char \*

.. _`gfs2_mount_args.return`:

Return
------

errno

.. _`gfs2_jindex_free`:

gfs2_jindex_free
================

.. c:function:: void gfs2_jindex_free(struct gfs2_sbd *sdp)

    Clear all the journal index information

    :param sdp:
        The GFS2 superblock
    :type sdp: struct gfs2_sbd \*

.. _`gfs2_make_fs_rw`:

gfs2_make_fs_rw
===============

.. c:function:: int gfs2_make_fs_rw(struct gfs2_sbd *sdp)

    Turn a Read-Only FS into a Read-Write one

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

.. _`gfs2_make_fs_rw.return`:

Return
------

errno

.. _`gfs2_lock_fs_check_clean`:

gfs2_lock_fs_check_clean
========================

.. c:function:: int gfs2_lock_fs_check_clean(struct gfs2_sbd *sdp, struct gfs2_holder *freeze_gh)

    Stop all writes to the FS and check that all journals are clean

    :param sdp:
        the file system
    :type sdp: struct gfs2_sbd \*

    :param freeze_gh:
        *undescribed*
    :type freeze_gh: struct gfs2_holder \*

.. _`gfs2_lock_fs_check_clean.return`:

Return
------

errno

.. _`gfs2_write_inode`:

gfs2_write_inode
================

.. c:function:: int gfs2_write_inode(struct inode *inode, struct writeback_control *wbc)

    Make sure the inode is stable on the disk

    :param inode:
        The inode
    :type inode: struct inode \*

    :param wbc:
        The writeback control structure
    :type wbc: struct writeback_control \*

.. _`gfs2_write_inode.return`:

Return
------

errno

.. _`gfs2_dirty_inode`:

gfs2_dirty_inode
================

.. c:function:: void gfs2_dirty_inode(struct inode *inode, int flags)

    check for atime updates

    :param inode:
        The inode in question
    :type inode: struct inode \*

    :param flags:
        The type of dirty
    :type flags: int

.. _`gfs2_dirty_inode.description`:

Description
-----------

Unfortunately it can be called under any combination of inode
glock and transaction lock, so we have to check carefully.

At the moment this deals only with atime - it should be possible
to expand that role in future, once a review of the locking has
been carried out.

.. _`gfs2_make_fs_ro`:

gfs2_make_fs_ro
===============

.. c:function:: int gfs2_make_fs_ro(struct gfs2_sbd *sdp)

    Turn a Read-Write FS into a Read-Only one

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

.. _`gfs2_make_fs_ro.return`:

Return
------

errno

.. _`gfs2_put_super`:

gfs2_put_super
==============

.. c:function:: void gfs2_put_super(struct super_block *sb)

    Unmount the filesystem

    :param sb:
        The VFS superblock
    :type sb: struct super_block \*

.. _`gfs2_sync_fs`:

gfs2_sync_fs
============

.. c:function:: int gfs2_sync_fs(struct super_block *sb, int wait)

    sync the filesystem

    :param sb:
        the superblock
    :type sb: struct super_block \*

    :param wait:
        *undescribed*
    :type wait: int

.. _`gfs2_sync_fs.description`:

Description
-----------

Flushes the log to disk.

.. _`gfs2_freeze`:

gfs2_freeze
===========

.. c:function:: int gfs2_freeze(struct super_block *sb)

    prevent further writes to the filesystem

    :param sb:
        the VFS structure for the filesystem
    :type sb: struct super_block \*

.. _`gfs2_unfreeze`:

gfs2_unfreeze
=============

.. c:function:: int gfs2_unfreeze(struct super_block *sb)

    reallow writes to the filesystem

    :param sb:
        the VFS structure for the filesystem
    :type sb: struct super_block \*

.. _`statfs_slow_fill`:

statfs_slow_fill
================

.. c:function:: int statfs_slow_fill(struct gfs2_rgrpd *rgd, struct gfs2_statfs_change_host *sc)

    fill in the sg for a given RG

    :param rgd:
        the RG
    :type rgd: struct gfs2_rgrpd \*

    :param sc:
        the sc structure
    :type sc: struct gfs2_statfs_change_host \*

.. _`statfs_slow_fill.return`:

Return
------

0 on success, -ESTALE if the LVB is invalid

.. _`gfs2_statfs_slow`:

gfs2_statfs_slow
================

.. c:function:: int gfs2_statfs_slow(struct gfs2_sbd *sdp, struct gfs2_statfs_change_host *sc)

    Stat a filesystem using asynchronous locking

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

    :param sc:
        the sc info that will be returned
    :type sc: struct gfs2_statfs_change_host \*

.. _`gfs2_statfs_slow.description`:

Description
-----------

Any error (other than a signal) will cause this routine to fall back
to the synchronous version.

.. _`gfs2_statfs_slow.fixme`:

FIXME
-----

This really shouldn't busy wait like this.

.. _`gfs2_statfs_slow.return`:

Return
------

errno

.. _`gfs2_statfs_i`:

gfs2_statfs_i
=============

.. c:function:: int gfs2_statfs_i(struct gfs2_sbd *sdp, struct gfs2_statfs_change_host *sc)

    Do a statfs

    :param sdp:
        the filesystem
    :type sdp: struct gfs2_sbd \*

    :param sc:
        *undescribed*
    :type sc: struct gfs2_statfs_change_host \*

.. _`gfs2_statfs_i.return`:

Return
------

errno

.. _`gfs2_statfs`:

gfs2_statfs
===========

.. c:function:: int gfs2_statfs(struct dentry *dentry, struct kstatfs *buf)

    Gather and return stats about the filesystem

    :param dentry:
        *undescribed*
    :type dentry: struct dentry \*

    :param buf:
        *undescribed*
    :type buf: struct kstatfs \*

.. _`gfs2_statfs.return`:

Return
------

0 on success or error code

.. _`gfs2_remount_fs`:

gfs2_remount_fs
===============

.. c:function:: int gfs2_remount_fs(struct super_block *sb, int *flags, char *data)

    called when the FS is remounted

    :param sb:
        the filesystem
    :type sb: struct super_block \*

    :param flags:
        the remount flags
    :type flags: int \*

    :param data:
        extra data passed in (not used right now)
    :type data: char \*

.. _`gfs2_remount_fs.return`:

Return
------

errno

.. _`gfs2_drop_inode`:

gfs2_drop_inode
===============

.. c:function:: int gfs2_drop_inode(struct inode *inode)

    Drop an inode (test for remote unlink)

    :param inode:
        The inode to drop
    :type inode: struct inode \*

.. _`gfs2_drop_inode.description`:

Description
-----------

If we've received a callback on an iopen lock then it's because a
remote node tried to deallocate the inode but failed due to this node
still having the inode open. Here we mark the link count zero
since we know that it must have reached zero if the GLF_DEMOTE flag
is set on the iopen glock. If we didn't do a disk read since the
remote node removed the final link then we might otherwise miss
this event. This check ensures that this node will deallocate the
inode's blocks, or alternatively pass the baton on to another
node for later deallocation.

.. _`gfs2_show_options`:

gfs2_show_options
=================

.. c:function:: int gfs2_show_options(struct seq_file *s, struct dentry *root)

    Show mount options for /proc/mounts

    :param s:
        seq_file structure
    :type s: struct seq_file \*

    :param root:
        root of this (sub)tree
    :type root: struct dentry \*

.. _`gfs2_show_options.return`:

Return
------

0 on success or error code

.. _`gfs2_glock_put_eventually`:

gfs2_glock_put_eventually
=========================

.. c:function:: void gfs2_glock_put_eventually(struct gfs2_glock *gl)

    :param gl:
        The glock to put
    :type gl: struct gfs2_glock \*

.. _`gfs2_glock_put_eventually.description`:

Description
-----------

When under memory pressure, trigger a deferred glock put to make sure we
won't call into DLM and deadlock.  Otherwise, put the glock directly.

.. _`gfs2_evict_inode`:

gfs2_evict_inode
================

.. c:function:: void gfs2_evict_inode(struct inode *inode)

    Remove an inode from cache

    :param inode:
        The inode to evict
    :type inode: struct inode \*

.. _`gfs2_evict_inode.there-are-three-cases-to-consider`:

There are three cases to consider
---------------------------------

1. i_nlink == 0, we are final opener (and must deallocate)
2. i_nlink == 0, we are not the final opener (and cannot deallocate)
3. i_nlink > 0

If the fs is read only, then we have to treat all cases as per #3
since we are unable to do any deallocation. The inode will be
deallocated by the next read/write node to attempt an allocation
in the same resource group

We have to (at the moment) hold the inodes main lock to cover
the gap between unlocking the shared lock on the iopen lock and
taking the exclusive lock. I'd rather do a shared -> exclusive
conversion on the iopen lock, but we can change that later. This
is safe, just less efficient.

.. This file was automatic generated / don't edit.

