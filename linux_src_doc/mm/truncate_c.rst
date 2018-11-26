.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/truncate.c

.. _`do_invalidatepage`:

do_invalidatepage
=================

.. c:function:: void do_invalidatepage(struct page *page, unsigned int offset, unsigned int length)

    invalidate part or all of a page

    :param page:
        the page which is affected
    :type page: struct page \*

    :param offset:
        start of the range to invalidate
    :type offset: unsigned int

    :param length:
        length of the range to invalidate
    :type length: unsigned int

.. _`do_invalidatepage.description`:

Description
-----------

\ :c:func:`do_invalidatepage`\  is called when all or part of the page has become
invalidated by a truncate operation.

\ :c:func:`do_invalidatepage`\  does not have to release all buffers, but it must
ensure that no dirty buffer is left outside \ ``offset``\  and that no I/O
is underway against any of the blocks which are outside the truncation
point.  Because the caller is about to free (and possibly reuse) those
blocks on-disk.

.. _`truncate_inode_pages_range`:

truncate_inode_pages_range
==========================

.. c:function:: void truncate_inode_pages_range(struct address_space *mapping, loff_t lstart, loff_t lend)

    truncate range of pages specified by start & end byte offsets

    :param mapping:
        mapping to truncate
    :type mapping: struct address_space \*

    :param lstart:
        offset from which to truncate
    :type lstart: loff_t

    :param lend:
        offset to which to truncate (inclusive)
    :type lend: loff_t

.. _`truncate_inode_pages_range.description`:

Description
-----------

Truncate the page cache, removing the pages that are between
specified offsets (and zeroing out partial pages
if lstart or lend + 1 is not page aligned).

Truncate takes two passes - the first pass is nonblocking.  It will not
block on page locks and it will not block on writeback.  The second pass
will wait.  This is to prevent as much IO as possible in the affected region.
The first pass will remove most pages, so the search cost of the second pass
is low.

We pass down the cache-hot hint to the page freeing code.  Even if the
mapping is large, it is probably the case that the final pages are the most
recently touched, and freeing happens in ascending file offset order.

Note that since ->invalidatepage() accepts range to invalidate
truncate_inode_pages_range is able to handle cases where lend + 1 is not
page aligned properly.

.. _`truncate_inode_pages`:

truncate_inode_pages
====================

.. c:function:: void truncate_inode_pages(struct address_space *mapping, loff_t lstart)

    truncate *all* the pages from an offset

    :param mapping:
        mapping to truncate
    :type mapping: struct address_space \*

    :param lstart:
        offset from which to truncate
    :type lstart: loff_t

.. _`truncate_inode_pages.description`:

Description
-----------

Called under (and serialised by) inode->i_mutex.

.. _`truncate_inode_pages.note`:

Note
----

When this function returns, there can be a page in the process of
deletion (inside \ :c:func:`__delete_from_page_cache`\ ) in the specified range.  Thus
mapping->nrpages can be non-zero when this function returns even after
truncation of the whole mapping.

.. _`truncate_inode_pages_final`:

truncate_inode_pages_final
==========================

.. c:function:: void truncate_inode_pages_final(struct address_space *mapping)

    truncate *all* pages before inode dies

    :param mapping:
        mapping to truncate
    :type mapping: struct address_space \*

.. _`truncate_inode_pages_final.description`:

Description
-----------

Called under (and serialized by) inode->i_mutex.

Filesystems have to use this in the .evict_inode path to inform the
VM that this is the final truncate and the inode is going away.

.. _`invalidate_mapping_pages`:

invalidate_mapping_pages
========================

.. c:function:: unsigned long invalidate_mapping_pages(struct address_space *mapping, pgoff_t start, pgoff_t end)

    Invalidate all the unlocked pages of one inode

    :param mapping:
        the address_space which holds the pages to invalidate
    :type mapping: struct address_space \*

    :param start:
        the offset 'from' which to invalidate
    :type start: pgoff_t

    :param end:
        the offset 'to' which to invalidate (inclusive)
    :type end: pgoff_t

.. _`invalidate_mapping_pages.description`:

Description
-----------

This function only removes the unlocked pages, if you want to
remove all the pages of one inode, you must call truncate_inode_pages.

\ :c:func:`invalidate_mapping_pages`\  will not block on IO activity. It will not
invalidate pages which are dirty, locked, under writeback or mapped into
pagetables.

.. _`invalidate_inode_pages2_range`:

