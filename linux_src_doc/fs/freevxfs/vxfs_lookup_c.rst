.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/freevxfs/vxfs_lookup.c

.. _`vxfs_find_entry`:

vxfs_find_entry
===============

.. c:function:: struct vxfs_direct *vxfs_find_entry(struct inode *ip, struct dentry *dp, struct page **ppp)

    find a mathing directory entry for a dentry

    :param struct inode \*ip:
        directory inode

    :param struct dentry \*dp:
        dentry for which we want to find a direct

    :param struct page \*\*ppp:
        gets filled with the page the return value sits in

.. _`vxfs_find_entry.description`:

Description
-----------

vxfs_find_entry finds a \ :c:type:`struct vxfs_direct <vxfs_direct>`\  for the VFS directory
cache entry \ ``dp``\ .  \ ``ppp``\  will be filled with the page the return
value resides in.

.. _`vxfs_find_entry.return`:

Return
------

The wanted direct on success, else a NULL pointer.

.. _`vxfs_inode_by_name`:

vxfs_inode_by_name
==================

.. c:function:: ino_t vxfs_inode_by_name(struct inode *dip, struct dentry *dp)

    find inode number for dentry

    :param struct inode \*dip:
        directory to search in

    :param struct dentry \*dp:
        dentry we search for

.. _`vxfs_inode_by_name.description`:

Description
-----------

vxfs_inode_by_name finds out the inode number of
the path component described by \ ``dp``\  in \ ``dip``\ .

.. _`vxfs_inode_by_name.return`:

Return
------

The wanted inode number on success, else Zero.

.. _`vxfs_lookup`:

vxfs_lookup
===========

.. c:function:: struct dentry *vxfs_lookup(struct inode *dip, struct dentry *dp, unsigned int flags)

    lookup pathname component

    :param struct inode \*dip:
        dir in which we lookup

    :param struct dentry \*dp:
        dentry we lookup

    :param unsigned int flags:
        lookup flags

.. _`vxfs_lookup.description`:

Description
-----------

vxfs_lookup tries to lookup the pathname component described
by \ ``dp``\  in \ ``dip``\ .

.. _`vxfs_lookup.return`:

Return
------

A NULL-pointer on success, else a negative error code encoded
in the return pointer.

.. _`vxfs_readdir`:

vxfs_readdir
============

.. c:function:: int vxfs_readdir(struct file *fp, struct dir_context *ctx)

    read a directory

    :param struct file \*fp:
        the directory to read

    :param struct dir_context \*ctx:
        *undescribed*

.. _`vxfs_readdir.description`:

Description
-----------

vxfs_readdir fills \ ``retp``\  with directory entries from \ ``fp``\ 
using the VFS supplied callback \ ``filler``\ .

.. _`vxfs_readdir.return`:

Return
------

Zero.

.. This file was automatic generated / don't edit.

