.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/move_extent.c

.. _`get_ext_path`:

get_ext_path
============

.. c:function:: int get_ext_path(struct inode *inode, ext4_lblk_t lblock, struct ext4_ext_path **ppath)

    Find an extent path for designated logical block number.

    :param struct inode \*inode:
        an inode which is searched

    :param ext4_lblk_t lblock:
        logical block number to find an extent path

    :param struct ext4_ext_path \*\*ppath:
        *undescribed*

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

    :param struct inode \*first:
        *undescribed*

    :param struct inode \*second:
        *undescribed*

.. _`ext4_double_down_write_data_sem.description`:

Description
-----------

Acquire write lock of i_data_sem of the two inodes

.. _`ext4_double_up_write_data_sem`:

ext4_double_up_write_data_sem
=============================

.. c:function:: void ext4_double_up_write_data_sem(struct inode *orig_inode, struct inode *donor_inode)

    Release two inodes' write lock of i_data_sem

    :param struct inode \*orig_inode:
        original inode structure to be released its lock first

    :param struct inode \*donor_inode:
        donor inode structure to be released its lock second
        Release write lock of i_data_sem of two inodes (orig and donor).

.. _`mext_check_coverage`:

mext_check_coverage
===================

.. c:function:: int mext_check_coverage(struct inode *inode, ext4_lblk_t from, ext4_lblk_t count, int unwritten, int *err)

    Check that all extents in range has the same type

    :param struct inode \*inode:
        inode in question

    :param ext4_lblk_t from:
        block offset of inode

    :param ext4_lblk_t count:
        block count to be checked

    :param int unwritten:
        extents expected to be unwritten

    :param int \*err:
        pointer to save error value

.. _`mext_check_coverage.description`:

Description
-----------

Return 1 if all extents in range has expected type, and zero otherwise.

.. _`mext_page_double_lock`:

mext_page_double_lock
=====================

.. c:function:: int mext_page_double_lock(struct inode *inode1, struct inode *inode2, pgoff_t index1, pgoff_t index2, struct page  *page[2])

    Grab and lock pages on both \ ``inode1``\  and \ ``inode2``\ 

    :param struct inode \*inode1:
        the inode structure

    :param struct inode \*inode2:
        the inode structure

    :param pgoff_t index1:
        page index

    :param pgoff_t index2:
        page index

    :param struct page  \*page:
        result page vector

.. _`mext_page_double_lock.description`:

Description
-----------

Grab two locked pages for inode's by inode order

.. _`move_extent_per_page`:

move_extent_per_page
====================

.. c:function:: int move_extent_per_page(struct file *o_filp, struct inode *donor_inode, pgoff_t orig_page_offset, pgoff_t donor_page_offset, int data_offset_in_page, int block_len_in_page, int unwritten, int *err)

    Move extent data per page

    :param struct file \*o_filp:
        file structure of original file

    :param struct inode \*donor_inode:
        donor inode

    :param pgoff_t orig_page_offset:
        page index on original file

    :param pgoff_t donor_page_offset:
        page index on donor file

    :param int data_offset_in_page:
        block index where data swapping starts

    :param int block_len_in_page:
        the number of blocks to be swapped

    :param int unwritten:
        orig extent is unwritten or not

    :param int \*err:
        pointer to save return value

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

    :param struct inode \*orig_inode:
        original inode

    :param struct inode \*donor_inode:
        donor inode

    :param __u64 orig_start:
        logical start offset in block for orig

    :param __u64 donor_start:
        logical start offset in block for donor

    :param __u64 \*len:
        the number of blocks to be moved

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

    :param struct file \*o_filp:
        file structure of the original file

    :param struct file \*d_filp:
        file structure of the donor file

    :param __u64 orig_blk:
        start offset in block for orig

    :param __u64 donor_blk:
        start offset in block for donor

    :param __u64 len:
        the number of blocks to be moved

    :param __u64 \*moved_len:
        moved block length

.. _`ext4_move_extents.description`:

Description
-----------

This function returns 0 and moved block length is set in moved_len
if succeed, otherwise returns error value.

.. This file was automatic generated / don't edit.

