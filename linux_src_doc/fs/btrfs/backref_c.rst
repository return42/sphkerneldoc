.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/backref.c

.. _`btrfs_check_shared`:

btrfs_check_shared
==================

.. c:function:: int btrfs_check_shared(struct btrfs_root *root, u64 inum, u64 bytenr)

    tell us whether an extent is shared

    :param struct btrfs_root \*root:
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

This attempts to allocate a transaction in order to account for
delayed refs, but continues on even when the alloc fails.

.. _`btrfs_check_shared.return`:

Return
------

0 if extent is not shared, 1 if it is shared, < 0 on error.

.. This file was automatic generated / don't edit.

