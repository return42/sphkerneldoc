.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/ntfs.h

.. _`ntfs_sb`:

NTFS_SB
=======

.. c:function:: ntfs_volume *NTFS_SB(struct super_block *sb)

    return the ntfs volume given a vfs super block

    :param sb:
        VFS super block
    :type sb: struct super_block \*

.. _`ntfs_sb.description`:

Description
-----------

\ :c:func:`NTFS_SB`\  returns the ntfs volume associated with the VFS super block \ ``sb``\ .

.. This file was automatic generated / don't edit.

