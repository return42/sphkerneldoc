.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/notify/inode_mark.c

.. _`fsnotify_unmount_inodes`:

fsnotify_unmount_inodes
=======================

.. c:function:: void fsnotify_unmount_inodes(struct super_block *sb)

    an sb is unmounting.  handle any watched inodes.

    :param struct super_block \*sb:
        superblock being unmounted.

.. _`fsnotify_unmount_inodes.description`:

Description
-----------

Called during unmount with no locks held, so needs to be safe against
concurrent modifiers. We temporarily drop sb->s_inode_list_lock and CAN block.

.. This file was automatic generated / don't edit.

