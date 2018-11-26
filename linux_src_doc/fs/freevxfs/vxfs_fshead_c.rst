.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/freevxfs/vxfs_fshead.c

.. _`vxfs_getfsh`:

vxfs_getfsh
===========

.. c:function:: struct vxfs_fsh *vxfs_getfsh(struct inode *ip, int which)

    read fileset header into memory

    :param ip:
        the (fake) fileset header inode
    :type ip: struct inode \*

    :param which:
        0 for the structural, 1 for the primary fsh.
    :type which: int

.. _`vxfs_getfsh.description`:

Description
-----------

vxfs_getfsh reads either the structural or primary fileset header
described by \ ``ip``\  into memory.

.. _`vxfs_getfsh.return`:

Return
------

The fileset header structure on success, else Zero.

.. _`vxfs_read_fshead`:

vxfs_read_fshead
================

.. c:function:: int vxfs_read_fshead(struct super_block *sbp)

    read the fileset headers

    :param sbp:
        superblock to which the fileset belongs
    :type sbp: struct super_block \*

.. _`vxfs_read_fshead.description`:

Description
-----------

vxfs_read_fshead will fill the inode and structural inode list in \ ``sb``\ .

.. _`vxfs_read_fshead.return`:

Return
------

Zero on success, else a negative error code (-EINVAL).

.. This file was automatic generated / don't edit.

