.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/ioctl.c

.. _`btrfs_clone`:

btrfs_clone
===========

.. c:function:: int btrfs_clone(struct inode *src, struct inode *inode, const u64 off, const u64 olen, const u64 olen_aligned, const u64 destoff, int no_time_update)

    clone a range from inode file to another

    :param src:
        Inode to clone from
    :type src: struct inode \*

    :param inode:
        Inode to clone to
    :type inode: struct inode \*

    :param off:
        Offset within source to start clone from
    :type off: const u64

    :param olen:
        Original length, passed by user, of range to clone
    :type olen: const u64

    :param olen_aligned:
        Block-aligned value of olen
    :type olen_aligned: const u64

    :param destoff:
        Offset within \ ``inode``\  to start clone
    :type destoff: const u64

    :param no_time_update:
        Whether to update mtime/ctime on the target inode
    :type no_time_update: int

.. This file was automatic generated / don't edit.

