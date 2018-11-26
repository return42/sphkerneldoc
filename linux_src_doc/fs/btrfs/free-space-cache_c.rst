.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/free-space-cache.c

.. _`__btrfs_write_out_cache`:

\__btrfs_write_out_cache
========================

.. c:function:: int __btrfs_write_out_cache(struct btrfs_root *root, struct inode *inode, struct btrfs_free_space_ctl *ctl, struct btrfs_block_group_cache *block_group, struct btrfs_io_ctl *io_ctl, struct btrfs_trans_handle *trans)

    write out cached info to an inode \ ``root``\  - the root the inode belongs to \ ``ctl``\  - the free space cache we are going to write out \ ``block_group``\  - the block_group for this cache if it belongs to a block_group \ ``trans``\  - the trans handle

    :param root:
        *undescribed*
    :type root: struct btrfs_root \*

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param ctl:
        *undescribed*
    :type ctl: struct btrfs_free_space_ctl \*

    :param block_group:
        *undescribed*
    :type block_group: struct btrfs_block_group_cache \*

    :param io_ctl:
        *undescribed*
    :type io_ctl: struct btrfs_io_ctl \*

    :param trans:
        *undescribed*
    :type trans: struct btrfs_trans_handle \*

.. _`__btrfs_write_out_cache.description`:

Description
-----------

This function writes out a free space cache struct to disk for quick recovery
on mount.  This will return 0 if it was successful in writing the cache out,
or an errno if it was not.

.. This file was automatic generated / don't edit.

