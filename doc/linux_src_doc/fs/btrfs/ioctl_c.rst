.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/ioctl.c

.. _`btrfs_clone`:

btrfs_clone
===========

.. c:function:: int btrfs_clone(struct inode *src, struct inode *inode, const u64 off, const u64 olen, const u64 olen_aligned, const u64 destoff, int no_time_update)

    clone a range from inode file to another

    :param struct inode \*src:
        Inode to clone from

    :param struct inode \*inode:
        Inode to clone to

    :param const u64 off:
        Offset within source to start clone from

    :param const u64 olen:
        Original length, passed by user, of range to clone

    :param const u64 olen_aligned:
        Block-aligned value of olen

    :param const u64 destoff:
        Offset within \ ``inode``\  to start clone

    :param int no_time_update:
        Whether to update mtime/ctime on the target inode

.. This file was automatic generated / don't edit.

