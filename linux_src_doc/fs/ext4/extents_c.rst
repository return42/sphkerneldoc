.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/extents.c

.. _`ext4_swap_extents`:

ext4_swap_extents
=================

.. c:function:: int ext4_swap_extents(handle_t *handle, struct inode *inode1, struct inode *inode2, ext4_lblk_t lblk1, ext4_lblk_t lblk2, ext4_lblk_t count, int unwritten, int *erp)

    Swap extents between two inodes

    :param handle:
        *undescribed*
    :type handle: handle_t \*

    :param inode1:
        First inode
    :type inode1: struct inode \*

    :param inode2:
        Second inode
    :type inode2: struct inode \*

    :param lblk1:
        Start block for first inode
    :type lblk1: ext4_lblk_t

    :param lblk2:
        Start block for second inode
    :type lblk2: ext4_lblk_t

    :param count:
        Number of blocks to swap
    :type count: ext4_lblk_t

    :param unwritten:
        Mark second inode's extents as unwritten after swap
    :type unwritten: int

    :param erp:
        Pointer to save error value
    :type erp: int \*

.. _`ext4_swap_extents.description`:

Description
-----------

This helper routine does exactly what is promise "swap extents". All other
stuff such as page-cache locking consistency, bh mapping consistency or
extent's data copying must be performed by caller.

.. _`ext4_swap_extents.locking`:

Locking
-------

i_mutex is held for both inodes
i_data_sem is locked for write for both inodes

.. _`ext4_swap_extents.assumptions`:

Assumptions
-----------

All pages from requested range are locked for both inodes

.. This file was automatic generated / don't edit.

