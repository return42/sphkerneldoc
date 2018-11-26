.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/extent_io.c

.. _`convert_extent_bit`:

convert_extent_bit
==================

.. c:function:: int convert_extent_bit(struct extent_io_tree *tree, u64 start, u64 end, unsigned bits, unsigned clear_bits, struct extent_state **cached_state)

    convert all bits in a given range from one bit to another

    :param tree:
        the io tree to search
    :type tree: struct extent_io_tree \*

    :param start:
        the start offset in bytes
    :type start: u64

    :param end:
        the end offset in bytes (inclusive)
    :type end: u64

    :param bits:
        the bits to set in this range
    :type bits: unsigned

    :param clear_bits:
        the bits to clear in this range
    :type clear_bits: unsigned

    :param cached_state:
        state that we're going to cache
    :type cached_state: struct extent_state \*\*

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

.. c:function:: int extent_write_cache_pages(struct address_space *mapping, struct writeback_control *wbc, struct extent_page_data *epd)

    walk the list of dirty pages of the given address space and write all of them.

    :param mapping:
        address space structure to write
    :type mapping: struct address_space \*

    :param wbc:
        subtract the number of written pages from \*@wbc->nr_to_write
    :type wbc: struct writeback_control \*

    :param epd:
        *undescribed*
    :type epd: struct extent_page_data \*

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

    :param eb:
        the extent buffer
    :type eb: struct extent_buffer \*

    :param start:
        offset of the bitmap item in the extent buffer
    :type start: unsigned long

    :param nr:
        bit number to test
    :type nr: unsigned long

.. _`extent_buffer_bitmap_set`:

extent_buffer_bitmap_set
========================

.. c:function:: void extent_buffer_bitmap_set(struct extent_buffer *eb, unsigned long start, unsigned long pos, unsigned long len)

    set an area of a bitmap

    :param eb:
        the extent buffer
    :type eb: struct extent_buffer \*

    :param start:
        offset of the bitmap item in the extent buffer
    :type start: unsigned long

    :param pos:
        bit number of the first bit
    :type pos: unsigned long

    :param len:
        number of bits to set
    :type len: unsigned long

.. _`extent_buffer_bitmap_clear`:

extent_buffer_bitmap_clear
==========================

.. c:function:: void extent_buffer_bitmap_clear(struct extent_buffer *eb, unsigned long start, unsigned long pos, unsigned long len)

    clear an area of a bitmap

    :param eb:
        the extent buffer
    :type eb: struct extent_buffer \*

    :param start:
        offset of the bitmap item in the extent buffer
    :type start: unsigned long

    :param pos:
        bit number of the first bit
    :type pos: unsigned long

    :param len:
        number of bits to clear
    :type len: unsigned long

.. This file was automatic generated / don't edit.

