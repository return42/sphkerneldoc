.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/page.c

.. _`nilfs_forget_buffer`:

nilfs_forget_buffer
===================

.. c:function:: void nilfs_forget_buffer(struct buffer_head *bh)

    discard dirty state

    :param struct buffer_head \*bh:
        buffer head of the buffer to be discarded

.. _`nilfs_copy_buffer`:

nilfs_copy_buffer
=================

.. c:function:: void nilfs_copy_buffer(struct buffer_head *dbh, struct buffer_head *sbh)

    - copy buffer data and flags

    :param struct buffer_head \*dbh:
        destination buffer

    :param struct buffer_head \*sbh:
        source buffer

.. _`nilfs_page_buffers_clean`:

nilfs_page_buffers_clean
========================

.. c:function:: int nilfs_page_buffers_clean(struct page *page)

    check if a page has dirty buffers or not.

    :param struct page \*page:
        page to be checked

.. _`nilfs_page_buffers_clean.description`:

Description
-----------

nilfs_page_buffers_clean() returns zero if the page has dirty buffers.
Otherwise, it returns non-zero value.

.. _`nilfs_copy_page`:

nilfs_copy_page
===============

.. c:function:: void nilfs_copy_page(struct page *dst, struct page *src, int copy_dirty)

    - copy the page with buffers

    :param struct page \*dst:
        destination page

    :param struct page \*src:
        source page

    :param int copy_dirty:
        flag whether to copy dirty states on the page's buffer heads.

.. _`nilfs_copy_page.description`:

Description
-----------

This function is for both data pages and btnode pages.  The dirty flag
should be treated by caller.  The page must not be under i/o.
Both src and dst page must be locked

.. _`nilfs_copy_back_pages`:

nilfs_copy_back_pages
=====================

.. c:function:: void nilfs_copy_back_pages(struct address_space *dmap, struct address_space *smap)

    - copy back pages to original cache from shadow cache

    :param struct address_space \*dmap:
        destination page cache

    :param struct address_space \*smap:
        source page cache

.. _`nilfs_copy_back_pages.description`:

Description
-----------

No pages must no be added to the cache during this process.
This must be ensured by the caller.

.. _`nilfs_clear_dirty_pages`:

nilfs_clear_dirty_pages
=======================

.. c:function:: void nilfs_clear_dirty_pages(struct address_space *mapping, bool silent)

    discard dirty pages in address space

    :param struct address_space \*mapping:
        address space with dirty pages for discarding

    :param bool silent:
        suppress [true] or print [false] warning messages

.. _`nilfs_clear_dirty_page`:

nilfs_clear_dirty_page
======================

.. c:function:: void nilfs_clear_dirty_page(struct page *page, bool silent)

    discard dirty page

    :param struct page \*page:
        dirty page that will be discarded

    :param bool silent:
        suppress [true] or print [false] warning messages

.. _`nilfs_find_uncommitted_extent`:

nilfs_find_uncommitted_extent
=============================

.. c:function:: unsigned long nilfs_find_uncommitted_extent(struct inode *inode, sector_t start_blk, sector_t *blkoff)

    find extent of uncommitted data

    :param struct inode \*inode:
        inode

    :param sector_t start_blk:
        start block offset (in)

    :param sector_t \*blkoff:
        start offset of the found extent (out)

.. _`nilfs_find_uncommitted_extent.description`:

Description
-----------

This function searches an extent of buffers marked "delayed" which
starts from a block offset equal to or larger than \ ``start_blk``\ .  If
such an extent was found, this will store the start offset in
\ ``blkoff``\  and return its length in blocks.  Otherwise, zero is
returned.

.. This file was automatic generated / don't edit.

