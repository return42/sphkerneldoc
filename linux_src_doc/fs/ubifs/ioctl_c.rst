.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ubifs/ioctl.c

.. _`ubifs_set_inode_flags`:

ubifs_set_inode_flags
=====================

.. c:function:: void ubifs_set_inode_flags(struct inode *inode)

    set VFS inode flags.

    :param inode:
        VFS inode to set flags for
    :type inode: struct inode \*

.. _`ubifs_set_inode_flags.description`:

Description
-----------

This function propagates flags from UBIFS inode object to VFS inode object.

.. This file was automatic generated / don't edit.

