.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/file.c

.. _`ecryptfs_read_update_atime`:

ecryptfs_read_update_atime
==========================

.. c:function:: ssize_t ecryptfs_read_update_atime(struct kiocb *iocb, struct iov_iter *to)

    Linux filesystem encryption layer

    :param struct kiocb \*iocb:
        *undescribed*

    :param struct iov_iter \*to:
        *undescribed*

.. _`ecryptfs_read_update_atime.description`:

Description
-----------

Copyright (C) 1997-2004 Erez Zadok
Copyright (C) 2001-2004 Stony Brook University
Copyright (C) 2004-2007 International Business Machines Corp.
Author(s): Michael A. Halcrow <mhalcrow\ ``us``\ .ibm.com>
Michael C. Thompson <mcthomps\ ``us``\ .ibm.com>

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

.. _`ecryptfs_readdir`:

ecryptfs_readdir
================

.. c:function:: int ecryptfs_readdir(struct file *file, struct dir_context *ctx)

    :param struct file \*file:
        The eCryptfs directory file

    :param struct dir_context \*ctx:
        The actor to feed the entries to

.. _`ecryptfs_open`:

ecryptfs_open
=============

.. c:function:: int ecryptfs_open(struct inode *inode, struct file *file)

    :param struct inode \*inode:
        inode specifying file to open

    :param struct file \*file:
        Structure to return filled in

.. _`ecryptfs_open.description`:

Description
-----------

Opens the file specified by inode.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_dir_open`:

ecryptfs_dir_open
=================

.. c:function:: int ecryptfs_dir_open(struct inode *inode, struct file *file)

    :param struct inode \*inode:
        inode specifying file to open

    :param struct file \*file:
        Structure to return filled in

.. _`ecryptfs_dir_open.description`:

Description
-----------

Opens the file specified by inode.

Returns zero on success; non-zero otherwise

.. This file was automatic generated / don't edit.

