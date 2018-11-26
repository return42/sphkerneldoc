.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/vfs_addr.c

.. _`v9fs_fid_readpage`:

v9fs_fid_readpage
=================

.. c:function:: int v9fs_fid_readpage(struct p9_fid *fid, struct page *page)

    read an entire page in from 9P

    :param fid:
        fid being read
    :type fid: struct p9_fid \*

    :param page:
        structure to page
    :type page: struct page \*

.. _`v9fs_vfs_readpage`:

v9fs_vfs_readpage
=================

.. c:function:: int v9fs_vfs_readpage(struct file *filp, struct page *page)

    read an entire page in from 9P

    :param filp:
        file being read
    :type filp: struct file \*

    :param page:
        structure to page
    :type page: struct page \*

.. _`v9fs_vfs_readpages`:

v9fs_vfs_readpages
==================

.. c:function:: int v9fs_vfs_readpages(struct file *filp, struct address_space *mapping, struct list_head *pages, unsigned nr_pages)

    read a set of pages from 9P

    :param filp:
        file being read
    :type filp: struct file \*

    :param mapping:
        the address space
    :type mapping: struct address_space \*

    :param pages:
        list of pages to read
    :type pages: struct list_head \*

    :param nr_pages:
        count of pages to read
    :type nr_pages: unsigned

.. _`v9fs_release_page`:

v9fs_release_page
=================

.. c:function:: int v9fs_release_page(struct page *page, gfp_t gfp)

    release the private state associated with a page

    :param page:
        *undescribed*
    :type page: struct page \*

    :param gfp:
        *undescribed*
    :type gfp: gfp_t

.. _`v9fs_release_page.description`:

Description
-----------

Returns 1 if the page can be released, false otherwise.

.. _`v9fs_invalidate_page`:

v9fs_invalidate_page
====================

.. c:function:: void v9fs_invalidate_page(struct page *page, unsigned int offset, unsigned int length)

    Invalidate a page completely or partially

    :param page:
        structure to page
    :type page: struct page \*

    :param offset:
        offset in the page
    :type offset: unsigned int

    :param length:
        *undescribed*
    :type length: unsigned int

.. _`v9fs_launder_page`:

v9fs_launder_page
=================

.. c:function:: int v9fs_launder_page(struct page *page)

    Writeback a dirty page Returns 0 on success.

    :param page:
        *undescribed*
    :type page: struct page \*

.. _`v9fs_direct_io`:

v9fs_direct_IO
==============

.. c:function:: ssize_t v9fs_direct_IO(struct kiocb *iocb, struct iov_iter *iter)

    9P address space operation for direct I/O

    :param iocb:
        target I/O control block
    :type iocb: struct kiocb \*

    :param iter:
        *undescribed*
    :type iter: struct iov_iter \*

.. _`v9fs_direct_io.description`:

Description
-----------

The presence of \ :c:func:`v9fs_direct_IO`\  in the address space ops vector
allowes \ :c:func:`open`\  O_DIRECT flags which would have failed otherwise.

In the non-cached mode, we shunt off direct read and write requests before
the VFS gets them, so this method should never be called.

Direct IO is not 'yet' supported in the cached mode. Hence when
this routine is called through \ :c:func:`generic_file_aio_read`\ , the read/write fails
with an error.

.. This file was automatic generated / don't edit.

