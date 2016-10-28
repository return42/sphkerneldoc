.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/backref.c

.. _`btrfs_check_shared`:

btrfs_check_shared
==================

.. c:function:: int btrfs_check_shared(struct btrfs_trans_handle *trans, struct btrfs_fs_info *fs_info, u64 root_objectid, u64 inum, u64 bytenr)

    tell us whether an extent is shared

    :param struct btrfs_trans_handle \*trans:
        optional trans handle

    :param struct btrfs_fs_info \*fs_info:
        *undescribed*

    :param u64 root_objectid:
        *undescribed*

    :param u64 inum:
        *undescribed*

    :param u64 bytenr:
        *undescribed*

.. _`btrfs_check_shared.description`:

Description
-----------

btrfs_check_shared uses the backref walking code but will short
circuit as soon as it finds a root or inode that doesn't match the
one passed in. This provides a significant performance benefit for
callers (such as fiemap) which want to know whether the extent is
shared but do not need a ref count.

.. _`btrfs_check_shared.return`:

Return
------

0 if extent is not shared, 1 if it is shared, < 0 on error.

.. This file was automatic generated / don't edit.

