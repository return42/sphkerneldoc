.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/super.c

.. _`__nilfs_error`:

\__nilfs_error
==============

.. c:function:: void __nilfs_error(struct super_block *sb, const char *function, const char *fmt,  ...)

    report failure condition on a filesystem

    :param sb:
        *undescribed*
    :type sb: struct super_block \*

    :param function:
        *undescribed*
    :type function: const char \*

    :param fmt:
        *undescribed*
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`__nilfs_error.description`:

Description
-----------

\__nilfs_error() sets an ERROR_FS flag on the superblock as well as
reporting an error message.  This function should be called when
NILFS detects incoherences or defects of meta data on disk.

This implements the body of \ :c:func:`nilfs_error`\  macro.  Normally,
\ :c:func:`nilfs_error`\  should be used.  As for sustainable errors such as a
single-shot I/O error, \ :c:func:`nilfs_msg`\  should be used instead.

Callers should not add a trailing newline since this will do it.

.. _`nilfs_cleanup_super`:

nilfs_cleanup_super
===================

.. c:function:: int nilfs_cleanup_super(struct super_block *sb)

    write filesystem state for cleanup

    :param sb:
        super block instance to be unmounted or degraded to read-only
    :type sb: struct super_block \*

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

    :param sb:
        super block instance
    :type sb: struct super_block \*

    :param sb2off:
        new offset of the secondary super block (in bytes)
    :type sb2off: loff_t

.. _`nilfs_resize_fs`:

nilfs_resize_fs
===============

.. c:function:: int nilfs_resize_fs(struct super_block *sb, __u64 newsize)

    resize the filesystem

    :param sb:
        super block instance
    :type sb: struct super_block \*

    :param newsize:
        new size of the filesystem (in bytes)
    :type newsize: __u64

.. _`nilfs_tree_is_busy`:

nilfs_tree_is_busy
==================

.. c:function:: bool nilfs_tree_is_busy(struct dentry *root_dentry)

    try to shrink dentries of a checkpoint

    :param root_dentry:
        root dentry of the tree to be shrunk
    :type root_dentry: struct dentry \*

.. _`nilfs_tree_is_busy.description`:

Description
-----------

This function returns true if the tree was in-use.

.. _`nilfs_fill_super`:

nilfs_fill_super
================

.. c:function:: int nilfs_fill_super(struct super_block *sb, void *data, int silent)

    initialize a super block instance

    :param sb:
        super_block
    :type sb: struct super_block \*

    :param data:
        mount options
    :type data: void \*

    :param silent:
        silent mode flag
    :type silent: int

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

    :param data:
        mount options
    :type data: char \*

    :param sd:
        nilfs_super_data
    :type sd: struct nilfs_super_data \*

.. This file was automatic generated / don't edit.

