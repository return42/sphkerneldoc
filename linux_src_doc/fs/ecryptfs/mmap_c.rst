.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/mmap.c

.. _`ecryptfs_get_locked_page`:

ecryptfs_get_locked_page
========================

.. c:function:: struct page *ecryptfs_get_locked_page(struct inode *inode, loff_t index)

    Linux filesystem encryption layer This is where eCryptfs coordinates the symmetric encryption and decryption of the file data as it passes between the lower encrypted file and the upper decrypted file.

    :param inode:
        *undescribed*
    :type inode: struct inode \*

    :param index:
        *undescribed*
    :type index: loff_t

.. _`ecryptfs_get_locked_page.description`:

Description
-----------

Copyright (C) 1997-2003 Erez Zadok
Copyright (C) 2001-2003 Stony Brook University
Copyright (C) 2004-2007 International Business Machines Corp.
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

.. _`ecryptfs_writepage`:

ecryptfs_writepage
==================

.. c:function:: int ecryptfs_writepage(struct page *page, struct writeback_control *wbc)

    :param page:
        Page that is locked before this call is made
    :type page: struct page \*

    :param wbc:
        *undescribed*
    :type wbc: struct writeback_control \*

.. _`ecryptfs_writepage.description`:

Description
-----------

Returns zero on success; non-zero otherwise

This is where we encrypt the data and pass the encrypted data to
the lower filesystem.  In OpenPGP-compatible mode, we operate on
entire underlying packets.

.. _`ecryptfs_copy_up_encrypted_with_header`:

ecryptfs_copy_up_encrypted_with_header
======================================

.. c:function:: int ecryptfs_copy_up_encrypted_with_header(struct page *page, struct ecryptfs_crypt_stat *crypt_stat)

    Octets 0-7:        Unencrypted file size (big-endian) Octets 8-15:       eCryptfs special marker Octets 16-19:      Flags

    :param page:
        *undescribed*
    :type page: struct page \*

    :param crypt_stat:
        *undescribed*
    :type crypt_stat: struct ecryptfs_crypt_stat \*

.. _`ecryptfs_copy_up_encrypted_with_header.octet-16`:

Octet 16
--------

File format version number (between 0 and 255)
Octets 17-18:     Reserved

.. _`ecryptfs_copy_up_encrypted_with_header.octet-19`:

Octet 19
--------

Bit 1 (lsb): Reserved
Bit 2: Encrypted?
Bits 3-8: Reserved
Octets 20-23:      Header extent size (big-endian)
Octets 24-25:      Number of header extents at front of file
(big-endian)

.. _`ecryptfs_copy_up_encrypted_with_header.octet--26`:

Octet  26
---------

Begin RFC 2440 authentication token packet set

.. _`ecryptfs_readpage`:

ecryptfs_readpage
=================

.. c:function:: int ecryptfs_readpage(struct file *file, struct page *page)

    :param file:
        An eCryptfs file
    :type file: struct file \*

    :param page:
        Page from eCryptfs inode mapping into which to stick the read data
    :type page: struct page \*

.. _`ecryptfs_readpage.description`:

Description
-----------

Read in a page, decrypting if necessary.

Returns zero on success; non-zero on error.

.. _`fill_zeros_to_end_of_page`:

fill_zeros_to_end_of_page
=========================

.. c:function:: int fill_zeros_to_end_of_page(struct page *page, unsigned int to)

    :param page:
        *undescribed*
    :type page: struct page \*

    :param to:
        *undescribed*
    :type to: unsigned int

.. _`ecryptfs_write_begin`:

ecryptfs_write_begin
====================

.. c:function:: int ecryptfs_write_begin(struct file *file, struct address_space *mapping, loff_t pos, unsigned len, unsigned flags, struct page **pagep, void **fsdata)

    :param file:
        The eCryptfs file
    :type file: struct file \*

    :param mapping:
        The eCryptfs object
    :type mapping: struct address_space \*

    :param pos:
        The file offset at which to start writing
    :type pos: loff_t

    :param len:
        Length of the write
    :type len: unsigned

    :param flags:
        Various flags
    :type flags: unsigned

    :param pagep:
        Pointer to return the page
    :type pagep: struct page \*\*

    :param fsdata:
        Pointer to return fs data (unused)
    :type fsdata: void \*\*

.. _`ecryptfs_write_begin.description`:

Description
-----------

This function must zero any hole we create

Returns zero on success; non-zero otherwise

.. _`ecryptfs_write_inode_size_to_header`:

ecryptfs_write_inode_size_to_header
===================================

.. c:function:: int ecryptfs_write_inode_size_to_header(struct inode *ecryptfs_inode)

    :param ecryptfs_inode:
        *undescribed*
    :type ecryptfs_inode: struct inode \*

.. _`ecryptfs_write_inode_size_to_header.description`:

Description
-----------

Writes the lower file size to the first 8 bytes of the header.

Returns zero on success; non-zero on error.

.. _`ecryptfs_write_end`:

ecryptfs_write_end
==================

.. c:function:: int ecryptfs_write_end(struct file *file, struct address_space *mapping, loff_t pos, unsigned len, unsigned copied, struct page *page, void *fsdata)

    :param file:
        The eCryptfs file object
    :type file: struct file \*

    :param mapping:
        The eCryptfs object
    :type mapping: struct address_space \*

    :param pos:
        The file position
    :type pos: loff_t

    :param len:
        The length of the data (unused)
    :type len: unsigned

    :param copied:
        The amount of data copied
    :type copied: unsigned

    :param page:
        The eCryptfs page
    :type page: struct page \*

    :param fsdata:
        The fsdata (unused)
    :type fsdata: void \*

.. This file was automatic generated / don't edit.

