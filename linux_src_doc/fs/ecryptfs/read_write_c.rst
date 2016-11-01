.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/read_write.c

.. _`ecryptfs_write_lower`:

ecryptfs_write_lower
====================

.. c:function:: int ecryptfs_write_lower(struct inode *ecryptfs_inode, char *data, loff_t offset, size_t size)

    Linux filesystem encryption layer

    :param struct inode \*ecryptfs_inode:
        *undescribed*

    :param char \*data:
        *undescribed*

    :param loff_t offset:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`ecryptfs_write_lower.description`:

Description
-----------

Copyright (C) 2007 International Business Machines Corp.
Author(s): Michael A. Halcrow <mahalcro@us.ibm.com>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
02111-1307, USA.

.. _`ecryptfs_write_lower_page_segment`:

ecryptfs_write_lower_page_segment
=================================

.. c:function:: int ecryptfs_write_lower_page_segment(struct inode *ecryptfs_inode, struct page *page_for_lower, size_t offset_in_page, size_t size)

    :param struct inode \*ecryptfs_inode:
        The eCryptfs inode

    :param struct page \*page_for_lower:
        The page containing the data to be written to the
        lower file

    :param size_t offset_in_page:
        The offset in the \ ``page_for_lower``\  from which to
        start writing the data

    :param size_t size:
        The amount of data from \ ``page_for_lower``\  to write to the
        lower file

.. _`ecryptfs_write_lower_page_segment.description`:

Description
-----------

Determines the byte offset in the file for the given page and
offset within the page, maps the page, and makes the call to write
the contents of \ ``page_for_lower``\  to the lower inode.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_write`:

ecryptfs_write
==============

.. c:function:: int ecryptfs_write(struct inode *ecryptfs_inode, char *data, loff_t offset, size_t size)

    :param struct inode \*ecryptfs_inode:
        The eCryptfs file into which to write

    :param char \*data:
        Virtual address where data to write is located

    :param loff_t offset:
        Offset in the eCryptfs file at which to begin writing the
        data from \ ``data``\ 

    :param size_t size:
        The number of bytes to write from \ ``data``\ 

.. _`ecryptfs_write.description`:

Description
-----------

Write an arbitrary amount of data to an arbitrary location in the
eCryptfs inode page cache. This is done on a page-by-page, and then
by an extent-by-extent, basis; individual extents are encrypted and
written to the lower page cache (via VFS writes). This function
takes care of all the address translation to locations in the lower
filesystem; it also handles truncate events, writing out zeros
where necessary.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_read_lower`:

ecryptfs_read_lower
===================

.. c:function:: int ecryptfs_read_lower(char *data, loff_t offset, size_t size, struct inode *ecryptfs_inode)

    :param char \*data:
        The read data is stored here by this function

    :param loff_t offset:
        Byte offset in the lower file from which to read the data

    :param size_t size:
        Number of bytes to read from \ ``offset``\  of the lower file and
        store into \ ``data``\ 

    :param struct inode \*ecryptfs_inode:
        The eCryptfs inode

.. _`ecryptfs_read_lower.description`:

Description
-----------

Read \ ``size``\  bytes of data at byte offset \ ``offset``\  from the lower
inode into memory location \ ``data``\ .

Returns bytes read on success; 0 on EOF; less than zero on error

.. _`ecryptfs_read_lower_page_segment`:

ecryptfs_read_lower_page_segment
================================

.. c:function:: int ecryptfs_read_lower_page_segment(struct page *page_for_ecryptfs, pgoff_t page_index, size_t offset_in_page, size_t size, struct inode *ecryptfs_inode)

    :param struct page \*page_for_ecryptfs:
        The page into which data for eCryptfs will be
        written

    :param pgoff_t page_index:
        *undescribed*

    :param size_t offset_in_page:
        Offset in \ ``page_for_ecryptfs``\  from which to start
        writing

    :param size_t size:
        The number of bytes to write into \ ``page_for_ecryptfs``\ 

    :param struct inode \*ecryptfs_inode:
        The eCryptfs inode

.. _`ecryptfs_read_lower_page_segment.description`:

Description
-----------

Determines the byte offset in the file for the given page and
offset within the page, maps the page, and makes the call to read
the contents of \ ``page_for_ecryptfs``\  from the lower inode.

Returns zero on success; non-zero otherwise

.. This file was automatic generated / don't edit.

