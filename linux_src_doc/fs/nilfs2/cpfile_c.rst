.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/cpfile.c

.. _`nilfs_cpfile_find_checkpoint_block`:

nilfs_cpfile_find_checkpoint_block
==================================

.. c:function:: int nilfs_cpfile_find_checkpoint_block(struct inode *cpfile, __u64 start_cno, __u64 end_cno, __u64 *cnop, struct buffer_head **bhp)

    find and get a buffer on cpfile

    :param struct inode \*cpfile:
        inode of cpfile

    :param __u64 start_cno:
        start checkpoint number (inclusive)

    :param __u64 end_cno:
        end checkpoint number (inclusive)

    :param __u64 \*cnop:
        place to store the next checkpoint number

    :param struct buffer_head \*\*bhp:
        place to store a pointer to buffer_head struct

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

    :param struct inode \*cpfile:
        inode of checkpoint file

    :param __u64 cno:
        checkpoint number

    :param int create:
        create flag

    :param struct nilfs_checkpoint \*\*cpp:
        pointer to a checkpoint

    :param struct buffer_head \*\*bhp:
        pointer to a buffer head

.. _`nilfs_cpfile_get_checkpoint.description`:

Description
-----------

nilfs_cpfile_get_checkpoint() acquires the checkpoint
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

    :param struct inode \*cpfile:
        inode of checkpoint file

    :param __u64 cno:
        checkpoint number

    :param struct buffer_head \*bh:
        buffer head

.. _`nilfs_cpfile_put_checkpoint.description`:

Description
-----------

nilfs_cpfile_put_checkpoint() releases the checkpoint
specified by \ ``cno``\ . \ ``bh``\  must be the buffer head which has been returned by
a previous call to \ :c:func:`nilfs_cpfile_get_checkpoint`\  with \ ``cno``\ .

.. _`nilfs_cpfile_delete_checkpoints`:

nilfs_cpfile_delete_checkpoints
===============================

.. c:function:: int nilfs_cpfile_delete_checkpoints(struct inode *cpfile, __u64 start, __u64 end)

    delete checkpoints

    :param struct inode \*cpfile:
        inode of checkpoint file

    :param __u64 start:
        start checkpoint number

    :param __u64 end:
        end checkpoint numer

.. _`nilfs_cpfile_delete_checkpoints.description`:

Description
-----------

nilfs_cpfile_delete_checkpoints() deletes the checkpoints in
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

    :param struct inode \*cpfile:
        *undescribed*

    :param __u64 \*cnop:
        *undescribed*

    :param int mode:
        *undescribed*

    :param void \*buf:
        *undescribed*

    :param unsigned int cisz:
        *undescribed*

    :param size_t nci:
        *undescribed*

.. _`nilfs_cpfile_delete_checkpoint`:

nilfs_cpfile_delete_checkpoint
==============================

.. c:function:: int nilfs_cpfile_delete_checkpoint(struct inode *cpfile, __u64 cno)

    :param struct inode \*cpfile:
        *undescribed*

    :param __u64 cno:
        *undescribed*

.. _`nilfs_cpfile_is_snapshot`:

nilfs_cpfile_is_snapshot
========================

.. c:function:: int nilfs_cpfile_is_snapshot(struct inode *cpfile, __u64 cno)

    :param struct inode \*cpfile:
        inode of checkpoint file

    :param __u64 cno:
        checkpoint number

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

    :param struct inode \*cpfile:
        inode of checkpoint file

    :param __u64 cno:
        checkpoint number

    :param int mode:
        *undescribed*

.. _`nilfs_cpfile_change_cpmode.description`:

Description
-----------

nilfs_change_cpmode() changes the mode of the checkpoint
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

    :param struct inode \*cpfile:
        inode of checkpoint file

    :param struct nilfs_cpstat \*cpstat:
        *undescribed*

.. _`nilfs_cpfile_get_stat.description`:

Description
-----------

nilfs_cpfile_get_stat() returns information about checkpoints.

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

    :param struct super_block \*sb:
        super block instance

    :param size_t cpsize:
        size of a checkpoint entry

    :param struct nilfs_inode \*raw_inode:
        on-disk cpfile inode

    :param struct inode \*\*inodep:
        buffer to store the inode

.. This file was automatic generated / don't edit.

