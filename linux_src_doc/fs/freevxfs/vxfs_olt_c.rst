.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/freevxfs/vxfs_olt.c

.. _`vxfs_read_olt`:

vxfs_read_olt
=============

.. c:function:: int vxfs_read_olt(struct super_block *sbp, u_long bsize)

    read olt

    :param struct super_block \*sbp:
        superblock of the filesystem

    :param u_long bsize:
        blocksize of the filesystem

.. _`vxfs_read_olt.description`:

Description
-----------

vxfs_read_olt reads the olt of the filesystem described by \ ``sbp``\ 
into main memory and does some basic setup.

.. _`vxfs_read_olt.return`:

Return
------

Zero on success, else a negative error code.

.. This file was automatic generated / don't edit.

