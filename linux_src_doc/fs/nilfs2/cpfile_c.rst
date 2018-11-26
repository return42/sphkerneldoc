.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/cpfile.c

.. _`nilfs_cpfile_find_checkpoint_block`:

nilfs_cpfile_find_checkpoint_block
==================================

.. c:function:: int nilfs_cpfile_find_checkpoint_block(struct inode *cpfile, __u64 start_cno, __u64 end_cno, __u64 *cnop, struct buffer_head **bhp)

    find and get a buffer on cpfile

    :param cpfile:
        inode of cpfile
    :type cpfile: struct inode \*

    :param start_cno:
        start checkpoint number (inclusive)
    :type start_cno: __u64

    :param end_cno:
        end checkpoint number (inclusive)
    :type end_cno: __u64

    :param cnop:
        place to store the next checkpoint number
    :type cnop: __u64 \*

    :param bhp:
        place to store a pointer to buffer_head struct
    :type bhp: struct buffer_head \*\*

.. _`nilfs_cpfile_find_checkpoint_block.return-value`:

Return Value
------------

On success, it returns 0. On error, the following negative
error code is returned.

\ ``-ENOMEM``\  - Insufficient memory available.

\ ``-EIO``\  - I/O error

\ ``-ENOENT``\  - no block exists in the range.

.. _`nilfs_cpfile_get_checkpoint`:

nilfs_cpfile_get_checkpoint
===========================

.. c:function:: int nilfs_cpfile_get_checkpoint(struct inode *cpfile, __u64 cno, int create, struct nilfs_checkpoint **cpp, struct buffer_head **bhp)

    get a checkpoint

    :param cpfile:
        inode of checkpoint file
    :type cpfile: struct inode \*

    :param cno:
        checkpoint number
    :type cno: __u64

    :param create:
        create flag
    :type create: int

    :param cpp:
        pointer to a checkpoint
    :type cpp: struct nilfs_checkpoint \*\*

    :param bhp:
        pointer to a buffer head
    :type bhp: struct buffer_head \*\*

.. _`nilfs_cpfile_get_checkpoint.description`:

Description
-----------

\ :c:func:`nilfs_cpfile_get_checkpoint`\  acquires the checkpoint
specified by \ ``cno``\ . A new checkpoint will be created if \ ``cno``\  is the current
checkpoint number and \ ``create``\  is nonzero.

.. _`nilfs_cpfile_get_checkpoint.return-value`:

Return Value
------------

On success, 0 is returned, and the checkpoint and the
buffer head of the buffer on which the checkpoint is located are stored in
the place pointed by \ ``cpp``\  and \ ``bhp``\ , respectively. On error, one of the
following negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOENT``\  - No such checkpoint.

\ ``-EINVAL``\  - invalid checkpoint.

.. _`nilfs_cpfile_put_checkpoint`:

nilfs_cpfile_put_checkpoint
===========================

.. c:function:: void nilfs_cpfile_put_checkpoint(struct inode *cpfile, __u64 cno, struct buffer_head *bh)

    put a checkpoint

    :param cpfile:
        inode of checkpoint file
    :type cpfile: struct inode \*

    :param cno:
        checkpoint number
    :type cno: __u64

    :param bh:
        buffer head
    :type bh: struct buffer_head \*

.. _`nilfs_cpfile_put_checkpoint.description`:

Description
-----------

\ :c:func:`nilfs_cpfile_put_checkpoint`\  releases the checkpoint
specified by \ ``cno``\ . \ ``bh``\  must be the buffer head which has been returned by
a previous call to \ :c:func:`nilfs_cpfile_get_checkpoint`\  with \ ``cno``\ .

.. _`nilfs_cpfile_delete_checkpoints`:

nilfs_cpfile_delete_checkpoints
===============================

.. c:function:: int nilfs_cpfile_delete_checkpoints(struct inode *cpfile, __u64 start, __u64 end)

    delete checkpoints

    :param cpfile:
        inode of checkpoint file
    :type cpfile: struct inode \*

    :param start:
        start checkpoint number
    :type start: __u64

    :param end:
        end checkpoint numer
    :type end: __u64

.. _`nilfs_cpfile_delete_checkpoints.description`:

Description
-----------

