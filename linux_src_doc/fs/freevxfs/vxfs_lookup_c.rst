.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/freevxfs/vxfs_lookup.c

.. _`vxfs_find_entry`:

vxfs_find_entry
===============

.. c:function:: struct vxfs_direct *vxfs_find_entry(struct inode *ip, struct dentry *dp, struct page **ppp)

    find a mathing directory entry for a dentry

    :param ip:
        directory inode
    :type ip: struct inode \*

    :param dp:
        dentry for which we want to find a direct
    :type dp: struct dentry \*

    :param ppp:
        gets filled with the page the return value sits in
    :type ppp: struct page \*\*

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

    :param dip:
        directory to search in
    :type dip: struct inode \*

    :param dp:
        dentry we search for
    :type dp: struct dentry \*

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

    :param dip:
        dir in which we lookup
    :type dip: struct inode \*

    :param dp:
        dentry we lookup
    :type dp: struct dentry \*

    :param flags:
        lookup flags
    :type flags: unsigned int

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

    :param fp:
        the directory to read
    :type fp: struct file \*

    :param ctx:
        *undescribed*
    :type ctx: struct dir_context \*

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

