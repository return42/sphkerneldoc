.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/compress.c

.. _`define_spinlock`:

DEFINE_SPINLOCK
===============

.. c:function::  DEFINE_SPINLOCK( ntfs_cb_lock)

    spinlock which protects ntfs_compression_buffer

    :param ntfs_cb_lock:
        *undescribed*
    :type ntfs_cb_lock: 

.. _`allocate_compression_buffers`:

allocate_compression_buffers
============================

.. c:function:: int allocate_compression_buffers( void)

    allocate the decompression buffers

    :param void:
        no arguments
    :type void: 

.. _`allocate_compression_buffers.description`:

Description
-----------

Caller has to hold the ntfs_lock mutex.

Return 0 on success or -ENOMEM if the allocations failed.

.. _`free_compression_buffers`:

free_compression_buffers
========================

.. c:function:: void free_compression_buffers( void)

    free the decompression buffers

    :param void:
        no arguments
    :type void: 

.. _`free_compression_buffers.description`:

Description
-----------

Caller has to hold the ntfs_lock mutex.

.. _`zero_partial_compressed_page`:

zero_partial_compressed_page
============================

.. c:function:: void zero_partial_compressed_page(struct page *page, const s64 initialized_size)

    zero out of bounds compressed page region

    :param page:
        *undescribed*
    :type page: struct page \*

    :param initialized_size:
        *undescribed*
    :type initialized_size: const s64

.. _`handle_bounds_compressed_page`:

handle_bounds_compressed_page
=============================

.. c:function:: void handle_bounds_compressed_page(struct page *page, const loff_t i_size, const s64 initialized_size)

    test for&handle out of bounds compressed page

    :param page:
        *undescribed*
    :type page: struct page \*

    :param i_size:
        *undescribed*
    :type i_size: const loff_t

    :param initialized_size:
        *undescribed*
    :type initialized_size: const s64

.. _`ntfs_decompress`:

ntfs_decompress
===============

.. c:function:: int ntfs_decompress(struct page  *dest_pages, int completed_pages, int *dest_index, int *dest_ofs, const int dest_max_index, const int dest_max_ofs, const int xpage, char *xpage_done, u8 *const cb_start, const u32 cb_size, const loff_t i_size, const s64 initialized_size)

    decompress a compression block into an array of pages

    :param dest_pages:
        destination array of pages
    :type dest_pages: struct page  \*

    :param completed_pages:
        scratch space to track completed pages
    :type completed_pages: int

    :param dest_index:
        current index into \ ``dest_pages``\  (IN/OUT)
    :type dest_index: int \*

    :param dest_ofs:
        current offset within \ ``dest_pages``\ [@dest_index] (IN/OUT)
    :type dest_ofs: int \*

    :param dest_max_index:
        maximum index into \ ``dest_pages``\  (IN)
    :type dest_max_index: const int

    :param dest_max_ofs:
        maximum offset within \ ``dest_pages``\ [@dest_max_index] (IN)
    :type dest_max_ofs: const int

    :param xpage:
        the target page (-1 if none) (IN)
    :type xpage: const int

    :param xpage_done:
        set to 1 if xpage was completed successfully (IN/OUT)
    :type xpage_done: char \*

    :param cb_start:
        compression block to decompress (IN)
    :type cb_start: u8 \*const

    :param cb_size:
        size of compression block \ ``cb_start``\  in bytes (IN)
    :type cb_size: const u32

    :param i_size:
        file size when we started the read (IN)
    :type i_size: const loff_t

    :param initialized_size:
        initialized file size when we started the read (IN)
    :type initialized_size: const s64

.. _`ntfs_decompress.description`:

Description
-----------

The caller must have disabled preemption. \ :c:func:`ntfs_decompress`\  reenables it when
the critical section is finished.

This decompresses the compression block \ ``cb_start``\  into the array of
destination pages \ ``dest_pages``\  starting at index \ ``dest_index``\  into \ ``dest_pages``\ 
and at offset \ ``dest_pos``\  into the page \ ``dest_pages``\ [@dest_index].

When the page \ ``dest_pages``\ [@xpage] is completed, \ ``xpage_done``\  is set to 1.
If xpage is -1 or \ ``xpage``\  has not been completed, \ ``xpage_done``\  is not modified.

\ ``cb_start``\  is a pointer to the compression block which needs decompressing
and \ ``cb_size``\  is the size of \ ``cb_start``\  in bytes (8-64kiB).

Return 0 if success or -EOVERFLOW on error in the compressed stream.
\ ``xpage_done``\  indicates whether the target page (@dest_pages[@xpage]) was
completed during the decompression of the compression block (@cb_start).

.. _`ntfs_decompress.warning`:

Warning
-------

This function \*REQUIRES\* PAGE_SIZE >= 4096 or it will blow up
unpredicatbly! You have been warned!

.. _`ntfs_decompress.note-to-hackers`:

Note to hackers
---------------

This function may not sleep until it has finished accessing
the compression block \ ``cb_start``\  as it is a per-CPU buffer.

.. _`ntfs_read_compressed_block`:

ntfs_read_compressed_block
==========================

.. c:function:: int ntfs_read_compressed_block(struct page *page)

    read a compressed block into the page cache

    :param page:
        locked page in the compression block(s) we need to read
    :type page: struct page \*

.. _`ntfs_read_compressed_block.description`:

Description
-----------

When we are called the page has already been verified to be locked and the
attribute is known to be non-resident, not encrypted, but compressed.

1. Determine which compression block(s) \ ``page``\  is in.
2. Get hold of all pages corresponding to this/these compression block(s).
3. Read the (first) compression block.
4. Decompress it into the corresponding pages.
5. Throw the compressed data away and proceed to 3. for the next compression
block or return success if no more compression blocks left.

.. _`ntfs_read_compressed_block.warning`:

Warning
-------

We have to be careful what we do about existing pages. They might
have been written to so that we would lose data if we were to just overwrite
them with the out-of-date uncompressed data.

.. _`ntfs_read_compressed_block.fixme`:

FIXME
-----

For PAGE_SIZE > cb_size we are not doing the Right Thing(TM) at
the end of the file I think. We need to detect this case and zero the out
of bounds remainder of the page in question and mark it as handled. At the
moment we would just return -EIO on such a page. This bug will only become
apparent if pages are above 8kiB and the NTFS volume only uses 512 byte
clusters so is probably not going to be seen by anyone. Still this should
be fixed. (AIA)

Again for PAGE_SIZE > cb_size we are screwing up both in
handling sparse and compressed cbs. (AIA)

At the moment we don't do any zeroing out in the case that
initialized_size is less than data_size. This should be safe because of the
nature of the compression algorithm used. Just in case we check and output
an error message in read inode if the two sizes are not equal for a
compressed file. (AIA)

.. This file was automatic generated / don't edit.

