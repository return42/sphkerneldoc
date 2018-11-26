.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/move_extent.c

.. _`get_ext_path`:

get_ext_path
============

.. c:function:: int get_ext_path(struct inode *inode, ext4_lblk_t lblock, struct ext4_ext_path **ppath)

    Find an extent path for designated logical block number.

    :param inode:
        an inode which is searched
    :type inode: struct inode \*

    :param lblock:
        logical block number to find an extent path
    :type lblock: ext4_lblk_t

    :param ppath:
        *undescribed*
    :type ppath: struct ext4_ext_path \*\*

.. _`get_ext_path.description`:

Description
-----------

ext4_find_extent wrapper. Return 0 on success, or a negative error value
on failure.

.. _`ext4_double_down_write_data_sem`:

ext4_double_down_write_data_sem
===============================

.. c:function:: void ext4_double_down_write_data_sem(struct inode *first, struct inode *second)

    Acquire two inodes' write lock of i_data_sem

    :param first:
        *undescribed*
    :type first: struct inode \*

    :param second:
        *undescribed*
    :type second: struct inode \*

.. _`ext4_double_down_write_data_sem.description`:

Description
-----------

Acquire write lock of i_data_sem of the two inodes

.. _`ext4_double_up_write_data_sem`:

ext4_double_up_write_data_sem
=============================

.. c:function:: void ext4_double_up_write_data_sem(struct inode *orig_inode, struct inode *donor_inode)

    Release two inodes' write lock of i_data_sem

    :param orig_inode:
        original inode structure to be released its lock first
    :type orig_inode: struct inode \*

    :param donor_inode:
        donor inode structure to be released its lock second
        Release write lock of i_data_sem of two inodes (orig and donor).
    :type donor_inode: struct inode \*

.. _`mext_check_coverage`:

mext_check_coverage
===================

.. c:function:: int mext_check_coverage(struct inode *inode, ext4_lblk_t from, ext4_lblk_t count, int unwritten, int *err)

    Check that all extents in range has the same type

    :param inode:
        inode in question
    :type inode: struct inode \*

    :param from:
        block offset of inode
    :type from: ext4_lblk_t

    :param count:
        block count to be checked
    :type count: ext4_lblk_t

    :param unwritten:
        extents expected to be unwritten
    :type unwritten: int

    :param err:
        pointer to save error value
    :type err: int \*

.. _`mext_check_coverage.description`:

Description
-----------

Return 1 if all extents in range has expected type, and zero otherwise.

.. _`mext_page_double_lock`:

mext_page_double_lock
=====================

.. c:function:: int mext_page_double_lock(struct inode *inode1, struct inode *inode2, pgoff_t index1, pgoff_t index2, struct page  *page)

    Grab and lock pages on both \ ``inode1``\  and \ ``inode2``\ 

    :param inode1:
        the inode structure
    :type inode1: struct inode \*

    :param inode2:
        the inode structure
    :type inode2: struct inode \*

    :param index1:
        page index
    :type index1: pgoff_t

    :param index2:
        page index
    :type index2: pgoff_t

    :param page:
        result page vector
    :type page: struct page  \*

.. _`mext_page_double_lock.description`:

Description
-----------

Grab two locked pages for inode's by inode order

.. _`move_extent_per_page`:

move_extent_per_page
====================

.. c:function:: int move_extent_per_page(struct file *o_filp, struct inode *donor_inode, pgoff_t orig_page_offset, pgoff_t donor_page_offset, int data_offset_in_page, int block_len_in_page, int unwritten, int *err)

    Move extent data per page

    :param o_filp:
        file structure of original file
    :type o_filp: struct file \*

    :param donor_inode:
        donor inode
    :type donor_inode: struct inode \*

    :param orig_page_offset:
        page index on original file
    :type orig_page_offset: pgoff_t

    :param donor_page_offset:
        page index on donor file
    :type donor_page_offset: pgoff_t

    :param data_offset_in_page:
        block index where data swapping starts
    :type data_offset_in_page: int

    :param block_len_in_page:
        the number of blocks to be swapped
    :type block_len_in_page: int

    :param unwritten:
        orig extent is unwritten or not
    :type unwritten: int

    :param err:
        pointer to save return value
    :type err: int \*

.. _`move_extent_per_page.description`:

Description
-----------

Save the data in original inode blocks and replace original inode extents
with donor inode extents by calling \ :c:func:`ext4_swap_extents`\ .
Finally, write out the saved data in new original inode blocks. Return
replaced block count.

.. _`mext_check_arguments`:

mext_check_arguments
====================

.. c:function:: int mext_check_arguments(struct inode *orig_inode, struct inode *donor_inode, __u64 orig_start, __u64 donor_start, __u64 *len)

    Check whether move extent can be done

    :param orig_inode:
        original inode
    :type orig_inode: struct inode \*

    :param donor_inode:
        donor inode
    :type donor_inode: struct inode \*

    :param orig_start:
        logical start offset in block for orig
    :type orig_start: __u64

    :param donor_start:
        logical start offset in block for donor
    :type donor_start: __u64

    :param len:
        the number of blocks to be moved
    :type len: __u64 \*

.. _`mext_check_arguments.description`:

Description
-----------

Check the arguments of \ :c:func:`ext4_move_extents`\  whether the files can be
exchanged with each other.
Return 0 on success, or a negative error value on failure.

.. _`ext4_move_extents`:

ext4_move_extents
=================

.. c:function:: int ext4_move_extents(struct file *o_filp, struct file *d_filp, __u64 orig_blk, __u64 donor_blk, __u64 len, __u64 *moved_len)

    Exchange the specified range of a file

    :param o_filp:
        file structure of the original file
    :type o_filp: struct file \*

    :param d_filp:
        file structure of the donor file
    :type d_filp: struct file \*

    :param orig_blk:
        start offset in block for orig
    :type orig_blk: __u64

    :param donor_blk:
        start offset in block for donor
    :type donor_blk: __u64

    :param len:
        the number of blocks to be moved
    :type len: __u64

    :param moved_len:
        moved block length
    :type moved_len: __u64 \*

.. _`ext4_move_extents.description`:

Description
-----------

This function returns 0 and moved block length is set in moved_len
if succeed, otherwise returns error value.

.. This file was automatic generated / don't edit.

