.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/freevxfs/vxfs_super.c

.. _`vxfs_put_super`:

vxfs_put_super
==============

.. c:function:: void vxfs_put_super(struct super_block *sbp)

    free superblock resources

    :param sbp:
        VFS superblock.
    :type sbp: struct super_block \*

.. _`vxfs_put_super.description`:

Description
-----------

vxfs_put_super frees all resources allocated for \ ``sbp``\ 
after the last instance of the filesystem is unmounted.

.. _`vxfs_statfs`:

vxfs_statfs
===========

.. c:function:: int vxfs_statfs(struct dentry *dentry, struct kstatfs *bufp)

    get filesystem information

    :param dentry:
        VFS dentry to locate superblock
    :type dentry: struct dentry \*

    :param bufp:
        output buffer
    :type bufp: struct kstatfs \*

.. _`vxfs_statfs.description`:

Description
-----------

vxfs_statfs fills the statfs buffer \ ``bufp``\  with information
about the filesystem described by \ ``dentry``\ .

.. _`vxfs_statfs.return`:

Return
------

Zero.

.. _`vxfs_statfs.locking`:

Locking
-------

No locks held.

.. _`vxfs_statfs.notes`:

Notes
-----

This is everything but complete...

.. _`vxfs_fill_super`:

vxfs_fill_super
===============

.. c:function:: int vxfs_fill_super(struct super_block *sbp, void *dp, int silent)

    read superblock into memory and initialize filesystem

    :param sbp:
        VFS superblock (to fill)
    :type sbp: struct super_block \*

    :param dp:
        fs private mount data
    :type dp: void \*

    :param silent:
        do not complain loudly when sth is wrong
    :type silent: int

.. _`vxfs_fill_super.description`:

Description
-----------

We are called on the first mount of a filesystem to read the
superblock into memory and do some basic setup.

.. _`vxfs_fill_super.return`:

Return
------

The superblock on success, else \ ``NULL``\ .

.. _`vxfs_fill_super.locking`:

Locking
-------

We are under \ ``sbp->s_lock``\ .

.. This file was automatic generated / don't edit.

