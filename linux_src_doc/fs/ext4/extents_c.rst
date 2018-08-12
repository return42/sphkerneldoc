.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/extents.c

.. _`ext4_find_delalloc_range`:

ext4_find_delalloc_range
========================

.. c:function:: int ext4_find_delalloc_range(struct inode *inode, ext4_lblk_t lblk_start, ext4_lblk_t lblk_end)

    find delayed allocated block in the given range.

    :param struct inode \*inode:
        *undescribed*

    :param ext4_lblk_t lblk_start:
        *undescribed*

    :param ext4_lblk_t lblk_end:
        *undescribed*

.. _`ext4_find_delalloc_range.description`:

Description
-----------

Return 1 if there is a delalloc block in the range, otherwise 0.

.. _`get_reserved_cluster_alloc`:

get_reserved_cluster_alloc
==========================

.. c:function:: unsigned int get_reserved_cluster_alloc(struct inode *inode, ext4_lblk_t lblk_start, unsigned int num_blks)

    are under delalloc and were reserved quota for. This function is called when we are writing out the blocks that were originally written with their allocation delayed, but then the space was allocated using \ :c:func:`fallocate`\  before the delayed allocation could be resolved.

    :param struct inode \*inode:
        *undescribed*

    :param ext4_lblk_t lblk_start:
        *undescribed*

    :param unsigned int num_blks:
        *undescribed*

.. _`get_reserved_cluster_alloc.the-cases-to-look-for-are`:

The cases to look for are
-------------------------

('=' indicated delayed allocated blocks
'-' indicates non-delayed allocated blocks)
(a) partial clusters towards beginning and/or end outside of allocated range
are not delalloc'ed.
Ex:
\|----c---=\|====c====\|====c====\|===-c----\|
\|++++++ allocated ++++++\|
==> 4 complete clusters in above example

(b) partial cluster (outside of allocated range) towards either end is
marked for delayed allocation. In this case, we will exclude that
cluster.
Ex:
\|----====c========\|========c========\|
\|++++++ allocated ++++++\|
==> 1 complete clusters in above example

Ex:
\|================c================\|
\|++++++ allocated ++++++\|
==> 0 complete clusters in above example

The ext4_da_update_reserve_space will be called only if we
determine here that there were some "entire" clusters that span
this 'allocated' range.
In the non-bigalloc case, this function will just end up returning num_blks
without ever calling ext4_find_delalloc_range.

.. _`ext4_swap_extents`:

ext4_swap_extents
=================

.. c:function:: int ext4_swap_extents(handle_t *handle, struct inode *inode1, struct inode *inode2, ext4_lblk_t lblk1, ext4_lblk_t lblk2, ext4_lblk_t count, int unwritten, int *erp)

    Swap extents between two inodes

    :param handle_t \*handle:
        *undescribed*

    :param struct inode \*inode1:
        First inode

    :param struct inode \*inode2:
        Second inode

    :param ext4_lblk_t lblk1:
        Start block for first inode

    :param ext4_lblk_t lblk2:
        Start block for second inode

    :param ext4_lblk_t count:
        Number of blocks to swap

    :param int unwritten:
        Mark second inode's extents as unwritten after swap

    :param int \*erp:
        Pointer to save error value

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