invalidate_inode_pages2_range
=============================

.. c:function:: int invalidate_inode_pages2_range(struct address_space *mapping, pgoff_t start, pgoff_t end)

    remove range of pages from an address_space

    :param mapping:
        the address_space
    :type mapping: struct address_space \*

    :param start:
        the page offset 'from' which to invalidate
    :type start: pgoff_t

    :param end:
        the page offset 'to' which to invalidate (inclusive)
    :type end: pgoff_t

.. _`invalidate_inode_pages2_range.description`:

Description
-----------

Any pages which are found to be mapped into pagetables are unmapped prior to
invalidation.

Returns -EBUSY if any pages could not be invalidated.

.. _`invalidate_inode_pages2`:

invalidate_inode_pages2
=======================

.. c:function:: int invalidate_inode_pages2(struct address_space *mapping)

    remove all pages from an address_space

    :param mapping:
        the address_space
    :type mapping: struct address_space \*

.. _`invalidate_inode_pages2.description`:

Description
-----------

Any pages which are found to be mapped into pagetables are unmapped prior to
invalidation.

Returns -EBUSY if any pages could not be invalidated.

.. _`truncate_pagecache`:

truncate_pagecache
==================

.. c:function:: void truncate_pagecache(struct inode *inode, loff_t newsize)

    unmap and remove pagecache that has been truncated

    :param inode:
        inode
    :type inode: struct inode \*

    :param newsize:
        new file size
    :type newsize: loff_t

.. _`truncate_pagecache.description`:

Description
-----------

inode's new i_size must already be written before truncate_pagecache
is called.

This function should typically be called before the filesystem
releases resources associated with the freed range (eg. deallocates
blocks). This way, pagecache will always stay logically coherent
with on-disk format, and the filesystem would not have to deal with
situations such as writepage being called for a page that has already
had its underlying blocks deallocated.

.. _`truncate_setsize`:

truncate_setsize
================

.. c:function:: void truncate_setsize(struct inode *inode, loff_t newsize)

    update inode and pagecache for a new file size

    :param inode:
        inode
    :type inode: struct inode \*

    :param newsize:
        new file size
    :type newsize: loff_t

.. _`truncate_setsize.description`:

Description
-----------

truncate_setsize updates i_size and performs pagecache truncation (if
necessary) to \ ``newsize``\ . It will be typically be called from the filesystem's
setattr function when ATTR_SIZE is passed in.

Must be called with a lock serializing truncates and writes (generally
i_mutex but e.g. xfs uses a different lock) and before all filesystem
specific block truncation has been performed.

.. _`pagecache_isize_extended`:

pagecache_isize_extended
========================

.. c:function:: void pagecache_isize_extended(struct inode *inode, loff_t from, loff_t to)

    update pagecache after extension of i_size

    :param inode:
        inode for which i_size was extended
    :type inode: struct inode \*

    :param from:
        original inode size
    :type from: loff_t

    :param to:
        new inode size
    :type to: loff_t

.. _`pagecache_isize_extended.description`:

Description
-----------

Handle extension of inode size either caused by extending truncate or by
write starting after current i_size. We mark the page straddling current
i_size RO so that \ :c:func:`page_mkwrite`\  is called on the nearest write access to
the page.  This way filesystem can be sure that \ :c:func:`page_mkwrite`\  is called on
the page before user writes to the page via mmap after the i_size has been
changed.

The function must be called after i_size is updated so that page fault
coming after we unlock the page will already see the new i_size.
The function must be called while we still hold i_mutex - this not only
makes sure i_size is stable but also that userspace cannot observe new
i_size value before we are prepared to store mmap writes at new inode size.

.. _`truncate_pagecache_range`:

truncate_pagecache_range
========================

.. c:function:: void truncate_pagecache_range(struct inode *inode, loff_t lstart, loff_t lend)

    unmap and remove pagecache that is hole-punched

    :param inode:
        inode
    :type inode: struct inode \*

    :param lstart:
        offset of beginning of hole
    :type lstart: loff_t

    :param lend:
        offset of last byte of hole
    :type lend: loff_t

.. _`truncate_pagecache_range.description`:

Description
-----------

This function should typically be called before the filesystem
releases resources associated with the freed range (eg. deallocates
blocks). This way, pagecache will always stay logically coherent
with on-disk format, and the filesystem would not have to deal with
situations such as writepage being called for a page that has already
had its underlying blocks deallocated.

.. This file was automatic generated / don't edit.

