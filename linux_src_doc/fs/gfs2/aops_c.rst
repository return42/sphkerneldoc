.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/aops.c

.. _`gfs2_get_block_noalloc`:

gfs2_get_block_noalloc
======================

.. c:function:: int gfs2_get_block_noalloc(struct inode *inode, sector_t lblock, struct buffer_head *bh_result, int create)

    Fills in a buffer head with details about a block

    :param struct inode \*inode:
        The inode

    :param sector_t lblock:
        The block number to look up

    :param struct buffer_head \*bh_result:
        The buffer head to return the result in

    :param int create:
        Non-zero if we may add block to the file

.. _`gfs2_get_block_noalloc.return`:

Return
------

errno

.. _`gfs2_writepage_common`:

gfs2_writepage_common
=====================

.. c:function:: int gfs2_writepage_common(struct page *page, struct writeback_control *wbc)

    Common bits of writepage

    :param struct page \*page:
        The page to be written

    :param struct writeback_control \*wbc:
        The writeback control

.. _`gfs2_writepage_common.return`:

Return
------

1 if writepage is ok, otherwise an error code or zero if no error.

.. _`gfs2_writepage`:

gfs2_writepage
==============

.. c:function:: int gfs2_writepage(struct page *page, struct writeback_control *wbc)

    Write page for writeback mappings

    :param struct page \*page:
        The page

    :param struct writeback_control \*wbc:
        The writeback control

.. _`__gfs2_jdata_writepage`:

\__gfs2_jdata_writepage
=======================

.. c:function:: int __gfs2_jdata_writepage(struct page *page, struct writeback_control *wbc)

    The core of jdata writepage

    :param struct page \*page:
        The page to write

    :param struct writeback_control \*wbc:
        The writeback control

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

    :param struct page \*page:
        Page to write

    :param struct writeback_control \*wbc:
        The writeback control

.. _`gfs2_jdata_writepage.return`:

Return
------

errno

.. _`gfs2_writepages`:

gfs2_writepages
===============

.. c:function:: int gfs2_writepages(struct address_space *mapping, struct writeback_control *wbc)

    Write a bunch of dirty pages back to disk

    :param struct address_space \*mapping:
        The mapping to write

    :param struct writeback_control \*wbc:
        Write-back control

.. _`gfs2_writepages.description`:

Description
-----------

Used for both ordered and writeback modes.

.. _`gfs2_write_jdata_pagevec`:

gfs2_write_jdata_pagevec
========================

.. c:function:: int gfs2_write_jdata_pagevec(struct address_space *mapping, struct writeback_control *wbc, struct pagevec *pvec, int nr_pages, pgoff_t *done_index)

    Write back a pagevec's worth of pages

    :param struct address_space \*mapping:
        The mapping

    :param struct writeback_control \*wbc:
        The writeback control

    :param struct pagevec \*pvec:
        The vector of pages

    :param int nr_pages:
        The number of pages to write

    :param pgoff_t \*done_index:
        Page index

.. _`gfs2_write_jdata_pagevec.return`:

Return
------

non-zero if loop should terminate, zero otherwise

.. _`gfs2_write_cache_jdata`:

gfs2_write_cache_jdata
======================

.. c:function:: int gfs2_write_cache_jdata(struct address_space *mapping, struct writeback_control *wbc)

    Like write_cache_pages but different

    :param struct address_space \*mapping:
        The mapping to write

    :param struct writeback_control \*wbc:
        The writeback control

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

    :param struct address_space \*mapping:
        The mapping to write

    :param struct writeback_control \*wbc:
        The writeback control

.. _`stuffed_readpage`:

stuffed_readpage
================

.. c:function:: int stuffed_readpage(struct gfs2_inode *ip, struct page *page)

    Fill in a Linux page with stuffed file data

    :param struct gfs2_inode \*ip:
        the inode

    :param struct page \*page:
        the page

.. _`stuffed_readpage.return`:

Return
------

errno

.. _`__gfs2_readpage`:

\__gfs2_readpage
================

.. c:function:: int __gfs2_readpage(void *file, struct page *page)

    readpage

    :param void \*file:
        The file to read a page for

    :param struct page \*page:
        The page to read

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

    :param struct file \*file:
        The file to read

    :param struct page \*page:
        The page of the file

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

    :param struct gfs2_inode \*ip:
        The gfs2 inode

    :param char \*buf:
        The buffer to fill

    :param loff_t \*pos:
        The file position

    :param unsigned size:
        The amount to read

.. _`gfs2_readpages`:

gfs2_readpages
==============

