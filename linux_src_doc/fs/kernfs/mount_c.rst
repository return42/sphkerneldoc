.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/kernfs/mount.c

.. _`kernfs_root_from_sb`:

kernfs_root_from_sb
===================

.. c:function:: struct kernfs_root *kernfs_root_from_sb(struct super_block *sb)

    determine kernfs_root associated with a super_block

    :param struct super_block \*sb:
        the super_block in question

.. _`kernfs_root_from_sb.description`:

Description
-----------

Return the kernfs_root associated with \ ``sb``\ .  If \ ``sb``\  is not a kernfs one,
\ ``NULL``\  is returned.

.. _`kernfs_node_dentry`:

kernfs_node_dentry
==================

.. c:function:: struct dentry *kernfs_node_dentry(struct kernfs_node *kn, struct super_block *sb)

    get a dentry for the given kernfs_node

    :param struct kernfs_node \*kn:
        kernfs_node for which a dentry is needed

    :param struct super_block \*sb:
        the kernfs super_block

.. _`kernfs_super_ns`:

kernfs_super_ns
===============

.. c:function:: const void *kernfs_super_ns(struct super_block *sb)

    determine the namespace tag of a kernfs super_block

    :param struct super_block \*sb:
        super_block of interest

.. _`kernfs_super_ns.description`:

Description
-----------

Return the namespace tag associated with kernfs super_block \ ``sb``\ .

.. _`kernfs_mount_ns`:

kernfs_mount_ns
===============

.. c:function:: struct dentry *kernfs_mount_ns(struct file_system_type *fs_type, int flags, struct kernfs_root *root, unsigned long magic, bool *new_sb_created, const void *ns)

    kernfs mount helper

    :param struct file_system_type \*fs_type:
        file_system_type of the fs being mounted

    :param int flags:
        mount flags specified for the mount

    :param struct kernfs_root \*root:
        kernfs_root of the hierarchy being mounted

    :param unsigned long magic:
        file system specific magic number

    :param bool \*new_sb_created:
        tell the caller if we allocated a new superblock

    :param const void \*ns:
        optional namespace tag of the mount

.. _`kernfs_mount_ns.description`:

Description
-----------

This is to be called from each kernfs user's file_system_type->mount()
implementation, which should pass through the specified \ ``fs_type``\  and
\ ``flags``\ , and specify the hierarchy and namespace tag to mount via \ ``root``\ 
and \ ``ns``\ , respectively.

The return value can be passed to the vfs layer verbatim.

.. _`kernfs_kill_sb`:

kernfs_kill_sb
==============

.. c:function:: void kernfs_kill_sb(struct super_block *sb)

    kill_sb for kernfs

    :param struct super_block \*sb:
        super_block being killed

.. _`kernfs_kill_sb.description`:

Description
-----------

This can be used directly for file_system_type->kill_sb().  If a kernfs
user needs extra cleanup, it can implement its own \ :c:func:`kill_sb`\  and call
this function at the end.

.. _`kernfs_pin_sb`:

kernfs_pin_sb
=============

.. c:function:: struct super_block *kernfs_pin_sb(struct kernfs_root *root, const void *ns)

    try to pin the superblock associated with a kernfs_root

    :param struct kernfs_root \*root:
        *undescribed*

    :param const void \*ns:
        the namespace tag

.. _`kernfs_pin_sb.description`:

Description
-----------

Pin the superblock so the superblock won't be destroyed in subsequent
operations.  This can be used to block ->kill_sb() which may be useful
for kernfs users which dynamically manage superblocks.

Returns NULL if there's no superblock associated to this kernfs_root, or
-EINVAL if the superblock is being freed.

.. This file was automatic generated / don't edit.

