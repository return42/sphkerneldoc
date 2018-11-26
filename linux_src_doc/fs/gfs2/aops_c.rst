.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/aops.c

.. _`gfs2_get_block_noalloc`:

gfs2_get_block_noalloc
======================

.. c:function:: int gfs2_get_block_noalloc(struct inode *inode, sector_t lblock, struct buffer_head *bh_result, int create)

    Fills in a buffer head with details about a block

    :param inode:
        The inode
    :type inode: struct inode \*

    :param lblock:
        The block number to look up
    :type lblock: sector_t

    :param bh_result:
        The buffer head to return the result in
    :type bh_result: struct buffer_head \*

    :param create:
        Non-zero if we may add block to the file
    :type create: int

.. _`gfs2_get_block_noalloc.return`:

Return
------

errno

.. _`gfs2_writepage_common`:

gfs2_writepage_common
=====================

.. c:function:: int gfs2_writepage_common(struct page *page, struct writeback_control *wbc)

    Common bits of writepage

    :param page:
        The page to be written
    :type page: struct page \*

    :param wbc:
        The writeback control
    :type wbc: struct writeback_control \*

.. _`gfs2_writepage_common.return`:

Return
------

1 if writepage is ok, otherwise an error code or zero if no error.

.. _`gfs2_writepage`:

gfs2_writepage
==============

.. c:function:: int gfs2_writepage(struct page *page, struct writeback_control *wbc)

    Write page for writeback mappings

    :param page:
        The page
    :type page: struct page \*

    :param wbc:
        The writeback control
    :type wbc: struct writeback_control \*

.. _`__gfs2_jdata_writepage`:

\__gfs2_jdata_writepage
=======================

.. c:function:: int __gfs2_jdata_writepage(struct page *page, struct writeback_control *wbc)

    The core of jdata writepage

    :param page:
        The page to write
    :type page: struct page \*

    :param wbc:
        The writeback control
    :type wbc: struct writeback_control \*

.. _`__gfs2_jdata_writepage.description`:

Description
-----------

This is shared between writepage and writepages and implements the
core of the writepage operation. If a transaction is required then
PageChecked will have been set and the transaction will have
already been started before this is called.

.. _`gfs2_jdata_writepage`:

gfs2_jdata_writepage
====================

.. c:function:: int gfs2_jdata_writepage(struct page *page, struct writeback_control *wbc)

    Write complete page

    :param page:
        Page to write
    :type page: struct page \*

    :param wbc:
        The writeback control
    :type wbc: struct writeback_control \*

.. _`gfs2_jdata_writepage.return`:

Return
------

errno

.. _`gfs2_writepages`:

gfs2_writepages
===============

.. c:function:: int gfs2_writepages(struct address_space *mapping, struct writeback_control *wbc)

    Write a bunch of dirty pages back to disk

    :param mapping:
        The mapping to write
    :type mapping: struct address_space \*

    :param wbc:
        Write-back control
    :type wbc: struct writeback_control \*

.. _`gfs2_writepages.description`:

Description
-----------

Used for both ordered and writeback modes.

.. _`gfs2_write_jdata_pagevec`:

gfs2_write_jdata_pagevec
========================

.. c:function:: int gfs2_write_jdata_pagevec(struct address_space *mapping, struct writeback_control *wbc, struct pagevec *pvec, int nr_pages, pgoff_t *done_index)

    Write back a pagevec's worth of pages

    :param mapping:
        The mapping
    :type mapping: struct address_space \*

    :param wbc:
        The writeback control
    :type wbc: struct writeback_control \*

    :param pvec:
        The vector of pages
    :type pvec: struct pagevec \*

    :param nr_pages:
        The number of pages to write
    :type nr_pages: int

    :param done_index:
        Page index
    :type done_index: pgoff_t \*

.. _`gfs2_write_jdata_pagevec.return`:

Return
------

non-zero if loop should terminate, zero otherwise

.. _`gfs2_write_cache_jdata`:

gfs2_write_cache_jdata
======================

.. c:function:: int gfs2_write_cache_jdata(struct address_space *mapping, struct writeback_control *wbc)

    Like write_cache_pages but different

    :param mapping:
        The mapping to write
    :type mapping: struct address_space \*

    :param wbc:
        The writeback control
    :type wbc: struct writeback_control \*

.. _`gfs2_write_cache_jdata.description`:

Description
-----------

The reason that we use our own function here is that we need to
start transactions before we grab page locks. This allows us
to get the ordering right.

.. _`gfs2_jdata_writepages`:

gfs2_jdata_writepages
=====================

.. c:function:: int gfs2_jdata_writepages(struct address_space *mapping, struct writeback_control *wbc)

    Write a bunch of dirty pages back to disk

    :param mapping:
        The mapping to write
    :type mapping: struct address_space \*

    :param wbc:
        The writeback control
    :type wbc: struct writeback_control \*

.. _`stuffed_readpage`:

stuffed_readpage
================

.. c:function:: int stuffed_readpage(struct gfs2_inode *ip, struct page *page)

    Fill in a Linux page with stuffed file data

    :param ip:
        the inode
    :type ip: struct gfs2_inode \*

    :param page:
        the page
    :type page: struct page \*

