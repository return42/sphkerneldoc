.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/vfs_super.c

.. _`v9fs_set_super`:

v9fs_set_super
==============

.. c:function:: int v9fs_set_super(struct super_block *s, void *data)

    set the superblock

    :param s:
        super block
    :type s: struct super_block \*

    :param data:
        file system specific data
    :type data: void \*

.. _`v9fs_fill_super`:

v9fs_fill_super
===============

.. c:function:: int v9fs_fill_super(struct super_block *sb, struct v9fs_session_info *v9ses, int flags, void *data)

    populate superblock with info

    :param sb:
        superblock
    :type sb: struct super_block \*

    :param v9ses:
        session information
    :type v9ses: struct v9fs_session_info \*

    :param flags:
        flags propagated from \ :c:func:`v9fs_mount`\ 
    :type flags: int

    :param data:
        *undescribed*
    :type data: void \*

.. _`v9fs_mount`:

v9fs_mount
==========

.. c:function:: struct dentry *v9fs_mount(struct file_system_type *fs_type, int flags, const char *dev_name, void *data)

    mount a superblock

    :param fs_type:
        file system type
    :type fs_type: struct file_system_type \*

    :param flags:
        mount flags
    :type flags: int

    :param dev_name:
        device name that was mounted
    :type dev_name: const char \*

    :param data:
        mount options
    :type data: void \*

.. _`v9fs_kill_super`:

v9fs_kill_super
===============

.. c:function:: void v9fs_kill_super(struct super_block *s)

    Kill Superblock

    :param s:
        superblock
    :type s: struct super_block \*

.. This file was automatic generated / don't edit.

