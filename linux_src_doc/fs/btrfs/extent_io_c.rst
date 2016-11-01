.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/extent_io.c

.. _`convert_extent_bit`:

convert_extent_bit
==================

.. c:function:: int convert_extent_bit(struct extent_io_tree *tree, u64 start, u64 end, unsigned bits, unsigned clear_bits, struct extent_state **cached_state)

    convert all bits in a given range from one bit to another

    :param struct extent_io_tree \*tree:
        the io tree to search

    :param u64 start:
        the start offset in bytes

    :param u64 end:
        the end offset in bytes (inclusive)

    :param unsigned bits:
        the bits to set in this range

    :param unsigned clear_bits:
        the bits to clear in this range

    :param struct extent_state \*\*cached_state:
        state that we're going to cache

.. _`convert_extent_bit.description`:

Description
-----------

This will go through and set bits for the given range.  If any states exist
already in this range they are set with the given bit and cleared of the
clear_bits.  This is only meant to be used by things that are mergeable, ie
converting from say DELALLOC to DIRTY.  This is not meant to be used with
boundary bits like LOCK.

All allocations are done with GFP_NOFS.

.. _`extent_write_cache_pages`:

extent_write_cache_pages
========================

.. c:function:: int extent_write_cache_pages(struct extent_io_tree *tree, struct address_space *mapping, struct writeback_control *wbc, writepage_t writepage, void *data, void (*flush_fn)(void *))

    walk the list of dirty pages of the given address space and write all of them.

    :param struct extent_io_tree \*tree:
        *undescribed*

    :param struct address_space \*mapping:
        address space structure to write

    :param struct writeback_control \*wbc:
        subtract the number of written pages from \*@wbc->nr_to_write

    :param writepage_t writepage:
        function called for each page

    :param void \*data:
        data passed to writepage function

    :param void (\*flush_fn)(void \*):
        *undescribed*

.. _`extent_write_cache_pages.description`:

Description
-----------

If a page is already under I/O, \ :c:func:`write_cache_pages`\  skips it, even
if it's dirty.  This is desirable behaviour for memory-cleaning writeback,
but it is INCORRECT for data-integrity system calls such as \ :c:func:`fsync`\ .  \ :c:func:`fsync`\ 
and \ :c:func:`msync`\  need to guarantee that all the data which was dirty at the time
the call was made get new I/O started against them.  If wbc->sync_mode is
WB_SYNC_ALL then we were called for data integrity and we must wait for
existing IO to complete.

.. _`extent_buffer_test_bit`:

extent_buffer_test_bit
======================

.. c:function:: int extent_buffer_test_bit(struct extent_buffer *eb, unsigned long start, unsigned long nr)

    determine whether a bit in a bitmap item is set

    :param struct extent_buffer \*eb:
        the extent buffer

    :param unsigned long start:
        offset of the bitmap item in the extent buffer

    :param unsigned long nr:
        bit number to test

.. _`extent_buffer_bitmap_set`:

extent_buffer_bitmap_set
========================

.. c:function:: void extent_buffer_bitmap_set(struct extent_buffer *eb, unsigned long start, unsigned long pos, unsigned long len)

    set an area of a bitmap

    :param struct extent_buffer \*eb:
        the extent buffer

    :param unsigned long start:
        offset of the bitmap item in the extent buffer

    :param unsigned long pos:
        bit number of the first bit

    :param unsigned long len:
        number of bits to set

.. _`extent_buffer_bitmap_clear`:

extent_buffer_bitmap_clear
==========================

.. c:function:: void extent_buffer_bitmap_clear(struct extent_buffer *eb, unsigned long start, unsigned long pos, unsigned long len)

    clear an area of a bitmap

    :param struct extent_buffer \*eb:
        the extent buffer

    :param unsigned long start:
        offset of the bitmap item in the extent buffer

    :param unsigned long pos:
        bit number of the first bit

    :param unsigned long len:
        number of bits to clear

.. This file was automatic generated / don't edit.

