.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/inode.c

.. _`lock_parent`:

lock_parent
===========

.. c:function:: struct dentry *lock_parent(struct dentry *dentry)

    Linux filesystem encryption layer

    :param struct dentry \*dentry:
        *undescribed*

.. _`lock_parent.description`:

Description
-----------

Copyright (C) 1997-2004 Erez Zadok
Copyright (C) 2001-2004 Stony Brook University
Copyright (C) 2004-2007 International Business Machines Corp.
Author(s): Michael A. Halcrow <mahalcro\ ``us``\ .ibm.com>
Michael C. Thompsion <mcthomps\ ``us``\ .ibm.com>

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

.. _`ecryptfs_interpose`:

ecryptfs_interpose
==================

.. c:function:: int ecryptfs_interpose(struct dentry *lower_dentry, struct dentry *dentry, struct super_block *sb)

    :param struct dentry \*lower_dentry:
        Existing dentry in the lower filesystem

    :param struct dentry \*dentry:
        ecryptfs' dentry

    :param struct super_block \*sb:
        ecryptfs's super_block

.. _`ecryptfs_interpose.description`:

Description
-----------

Interposes upper and lower dentries.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_do_create`:

ecryptfs_do_create
==================

.. c:function:: struct inode *ecryptfs_do_create(struct inode *directory_inode, struct dentry *ecryptfs_dentry, umode_t mode)

    :param struct inode \*directory_inode:
        inode of the new file's dentry's parent in ecryptfs

    :param struct dentry \*ecryptfs_dentry:
        New file's dentry in ecryptfs

    :param umode_t mode:
        The mode of the new file

.. _`ecryptfs_do_create.description`:

Description
-----------

Creates the underlying file and the eCryptfs inode which will link to
it. It will also update the eCryptfs directory inode to mimic the
stat of the lower directory inode.

Returns the new eCryptfs inode on success; an ERR_PTR on error condition

.. _`ecryptfs_initialize_file`:

ecryptfs_initialize_file
========================

.. c:function:: int ecryptfs_initialize_file(struct dentry *ecryptfs_dentry, struct inode *ecryptfs_inode)

    :param struct dentry \*ecryptfs_dentry:
        *undescribed*

    :param struct inode \*ecryptfs_inode:
        *undescribed*

.. _`ecryptfs_initialize_file.description`:

Description
-----------

Cause the file to be changed from a basic empty file to an ecryptfs
file with a header and first data page.

Returns zero on success

.. _`ecryptfs_create`:

ecryptfs_create
===============

.. c:function:: int ecryptfs_create(struct inode *directory_inode, struct dentry *ecryptfs_dentry, umode_t mode, bool excl)

    :param struct inode \*directory_inode:
        *undescribed*

    :param struct dentry \*ecryptfs_dentry:
        *undescribed*

    :param umode_t mode:
        The mode of the new file.

    :param bool excl:
        *undescribed*

.. _`ecryptfs_create.description`:

Description
-----------

Creates a new file.

Returns zero on success; non-zero on error condition

.. _`ecryptfs_lookup_interpose`:

ecryptfs_lookup_interpose
=========================

.. c:function:: struct dentry *ecryptfs_lookup_interpose(struct dentry *dentry, struct dentry *lower_dentry)

    Dentry interposition for a lookup

    :param struct dentry \*dentry:
        *undescribed*

    :param struct dentry \*lower_dentry:
        *undescribed*

.. _`ecryptfs_lookup`:

ecryptfs_lookup
===============

.. c:function:: struct dentry *ecryptfs_lookup(struct inode *ecryptfs_dir_inode, struct dentry *ecryptfs_dentry, unsigned int flags)

    :param struct inode \*ecryptfs_dir_inode:
        The eCryptfs directory inode

    :param struct dentry \*ecryptfs_dentry:
        The eCryptfs dentry that we are looking up

    :param unsigned int flags:
        lookup flags

.. _`ecryptfs_lookup.description`:

Description
-----------

Find a file on disk. If the file does not exist, then we'll add it to the
dentry cache and continue on to read it from the disk.

.. _`upper_size_to_lower_size`:

upper_size_to_lower_size
========================

.. c:function:: loff_t upper_size_to_lower_size(struct ecryptfs_crypt_stat *crypt_stat, loff_t upper_size)

    :param struct ecryptfs_crypt_stat \*crypt_stat:
        Crypt_stat associated with file

    :param loff_t upper_size:
        Size of the upper file

.. _`upper_size_to_lower_size.description`:

Description
-----------

Calculate the required size of the lower file based on the
specified size of the upper file. This calculation is based on the
number of headers in the underlying file and the extent size.

Returns Calculated size of the lower file.

.. _`truncate_upper`:

truncate_upper
==============

.. c:function:: int truncate_upper(struct dentry *dentry, struct iattr *ia, struct iattr *lower_ia)

    :param struct dentry \*dentry:
        The ecryptfs layer dentry

    :param struct iattr \*ia:
        Address of the ecryptfs inode's attributes

    :param struct iattr \*lower_ia:
        Address of the lower inode's attributes

.. _`truncate_upper.description`:

Description
-----------

Function to handle truncations modifying the size of the file. Note
that the file sizes are interpolated. When expanding, we are simply
writing strings of 0's out. When truncating, we truncate the upper
inode and update the lower_ia according to the page index
interpolations. If ATTR_SIZE is set in lower_ia->ia_valid upon return,
the caller must use lower_ia in a call to \ :c:func:`notify_change`\  to perform
the truncation of the lower inode.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_truncate`:

ecryptfs_truncate
=================

.. c:function:: int ecryptfs_truncate(struct dentry *dentry, loff_t new_length)

    :param struct dentry \*dentry:
        The ecryptfs layer dentry

    :param loff_t new_length:
        The length to expand the file to

.. _`ecryptfs_truncate.description`:

Description
-----------

Simple function that handles the truncation of an eCryptfs inode and
its corresponding lower inode.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_setattr`:

ecryptfs_setattr
================

.. c:function:: int ecryptfs_setattr(struct dentry *dentry, struct iattr *ia)

    :param struct dentry \*dentry:
        dentry handle to the inode to modify

    :param struct iattr \*ia:
        Structure with flags of what to change and values

.. _`ecryptfs_setattr.description`:

Description
-----------

Updates the metadata of an inode. If the update is to the size
i.e. truncation, then ecryptfs_truncate will handle the size modification
of both the ecryptfs inode and the lower inode.

All other metadata changes will be passed right to the lower filesystem,
and we will just update our inode to look like the lower.

.. This file was automatic generated / don't edit.

