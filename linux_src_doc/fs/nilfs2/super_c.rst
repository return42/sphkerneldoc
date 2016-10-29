.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/super.c

.. _`nilfs_error`:

nilfs_error
===========

.. c:function:: void nilfs_error(struct super_block *sb, const char *function, const char *fmt,  ...)

    report failure condition on a filesystem

    :param struct super_block \*sb:
        *undescribed*

    :param const char \*function:
        *undescribed*

    :param const char \*fmt:
        *undescribed*

    :param ... :
        variable arguments

.. _`nilfs_error.description`:

Description
-----------

\ :c:func:`nilfs_error`\  sets an ERROR_FS flag on the superblock as well as
reporting an error message.  It should be called when NILFS detects
incoherences or defects of meta data on disk.  As for sustainable
errors such as a single-shot I/O error, \ :c:func:`nilfs_warning`\  or the \ :c:func:`printk`\ 
function should be used instead.

The segment constructor must not call this function because it can
kill itself.

.. _`nilfs_cleanup_super`:

nilfs_cleanup_super
===================

.. c:function:: int nilfs_cleanup_super(struct super_block *sb)

    write filesystem state for cleanup

    :param struct super_block \*sb:
        super block instance to be unmounted or degraded to read-only

.. _`nilfs_cleanup_super.description`:

Description
-----------

This function restores state flags in the on-disk super block.
This will set "clean" flag (i.e. NILFS_VALID_FS) unless the
filesystem was not clean previously.

.. _`nilfs_move_2nd_super`:

nilfs_move_2nd_super
====================

.. c:function:: int nilfs_move_2nd_super(struct super_block *sb, loff_t sb2off)

    relocate secondary super block

    :param struct super_block \*sb:
        super block instance

    :param loff_t sb2off:
        new offset of the secondary super block (in bytes)

.. _`nilfs_resize_fs`:

nilfs_resize_fs
===============

.. c:function:: int nilfs_resize_fs(struct super_block *sb, __u64 newsize)

    resize the filesystem

    :param struct super_block \*sb:
        super block instance

    :param __u64 newsize:
        new size of the filesystem (in bytes)

.. _`nilfs_tree_is_busy`:

nilfs_tree_is_busy
==================

.. c:function:: bool nilfs_tree_is_busy(struct dentry *root_dentry)

    try to shrink dentries of a checkpoint

    :param struct dentry \*root_dentry:
        root dentry of the tree to be shrunk

.. _`nilfs_tree_is_busy.description`:

Description
-----------

This function returns true if the tree was in-use.

.. _`nilfs_fill_super`:

nilfs_fill_super
================

.. c:function:: int nilfs_fill_super(struct super_block *sb, void *data, int silent)

    initialize a super block instance

    :param struct super_block \*sb:
        super_block

    :param void \*data:
        mount options

    :param int silent:
        silent mode flag

.. _`nilfs_fill_super.description`:

Description
-----------

This function is called exclusively by nilfs->ns_mount_mutex.
So, the recovery process is protected from other simultaneous mounts.

.. _`nilfs_identify`:

nilfs_identify
==============

.. c:function:: int nilfs_identify(char *data, struct nilfs_super_data *sd)

    pre-read mount options needed to identify mount instance

    :param char \*data:
        mount options

    :param struct nilfs_super_data \*sd:
        nilfs_super_data

.. This file was automatic generated / don't edit.
