.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/freevxfs/vxfs_olt.c

.. _`vxfs_read_olt`:

vxfs_read_olt
=============

.. c:function:: int vxfs_read_olt(struct super_block *sbp, u_long bsize)

    read olt

    :param sbp:
        superblock of the filesystem
    :type sbp: struct super_block \*

    :param bsize:
        blocksize of the filesystem
    :type bsize: u_long

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