.. _`stuffed_readpage.return`:

Return
------

errno

.. _`__gfs2_readpage`:

\__gfs2_readpage
================

.. c:function:: int __gfs2_readpage(void *file, struct page *page)

    readpage

    :param file:
        The file to read a page for
    :type file: void \*

    :param page:
        The page to read
    :type page: struct page \*

.. _`__gfs2_readpage.description`:

Description
-----------

This is the core of gfs2's readpage. It's used by the internal file
reading code as in that case we already hold the glock. Also it's
called by \ :c:func:`gfs2_readpage`\  once the required lock has been granted.

.. _`gfs2_readpage`:

gfs2_readpage
=============

.. c:function:: int gfs2_readpage(struct file *file, struct page *page)

    read a page of a file

    :param file:
        The file to read
    :type file: struct file \*

    :param page:
        The page of the file
    :type page: struct page \*

.. _`gfs2_readpage.description`:

Description
-----------

This deals with the locking required. We have to unlock and
relock the page in order to get the locking in the right
order.

.. _`gfs2_internal_read`:

gfs2_internal_read
==================

.. c:function:: int gfs2_internal_read(struct gfs2_inode *ip, char *buf, loff_t *pos, unsigned size)

    read an internal file

    :param ip:
        The gfs2 inode
    :type ip: struct gfs2_inode \*

    :param buf:
        The buffer to fill
    :type buf: char \*

    :param pos:
        The file position
    :type pos: loff_t \*

    :param size:
        The amount to read
    :type size: unsigned

.. _`gfs2_readpages`:

gfs2_readpages
==============

.. c:function:: int gfs2_readpages(struct file *file, struct address_space *mapping, struct list_head *pages, unsigned nr_pages)

    Read a bunch of pages at once

    :param file:
        The file to read from
    :type file: struct file \*

    :param mapping:
        Address space info
    :type mapping: struct address_space \*

    :param pages:
        List of pages to read
    :type pages: struct list_head \*

    :param nr_pages:
        Number of pages to read
    :type nr_pages: unsigned

.. _`gfs2_readpages.some-notes`:

Some notes
----------

1. This is only for readahead, so we can simply ignore any things
which are slightly inconvenient (such as locking conflicts between
the page lock and the glock) and return having done no I/O. Its
obviously not something we'd want to do on too regular a basis.
Any I/O we ignore at this time will be done via readpage later.
2. We don't handle stuffed files here we let readpage do the honours.
3. \ :c:func:`mpage_readpages`\  does most of the heavy lifting in the common case.
4. \ :c:func:`gfs2_block_map`\  is relied upon to set BH_Boundary in the right places.

.. _`adjust_fs_space`:

adjust_fs_space
===============

.. c:function:: void adjust_fs_space(struct inode *inode)

    Adjusts the free space available due to gfs2_grow

    :param inode:
        the rindex inode
    :type inode: struct inode \*

.. _`gfs2_stuffed_write_end`:

gfs2_stuffed_write_end
======================

.. c:function:: int gfs2_stuffed_write_end(struct inode *inode, struct buffer_head *dibh, loff_t pos, unsigned copied, struct page *page)

    Write end for stuffed files

    :param inode:
        The inode
    :type inode: struct inode \*

    :param dibh:
        The buffer_head containing the on-disk inode
    :type dibh: struct buffer_head \*

    :param pos:
        The file position
    :type pos: loff_t

    :param copied:
        How much was actually copied by the VFS
    :type copied: unsigned

    :param page:
        The page
    :type page: struct page \*

.. _`gfs2_stuffed_write_end.description`:

Description
-----------

This copies the data from the page into the inode block after
the inode data structure itself.

.. _`gfs2_stuffed_write_end.return`:

Return
------

copied bytes or errno

.. _`jdata_set_page_dirty`:

jdata_set_page_dirty
====================

.. c:function:: int jdata_set_page_dirty(struct page *page)

    Page dirtying function

    :param page:
        The page to dirty
    :type page: struct page \*

.. _`jdata_set_page_dirty.return`:

Return
------

1 if it dirtyed the page, or 0 otherwise

.. _`gfs2_bmap`:

gfs2_bmap
=========

.. c:function:: sector_t gfs2_bmap(struct address_space *mapping, sector_t lblock)

    Block map function

    :param mapping:
        Address space info
    :type mapping: struct address_space \*

    :param lblock:
        The block to map
    :type lblock: sector_t

.. _`gfs2_bmap.return`:

Return
------

The disk address for the block or 0 on hole or error

.. _`gfs2_releasepage`:

gfs2_releasepage
================

.. c:function:: int gfs2_releasepage(struct page *page, gfp_t gfp_mask)

    free the metadata associated with a page

    :param page:
        the page that's being released
    :type page: struct page \*

    :param gfp_mask:
        passed from Linux VFS, ignored by us
    :type gfp_mask: gfp_t

.. _`gfs2_releasepage.description`:

Description
-----------

Call \ :c:func:`try_to_free_buffers`\  if the buffers in this page can be
released.

.. _`gfs2_releasepage.return`:

Return
------

0

.. This file was automatic generated / don't edit.