.. c:function:: int gfs2_readpages(struct file *file, struct address_space *mapping, struct list_head *pages, unsigned nr_pages)

    Read a bunch of pages at once

    :param struct file \*file:
        The file to read from

    :param struct address_space \*mapping:
        Address space info

    :param struct list_head \*pages:
        List of pages to read

    :param unsigned nr_pages:
        Number of pages to read

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

.. _`gfs2_write_begin`:

gfs2_write_begin
================

.. c:function:: int gfs2_write_begin(struct file *file, struct address_space *mapping, loff_t pos, unsigned len, unsigned flags, struct page **pagep, void **fsdata)

    Begin to write to a file

    :param struct file \*file:
        The file to write to

    :param struct address_space \*mapping:
        The mapping in which to write

    :param loff_t pos:
        The file offset at which to start writing

    :param unsigned len:
        Length of the write

    :param unsigned flags:
        Various flags

    :param struct page \*\*pagep:
        Pointer to return the page

    :param void \*\*fsdata:
        Pointer to return fs data (unused by GFS2)

.. _`gfs2_write_begin.return`:

Return
------

errno

.. _`adjust_fs_space`:

adjust_fs_space
===============

.. c:function:: void adjust_fs_space(struct inode *inode)

    Adjusts the free space available due to gfs2_grow

    :param struct inode \*inode:
        the rindex inode

.. _`gfs2_stuffed_write_end`:

gfs2_stuffed_write_end
======================

.. c:function:: int gfs2_stuffed_write_end(struct inode *inode, struct buffer_head *dibh, loff_t pos, unsigned len, unsigned copied, struct page *page)

    Write end for stuffed files

    :param struct inode \*inode:
        The inode

    :param struct buffer_head \*dibh:
        The buffer_head containing the on-disk inode

    :param loff_t pos:
        The file position

    :param unsigned len:
        The length of the write

    :param unsigned copied:
        How much was actually copied by the VFS

    :param struct page \*page:
        The page

.. _`gfs2_stuffed_write_end.description`:

Description
-----------

This copies the data from the page into the inode block after
the inode data structure itself.

.. _`gfs2_stuffed_write_end.return`:

Return
------

errno

.. _`gfs2_write_end`:

gfs2_write_end
==============

.. c:function:: int gfs2_write_end(struct file *file, struct address_space *mapping, loff_t pos, unsigned len, unsigned copied, struct page *page, void *fsdata)

    :param struct file \*file:
        The file to write to

    :param struct address_space \*mapping:
        The address space to write to

    :param loff_t pos:
        The file position

    :param unsigned len:
        The length of the data

    :param unsigned copied:
        How much was actually copied by the VFS

    :param struct page \*page:
        The page that has been written

    :param void \*fsdata:
        The fsdata (unused in GFS2)

.. _`gfs2_write_end.description`:

Description
-----------

The main write_end function for GFS2. We have a separate one for
stuffed files as they are slightly different, otherwise we just
put our locking around the VFS provided functions.

.. _`gfs2_write_end.return`:

Return
------

errno

.. _`gfs2_set_page_dirty`:

gfs2_set_page_dirty
===================

.. c:function:: int gfs2_set_page_dirty(struct page *page)

    Page dirtying function

    :param struct page \*page:
        The page to dirty

.. _`gfs2_set_page_dirty.return`:

Return
------

1 if it dirtyed the page, or 0 otherwise

.. _`gfs2_bmap`:

gfs2_bmap
=========

.. c:function:: sector_t gfs2_bmap(struct address_space *mapping, sector_t lblock)

    Block map function

    :param struct address_space \*mapping:
        Address space info

    :param sector_t lblock:
        The block to map

.. _`gfs2_bmap.return`:

Return
------

The disk address for the block or 0 on hole or error

.. _`gfs2_ok_for_dio`:

gfs2_ok_for_dio
===============

.. c:function:: int gfs2_ok_for_dio(struct gfs2_inode *ip, loff_t offset)

    check that dio is valid on this file

    :param struct gfs2_inode \*ip:
        The inode

    :param loff_t offset:
        The offset at which we are reading or writing

.. _`gfs2_ok_for_dio.return`:

Return
------

0 (to ignore the i/o request and thus fall back to buffered i/o)
1 (to accept the i/o request)

.. _`gfs2_releasepage`:

gfs2_releasepage
================

.. c:function:: int gfs2_releasepage(struct page *page, gfp_t gfp_mask)

    free the metadata associated with a page

    :param struct page \*page:
        the page that's being released

    :param gfp_t gfp_mask:
        passed from Linux VFS, ignored by us

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

