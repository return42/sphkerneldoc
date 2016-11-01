.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/aops.h

.. _`ntfs_unmap_page`:

ntfs_unmap_page
===============

.. c:function:: void ntfs_unmap_page(struct page *page)

    release a page that was mapped using \ :c:func:`ntfs_map_page`\ 

    :param struct page \*page:
        the page to release

.. _`ntfs_unmap_page.description`:

Description
-----------

Unpin, unmap and release a page that was obtained from \ :c:func:`ntfs_map_page`\ .

.. _`ntfs_map_page`:

ntfs_map_page
=============

.. c:function:: struct page *ntfs_map_page(struct address_space *mapping, unsigned long index)

    map a page into accessible memory, reading it if necessary

    :param struct address_space \*mapping:
        address space for which to obtain the page

    :param unsigned long index:
        index into the page cache for \ ``mapping``\  of the page to map

.. _`ntfs_map_page.description`:

Description
-----------

Read a page from the page cache of the address space \ ``mapping``\  at position
\ ``index``\ , where \ ``index``\  is in units of PAGE_SIZE, and not in bytes.

If the page is not in memory it is loaded from disk first using the readpage
method defined in the address space operations of \ ``mapping``\  and the page is
added to the page cache of \ ``mapping``\  in the process.

If the page belongs to an mst protected attribute and it is marked as such
in its ntfs inode (NInoMstProtected()) the mst fixups are applied but no
error checking is performed.  This means the caller has to verify whether
the ntfs record(s) contained in the page are valid or not using one of the
ntfs_is_XXXX_record{,p}() macros, where XXXX is the record type you are
expecting to see.  (For details of the macros, see fs/ntfs/layout.h.)

If the page is in high memory it is mapped into memory directly addressible
by the kernel.

Finally the page count is incremented, thus pinning the page into place.

The above means that page_address(page) can be used on all pages obtained
with \ :c:func:`ntfs_map_page`\  to get the kernel virtual address of the page.

When finished with the page, the caller has to call \ :c:func:`ntfs_unmap_page`\  to
unpin, unmap and release the page.

Note this does not grant exclusive access. If such is desired, the caller
must provide it independently of the ntfs_{un}map_page() calls by using
a {rw_}semaphore or other means of serialization. A spin lock cannot be
used as \ :c:func:`ntfs_map_page`\  can block.

The unlocked and uptodate page is returned on success or an encoded error
on failure. Caller has to test for error using the \ :c:func:`IS_ERR`\  macro on the
return value. If that evaluates to 'true', the negative error code can be
obtained using \ :c:func:`PTR_ERR`\  on the return value of \ :c:func:`ntfs_map_page`\ .

.. This file was automatic generated / don't edit.