\ :c:func:`nilfs_cpfile_delete_checkpoints`\  deletes the checkpoints in
the period from \ ``start``\  to \ ``end``\ , excluding \ ``end``\  itself. The checkpoints
which have been already deleted are ignored.

.. _`nilfs_cpfile_delete_checkpoints.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-EINVAL``\  - invalid checkpoints.

.. _`nilfs_cpfile_get_cpinfo`:

nilfs_cpfile_get_cpinfo
=======================

.. c:function:: ssize_t nilfs_cpfile_get_cpinfo(struct inode *cpfile, __u64 *cnop, int mode, void *buf, unsigned int cisz, size_t nci)

    :param cpfile:
        *undescribed*
    :type cpfile: struct inode \*

    :param cnop:
        *undescribed*
    :type cnop: __u64 \*

    :param mode:
        *undescribed*
    :type mode: int

    :param buf:
        *undescribed*
    :type buf: void \*

    :param cisz:
        *undescribed*
    :type cisz: unsigned int

    :param nci:
        *undescribed*
    :type nci: size_t

.. _`nilfs_cpfile_delete_checkpoint`:

nilfs_cpfile_delete_checkpoint
==============================

.. c:function:: int nilfs_cpfile_delete_checkpoint(struct inode *cpfile, __u64 cno)

    :param cpfile:
        *undescribed*
    :type cpfile: struct inode \*

    :param cno:
        *undescribed*
    :type cno: __u64

.. _`nilfs_cpfile_is_snapshot`:

nilfs_cpfile_is_snapshot
========================

.. c:function:: int nilfs_cpfile_is_snapshot(struct inode *cpfile, __u64 cno)

    :param cpfile:
        inode of checkpoint file
    :type cpfile: struct inode \*

    :param cno:
        checkpoint number
    :type cno: __u64

.. _`nilfs_cpfile_is_snapshot.return-value`:

Return Value
------------

On success, 1 is returned if the checkpoint specified by
\ ``cno``\  is a snapshot, or 0 if not. On error, one of the following negative
error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOENT``\  - No such checkpoint.

.. _`nilfs_cpfile_change_cpmode`:

nilfs_cpfile_change_cpmode
==========================

.. c:function:: int nilfs_cpfile_change_cpmode(struct inode *cpfile, __u64 cno, int mode)

    change checkpoint mode

    :param cpfile:
        inode of checkpoint file
    :type cpfile: struct inode \*

    :param cno:
        checkpoint number
    :type cno: __u64

    :param mode:
        *undescribed*
    :type mode: int

.. _`nilfs_cpfile_change_cpmode.description`:

Description
-----------

\ :c:func:`nilfs_change_cpmode`\  changes the mode of the checkpoint
specified by \ ``cno``\ . The mode \ ``mode``\  is NILFS_CHECKPOINT or NILFS_SNAPSHOT.

.. _`nilfs_cpfile_change_cpmode.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOENT``\  - No such checkpoint.

.. _`nilfs_cpfile_get_stat`:

nilfs_cpfile_get_stat
=====================

.. c:function:: int nilfs_cpfile_get_stat(struct inode *cpfile, struct nilfs_cpstat *cpstat)

    get checkpoint statistics

    :param cpfile:
        inode of checkpoint file
    :type cpfile: struct inode \*

    :param cpstat:
        *undescribed*
    :type cpstat: struct nilfs_cpstat \*

.. _`nilfs_cpfile_get_stat.description`:

Description
-----------

\ :c:func:`nilfs_cpfile_get_stat`\  returns information about checkpoints.

.. _`nilfs_cpfile_get_stat.return-value`:

Return Value
------------

On success, 0 is returned, and checkpoints information is
stored in the place pointed by \ ``stat``\ . On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

.. _`nilfs_cpfile_read`:

nilfs_cpfile_read
=================

.. c:function:: int nilfs_cpfile_read(struct super_block *sb, size_t cpsize, struct nilfs_inode *raw_inode, struct inode **inodep)

    read or get cpfile inode

    :param sb:
        super block instance
    :type sb: struct super_block \*

    :param cpsize:
        size of a checkpoint entry
    :type cpsize: size_t

    :param raw_inode:
        on-disk cpfile inode
    :type raw_inode: struct nilfs_inode \*

    :param inodep:
        buffer to store the inode
    :type inodep: struct inode \*\*

.. This file was automatic generated / don't edit.

