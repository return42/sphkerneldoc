.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/9p/vfs_super.c

.. _`v9fs_set_super`:

v9fs_set_super
==============

.. c:function:: int v9fs_set_super(struct super_block *s, void *data)

    set the superblock

    :param struct super_block \*s:
        super block

    :param void \*data:
        file system specific data

.. _`v9fs_fill_super`:

v9fs_fill_super
===============

.. c:function:: void v9fs_fill_super(struct super_block *sb, struct v9fs_session_info *v9ses, int flags, void *data)

    populate superblock with info

    :param struct super_block \*sb:
        superblock

    :param struct v9fs_session_info \*v9ses:
        session information

    :param int flags:
        flags propagated from \ :c:func:`v9fs_mount`\ 

    :param void \*data:
        *undescribed*

.. _`v9fs_mount`:

v9fs_mount
==========

.. c:function:: struct dentry *v9fs_mount(struct file_system_type *fs_type, int flags, const char *dev_name, void *data)

    mount a superblock

    :param struct file_system_type \*fs_type:
        file system type

    :param int flags:
        mount flags

    :param const char \*dev_name:
        device name that was mounted

    :param void \*data:
        mount options

.. _`v9fs_kill_super`:

v9fs_kill_super
===============

.. c:function:: void v9fs_kill_super(struct super_block *s)

    Kill Superblock

    :param struct super_block \*s:
        superblock

.. This file was automatic generated / don't edit.

