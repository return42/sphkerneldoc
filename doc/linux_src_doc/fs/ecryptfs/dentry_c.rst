.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/dentry.c

.. _`ecryptfs_d_revalidate`:

ecryptfs_d_revalidate
=====================

.. c:function:: int ecryptfs_d_revalidate(struct dentry *dentry, unsigned int flags)

    Linux filesystem encryption layer

    :param struct dentry \*dentry:
        *undescribed*

    :param unsigned int flags:
        *undescribed*

.. _`ecryptfs_d_revalidate.description`:

Description
-----------

Copyright (C) 1997-2003 Erez Zadok
Copyright (C) 2001-2003 Stony Brook University
Copyright (C) 2004-2006 International Business Machines Corp.
Author(s): Michael A. Halcrow <mahalcro\ ``us``\ .ibm.com>

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

.. _`ecryptfs_d_release`:

ecryptfs_d_release
==================

.. c:function:: void ecryptfs_d_release(struct dentry *dentry)

    :param struct dentry \*dentry:
        The ecryptfs dentry

.. _`ecryptfs_d_release.description`:

Description
-----------

Called when a dentry is really deallocated.

.. This file was automatic generated / don't edit.

