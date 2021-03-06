.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ioctl.c

.. _`vfs_ioctl`:

vfs_ioctl
=========

.. c:function:: long vfs_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)

    call filesystem specific ioctl methods

    :param filp:
        open file to invoke ioctl method on
    :type filp: struct file \*

    :param cmd:
        ioctl command to execute
    :type cmd: unsigned int

    :param arg:
        command-specific argument for ioctl
    :type arg: unsigned long

.. _`vfs_ioctl.description`:

Description
-----------

Invokes filesystem specific ->unlocked_ioctl, if one exists; otherwise
returns -ENOTTY.

Returns 0 on success, -errno on error.

.. _`set_unknown_flags`:

SET_UNKNOWN_FLAGS
=================

.. c:function::  SET_UNKNOWN_FLAGS()

    Fiemap helper function

.. _`set_unknown_flags.description`:

Description
-----------

Called from file system ->fiemap callback. Will populate extent
info as passed in via arguments and copy to user memory. On
success, extent count on fieinfo is incremented.

Returns 0 on success, -errno on error, 1 if this was the last
extent that will fit in user array.

.. _`fiemap_check_flags`:

fiemap_check_flags
==================

.. c:function:: int fiemap_check_flags(struct fiemap_extent_info *fieinfo, u32 fs_flags)

    check validity of requested flags for fiemap

    :param fieinfo:
        Fiemap context passed into ->fiemap
    :type fieinfo: struct fiemap_extent_info \*

    :param fs_flags:
        Set of fiemap flags that the file system understands
    :type fs_flags: u32

.. _`fiemap_check_flags.description`:

Description
-----------

Called from file system ->fiemap callback. This will compute the
intersection of valid fiemap flags and those that the fs supports. That
value is then compared against the user supplied flags. In case of bad user
flags, the invalid values will be written into the fieinfo structure, and
-EBADR is returned, which tells \ :c:func:`ioctl_fiemap`\  to return those values to
userspace. For this reason, a return code of -EBADR should be preserved.

Returns 0 on success, -EBADR on bad flags.

.. _`__generic_block_fiemap`:

\__generic_block_fiemap
=======================

.. c:function:: int __generic_block_fiemap(struct inode *inode, struct fiemap_extent_info *fieinfo, loff_t start, loff_t len, get_block_t *get_block)

    FIEMAP for block based inodes (no locking)

    :param inode:
        the inode to map
    :type inode: struct inode \*

    :param fieinfo:
        the fiemap info struct that will be passed back to userspace
    :type fieinfo: struct fiemap_extent_info \*

    :param start:
        where to start mapping in the inode
    :type start: loff_t

    :param len:
        how much space to map
    :type len: loff_t

    :param get_block:
        the fs's get_block function
    :type get_block: get_block_t \*

.. _`__generic_block_fiemap.description`:

Description
-----------

This does FIEMAP for block based inodes.  Basically it will just loop
through get_block until we hit the number of extents we want to map, or we
go past the end of the file and hit a hole.

If it is possible to have data blocks beyond a hole past \ ``inode->i_size``\ , then
please do not use this function, it will stop at the first unmapped block
beyond i_size.

If you use this function directly, you need to do your own locking. Use
generic_block_fiemap if you want the locking done for you.

.. _`generic_block_fiemap`:

generic_block_fiemap
====================

.. c:function:: int generic_block_fiemap(struct inode *inode, struct fiemap_extent_info *fieinfo, u64 start, u64 len, get_block_t *get_block)

    FIEMAP for block based inodes

    :param inode:
        The inode to map
    :type inode: struct inode \*

    :param fieinfo:
        The mapping information
    :type fieinfo: struct fiemap_extent_info \*

    :param start:
        The initial block to map
    :type start: u64

    :param len:
        The length of the extect to attempt to map
    :type len: u64

    :param get_block:
        The block mapping function for the fs
    :type get_block: get_block_t \*

.. _`generic_block_fiemap.description`:

Description
-----------

Calls \__generic_block_fiemap to map the inode, after taking
the inode's mutex lock.

.. This file was automatic generated / don't edit.

