.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/ioctl.c

.. _`nilfs_ioctl_wrap_copy`:

nilfs_ioctl_wrap_copy
=====================

.. c:function:: int nilfs_ioctl_wrap_copy(struct the_nilfs *nilfs, struct nilfs_argv *argv, int dir, ssize_t (*) dofunc (struct the_nilfs *, __u64 *, int, void *, size_t, size_t)

    wrapping function of get/set metadata info

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param struct nilfs_argv \*argv:
        vector of arguments from userspace

    :param int dir:
        set of direction flags

    :param (ssize_t (\*) dofunc (struct the_nilfs \*, __u64 \*, int, void \*, size_t, size_t):
        concrete function of get/set metadata info

.. _`nilfs_ioctl_wrap_copy.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_wrap_copy`\  gets/sets metadata info by means of
calling \ :c:func:`dofunc`\  function on the basis of \ ``argv``\  argument.

.. _`nilfs_ioctl_wrap_copy.return-value`:

Return Value
------------

On success, 0 is returned and requested metadata info
is copied into userspace. On error, one of the following
negative error codes is returned.

\ ``-EINVAL``\  - Invalid arguments from userspace.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-EFAULT``\  - Failure during execution of requested operation.

.. _`nilfs_ioctl_getflags`:

nilfs_ioctl_getflags
====================

.. c:function:: int nilfs_ioctl_getflags(struct inode *inode, void __user *argp)

    ioctl to support lsattr

    :param struct inode \*inode:
        *undescribed*

    :param void __user \*argp:
        *undescribed*

.. _`nilfs_ioctl_setflags`:

nilfs_ioctl_setflags
====================

.. c:function:: int nilfs_ioctl_setflags(struct inode *inode, struct file *filp, void __user *argp)

    ioctl to support chattr

    :param struct inode \*inode:
        *undescribed*

    :param struct file \*filp:
        *undescribed*

    :param void __user \*argp:
        *undescribed*

.. _`nilfs_ioctl_getversion`:

nilfs_ioctl_getversion
======================

.. c:function:: int nilfs_ioctl_getversion(struct inode *inode, void __user *argp)

    get info about a file's version (generation number)

    :param struct inode \*inode:
        *undescribed*

    :param void __user \*argp:
        *undescribed*

.. _`nilfs_ioctl_change_cpmode`:

nilfs_ioctl_change_cpmode
=========================

.. c:function:: int nilfs_ioctl_change_cpmode(struct inode *inode, struct file *filp, unsigned int cmd, void __user *argp)

    change checkpoint mode (checkpoint/snapshot)

    :param struct inode \*inode:
        inode object

    :param struct file \*filp:
        file object

    :param unsigned int cmd:
        ioctl's request code

    :param void __user \*argp:
        pointer on argument from userspace

.. _`nilfs_ioctl_change_cpmode.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_change_cpmode`\  function changes mode of
given checkpoint between checkpoint and snapshot state. This ioctl
is used in chcp and mkcp utilities.

.. _`nilfs_ioctl_change_cpmode.return-value`:

Return Value
------------

On success, 0 is returned and mode of a checkpoint is
changed. On error, one of the following negative error codes
is returned.

\ ``-EPERM``\  - Operation not permitted.

\ ``-EFAULT``\  - Failure during checkpoint mode changing.

.. _`nilfs_ioctl_delete_checkpoint`:

nilfs_ioctl_delete_checkpoint
=============================

.. c:function:: int nilfs_ioctl_delete_checkpoint(struct inode *inode, struct file *filp, unsigned int cmd, void __user *argp)

    remove checkpoint

    :param struct inode \*inode:
        inode object

    :param struct file \*filp:
        file object

    :param unsigned int cmd:
        ioctl's request code

    :param void __user \*argp:
        pointer on argument from userspace

.. _`nilfs_ioctl_delete_checkpoint.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_delete_checkpoint`\  function removes
checkpoint from NILFS2 file system. This ioctl is used in rmcp
utility.

.. _`nilfs_ioctl_delete_checkpoint.return-value`:

Return Value
------------

On success, 0 is returned and a checkpoint is
removed. On error, one of the following negative error codes
is returned.

\ ``-EPERM``\  - Operation not permitted.

\ ``-EFAULT``\  - Failure during checkpoint removing.

.. _`nilfs_ioctl_do_get_cpinfo`:

nilfs_ioctl_do_get_cpinfo
=========================

.. c:function:: ssize_t nilfs_ioctl_do_get_cpinfo(struct the_nilfs *nilfs, __u64 *posp, int flags, void *buf, size_t size, size_t nmembs)

    callback method getting info about checkpoints

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param __u64 \*posp:
        pointer on array of checkpoint's numbers

    :param int flags:
        checkpoint mode (checkpoint or snapshot)

    :param void \*buf:
        buffer for storing checkponts' info

    :param size_t size:
        size in bytes of one checkpoint info item in array

    :param size_t nmembs:
        number of checkpoints in array (numbers and infos)

.. _`nilfs_ioctl_do_get_cpinfo.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_do_get_cpinfo`\  function returns info about
requested checkpoints. The NILFS_IOCTL_GET_CPINFO ioctl is used in
lscp utility and by nilfs_cleanerd daemon.

.. _`nilfs_ioctl_do_get_cpinfo.return-value`:

Return value
------------

count of nilfs_cpinfo structures in output buffer.

.. _`nilfs_ioctl_get_cpstat`:

nilfs_ioctl_get_cpstat
======================

.. c:function:: int nilfs_ioctl_get_cpstat(struct inode *inode, struct file *filp, unsigned int cmd, void __user *argp)

    get checkpoints statistics

    :param struct inode \*inode:
        inode object

    :param struct file \*filp:
        file object

    :param unsigned int cmd:
        ioctl's request code

    :param void __user \*argp:
        pointer on argument from userspace

.. _`nilfs_ioctl_get_cpstat.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_get_cpstat`\  returns information about checkpoints.
The NILFS_IOCTL_GET_CPSTAT ioctl is used by lscp, rmcp utilities
and by nilfs_cleanerd daemon.

.. _`nilfs_ioctl_get_cpstat.return-value`:

Return Value
------------

On success, 0 is returned, and checkpoints information is
copied into userspace pointer \ ``argp``\ . On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-EFAULT``\  - Failure during getting checkpoints statistics.

.. _`nilfs_ioctl_do_get_suinfo`:

nilfs_ioctl_do_get_suinfo
=========================

.. c:function:: ssize_t nilfs_ioctl_do_get_suinfo(struct the_nilfs *nilfs, __u64 *posp, int flags, void *buf, size_t size, size_t nmembs)

    callback method getting segment usage info

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param __u64 \*posp:
        pointer on array of segment numbers

    :param int flags:
        \*not used\*

    :param void \*buf:
        buffer for storing suinfo array

    :param size_t size:
        size in bytes of one suinfo item in array

    :param size_t nmembs:
        count of segment numbers and suinfos in array

.. _`nilfs_ioctl_do_get_suinfo.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_do_get_suinfo`\  function returns segment usage
info about requested segments. The NILFS_IOCTL_GET_SUINFO ioctl is used
in lssu, nilfs_resize utilities and by nilfs_cleanerd daemon.

.. _`nilfs_ioctl_do_get_suinfo.return-value`:

Return value
------------

count of nilfs_suinfo structures in output buffer.

.. _`nilfs_ioctl_get_sustat`:

nilfs_ioctl_get_sustat
======================

.. c:function:: int nilfs_ioctl_get_sustat(struct inode *inode, struct file *filp, unsigned int cmd, void __user *argp)

    get segment usage statistics

    :param struct inode \*inode:
        inode object

    :param struct file \*filp:
        file object

    :param unsigned int cmd:
        ioctl's request code

    :param void __user \*argp:
        pointer on argument from userspace

.. _`nilfs_ioctl_get_sustat.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_get_sustat`\  returns segment usage statistics.
The NILFS_IOCTL_GET_SUSTAT ioctl is used in lssu, nilfs_resize utilities
and by nilfs_cleanerd daemon.

.. _`nilfs_ioctl_get_sustat.return-value`:

Return Value
------------

On success, 0 is returned, and segment usage information is
copied into userspace pointer \ ``argp``\ . On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-EFAULT``\  - Failure during getting segment usage statistics.

.. _`nilfs_ioctl_do_get_vinfo`:

nilfs_ioctl_do_get_vinfo
========================

.. c:function:: ssize_t nilfs_ioctl_do_get_vinfo(struct the_nilfs *nilfs, __u64 *posp, int flags, void *buf, size_t size, size_t nmembs)

    callback method getting virtual blocks info

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param __u64 \*posp:
        \*not used\*

    :param int flags:
        \*not used\*

    :param void \*buf:
        buffer for storing array of nilfs_vinfo structures

    :param size_t size:
        size in bytes of one vinfo item in array

    :param size_t nmembs:
        count of vinfos in array

.. _`nilfs_ioctl_do_get_vinfo.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_do_get_vinfo`\  function returns information
on virtual block addresses. The NILFS_IOCTL_GET_VINFO ioctl is used
by nilfs_cleanerd daemon.

.. _`nilfs_ioctl_do_get_vinfo.return-value`:

Return value
------------

count of nilfs_vinfo structures in output buffer.

.. _`nilfs_ioctl_do_get_bdescs`:

nilfs_ioctl_do_get_bdescs
=========================

.. c:function:: ssize_t nilfs_ioctl_do_get_bdescs(struct the_nilfs *nilfs, __u64 *posp, int flags, void *buf, size_t size, size_t nmembs)

    callback method getting disk block descriptors

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param __u64 \*posp:
        \*not used\*

    :param int flags:
        \*not used\*

    :param void \*buf:
        buffer for storing array of nilfs_bdesc structures

    :param size_t size:
        size in bytes of one bdesc item in array

    :param size_t nmembs:
        count of bdescs in array

.. _`nilfs_ioctl_do_get_bdescs.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_do_get_bdescs`\  function returns information
about descriptors of disk block numbers. The NILFS_IOCTL_GET_BDESCS ioctl
is used by nilfs_cleanerd daemon.

.. _`nilfs_ioctl_do_get_bdescs.return-value`:

Return value
------------

count of nilfs_bdescs structures in output buffer.

.. _`nilfs_ioctl_get_bdescs`:

nilfs_ioctl_get_bdescs
======================

.. c:function:: int nilfs_ioctl_get_bdescs(struct inode *inode, struct file *filp, unsigned int cmd, void __user *argp)

    get disk block descriptors

    :param struct inode \*inode:
        inode object

    :param struct file \*filp:
        file object

    :param unsigned int cmd:
        ioctl's request code

    :param void __user \*argp:
        pointer on argument from userspace

.. _`nilfs_ioctl_get_bdescs.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_do_get_bdescs`\  function returns information
about descriptors of disk block numbers. The NILFS_IOCTL_GET_BDESCS ioctl
is used by nilfs_cleanerd daemon.

.. _`nilfs_ioctl_get_bdescs.return-value`:

Return Value
------------

On success, 0 is returned, and disk block descriptors are
copied into userspace pointer \ ``argp``\ . On error, one of the following
negative error codes is returned.

\ ``-EINVAL``\  - Invalid arguments from userspace.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-EFAULT``\  - Failure during getting disk block descriptors.

.. _`nilfs_ioctl_move_inode_block`:

nilfs_ioctl_move_inode_block
============================

.. c:function:: int nilfs_ioctl_move_inode_block(struct inode *inode, struct nilfs_vdesc *vdesc, struct list_head *buffers)

    prepare data/node block for moving by GC

    :param struct inode \*inode:
        inode object

    :param struct nilfs_vdesc \*vdesc:
        descriptor of virtual block number

    :param struct list_head \*buffers:
        list of moving buffers

.. _`nilfs_ioctl_move_inode_block.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_move_inode_block`\  function registers data/node
buffer in the GC pagecache and submit read request.

.. _`nilfs_ioctl_move_inode_block.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOENT``\  - Requested block doesn't exist.

\ ``-EEXIST``\  - Blocks conflict is detected.

.. _`nilfs_ioctl_move_blocks`:

nilfs_ioctl_move_blocks
=======================

.. c:function:: int nilfs_ioctl_move_blocks(struct super_block *sb, struct nilfs_argv *argv, void *buf)

    move valid inode's blocks during garbage collection

    :param struct super_block \*sb:
        superblock object

    :param struct nilfs_argv \*argv:
        vector of arguments from userspace

    :param void \*buf:
        array of nilfs_vdesc structures

.. _`nilfs_ioctl_move_blocks.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_move_blocks`\  function reads valid data/node
blocks that garbage collector specified with the array of nilfs_vdesc
structures and stores them into page caches of GC inodes.

.. _`nilfs_ioctl_move_blocks.return-value`:

Return Value
------------

Number of processed nilfs_vdesc structures or
error code, otherwise.

.. _`nilfs_ioctl_delete_checkpoints`:

nilfs_ioctl_delete_checkpoints
==============================

.. c:function:: int nilfs_ioctl_delete_checkpoints(struct the_nilfs *nilfs, struct nilfs_argv *argv, void *buf)

    delete checkpoints

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param struct nilfs_argv \*argv:
        vector of arguments from userspace

    :param void \*buf:
        array of periods of checkpoints numbers

.. _`nilfs_ioctl_delete_checkpoints.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_delete_checkpoints`\  function deletes checkpoints
in the period from p_start to p_end, excluding p_end itself. The checkpoints
which have been already deleted are ignored.

.. _`nilfs_ioctl_delete_checkpoints.return-value`:

Return Value
------------

Number of processed nilfs_period structures or
error code, otherwise.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-EINVAL``\  - invalid checkpoints.

.. _`nilfs_ioctl_free_vblocknrs`:

nilfs_ioctl_free_vblocknrs
==========================

.. c:function:: int nilfs_ioctl_free_vblocknrs(struct the_nilfs *nilfs, struct nilfs_argv *argv, void *buf)

    free virtual block numbers

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param struct nilfs_argv \*argv:
        vector of arguments from userspace

    :param void \*buf:
        array of virtual block numbers

.. _`nilfs_ioctl_free_vblocknrs.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_free_vblocknrs`\  function frees
the virtual block numbers specified by \ ``buf``\  and \ ``argv``\ ->v_nmembs.

.. _`nilfs_ioctl_free_vblocknrs.return-value`:

Return Value
------------

Number of processed virtual block numbers or
error code, otherwise.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOENT``\  - The virtual block number have not been allocated.

.. _`nilfs_ioctl_mark_blocks_dirty`:

nilfs_ioctl_mark_blocks_dirty
=============================

.. c:function:: int nilfs_ioctl_mark_blocks_dirty(struct the_nilfs *nilfs, struct nilfs_argv *argv, void *buf)

    mark blocks dirty

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param struct nilfs_argv \*argv:
        vector of arguments from userspace

    :param void \*buf:
        array of block descriptors

.. _`nilfs_ioctl_mark_blocks_dirty.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_mark_blocks_dirty`\  function marks
metadata file or data blocks as dirty.

.. _`nilfs_ioctl_mark_blocks_dirty.return-value`:

Return Value
------------

Number of processed block descriptors or
error code, otherwise.

\ ``-ENOMEM``\  - Insufficient memory available.

\ ``-EIO``\  - I/O error

\ ``-ENOENT``\  - the specified block does not exist (hole block)

.. _`nilfs_ioctl_clean_segments`:

nilfs_ioctl_clean_segments
==========================

.. c:function:: int nilfs_ioctl_clean_segments(struct inode *inode, struct file *filp, unsigned int cmd, void __user *argp)

    clean segments

    :param struct inode \*inode:
        inode object

    :param struct file \*filp:
        file object

    :param unsigned int cmd:
        ioctl's request code

    :param void __user \*argp:
        pointer on argument from userspace

.. _`nilfs_ioctl_clean_segments.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_clean_segments`\  function makes garbage
collection operation in the environment of requested parameters
from userspace. The NILFS_IOCTL_CLEAN_SEGMENTS ioctl is used by
nilfs_cleanerd daemon.

.. _`nilfs_ioctl_clean_segments.return-value`:

Return Value
------------

On success, 0 is returned or error code, otherwise.

.. _`nilfs_ioctl_sync`:

nilfs_ioctl_sync
================

.. c:function:: int nilfs_ioctl_sync(struct inode *inode, struct file *filp, unsigned int cmd, void __user *argp)

    make a checkpoint

    :param struct inode \*inode:
        inode object

    :param struct file \*filp:
        file object

    :param unsigned int cmd:
        ioctl's request code

    :param void __user \*argp:
        pointer on argument from userspace

.. _`nilfs_ioctl_sync.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_sync`\  function constructs a logical segment
for checkpointing.  This function guarantees that all modified data
and metadata are written out to the device when it successfully
returned.

.. _`nilfs_ioctl_sync.return-value`:

Return Value
------------

On success, 0 is retured. On errors, one of the following
negative error code is returned.

\ ``-EROFS``\  - Read only filesystem.

\ ``-EIO``\  - I/O error

\ ``-ENOSPC``\  - No space left on device (only in a panic state).

\ ``-ERESTARTSYS``\  - Interrupted.

\ ``-ENOMEM``\  - Insufficient memory available.

\ ``-EFAULT``\  - Failure during execution of requested operation.

.. _`nilfs_ioctl_resize`:

nilfs_ioctl_resize
==================

.. c:function:: int nilfs_ioctl_resize(struct inode *inode, struct file *filp, void __user *argp)

    resize NILFS2 volume

    :param struct inode \*inode:
        inode object

    :param struct file \*filp:
        file object

    :param void __user \*argp:
        pointer on argument from userspace

.. _`nilfs_ioctl_resize.return-value`:

Return Value
------------

On success, 0 is returned or error code, otherwise.

.. _`nilfs_ioctl_trim_fs`:

nilfs_ioctl_trim_fs
===================

.. c:function:: int nilfs_ioctl_trim_fs(struct inode *inode, void __user *argp)

    trim ioctl handle function

    :param struct inode \*inode:
        inode object

    :param void __user \*argp:
        pointer on argument from userspace

.. _`nilfs_ioctl_trim_fs.decription`:

Decription
----------

nilfs_ioctl_trim_fs is the FITRIM ioctl handle function. It
checks the arguments from userspace and calls nilfs_sufile_trim_fs, which
performs the actual trim operation.

.. _`nilfs_ioctl_trim_fs.return-value`:

Return Value
------------

On success, 0 is returned or negative error code, otherwise.

.. _`nilfs_ioctl_set_alloc_range`:

nilfs_ioctl_set_alloc_range
===========================

.. c:function:: int nilfs_ioctl_set_alloc_range(struct inode *inode, void __user *argp)

    limit range of segments to be allocated

    :param struct inode \*inode:
        inode object

    :param void __user \*argp:
        pointer on argument from userspace

.. _`nilfs_ioctl_set_alloc_range.decription`:

Decription
----------

\ :c:func:`nilfs_ioctl_set_alloc_range`\  function defines lower limit
of segments in bytes and upper limit of segments in bytes.
The NILFS_IOCTL_SET_ALLOC_RANGE is used by nilfs_resize utility.

.. _`nilfs_ioctl_set_alloc_range.return-value`:

Return Value
------------

On success, 0 is returned or error code, otherwise.

.. _`nilfs_ioctl_get_info`:

nilfs_ioctl_get_info
====================

.. c:function:: int nilfs_ioctl_get_info(struct inode *inode, struct file *filp, unsigned int cmd, void __user *argp, size_t membsz, ssize_t (*) dofunc (struct the_nilfs *, __u64 *, int, void *, size_t, size_t)

    wrapping function of get metadata info

    :param struct inode \*inode:
        inode object

    :param struct file \*filp:
        file object

    :param unsigned int cmd:
        ioctl's request code

    :param void __user \*argp:
        pointer on argument from userspace

    :param size_t membsz:
        size of an item in bytes

    :param (ssize_t (\*) dofunc (struct the_nilfs \*, __u64 \*, int, void \*, size_t, size_t):
        concrete function of getting metadata info

.. _`nilfs_ioctl_get_info.description`:

Description
-----------

\ :c:func:`nilfs_ioctl_get_info`\  gets metadata info by means of
calling \ :c:func:`dofunc`\  function.

.. _`nilfs_ioctl_get_info.return-value`:

Return Value
------------

On success, 0 is returned and requested metadata info
is copied into userspace. On error, one of the following
negative error codes is returned.

\ ``-EINVAL``\  - Invalid arguments from userspace.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-EFAULT``\  - Failure during execution of requested operation.

.. _`nilfs_ioctl_set_suinfo`:

nilfs_ioctl_set_suinfo
======================

.. c:function:: int nilfs_ioctl_set_suinfo(struct inode *inode, struct file *filp, unsigned int cmd, void __user *argp)

    set segment usage info

    :param struct inode \*inode:
        inode object

    :param struct file \*filp:
        file object

    :param unsigned int cmd:
        ioctl's request code

    :param void __user \*argp:
        pointer on argument from userspace

.. _`nilfs_ioctl_set_suinfo.description`:

Description
-----------

Expects an array of nilfs_suinfo_update structures
encapsulated in nilfs_argv and updates the segment usage info
according to the flags in nilfs_suinfo_update.

.. _`nilfs_ioctl_set_suinfo.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the
following negative error codes is returned.

\ ``-EPERM``\  - Not enough permissions

\ ``-EFAULT``\  - Error copying input data

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-EINVAL``\  - Invalid values in input (segment number, flags or nblocks)

.. This file was automatic generated / don't edit.

