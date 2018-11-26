.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfs/dir.c

.. _`nfs_force_lookup_revalidate`:

nfs_force_lookup_revalidate
===========================

.. c:function:: void nfs_force_lookup_revalidate(struct inode *dir)

    Mark the directory as having changed \ ``dir``\  - pointer to directory inode

    :param dir:
        *undescribed*
    :type dir: struct inode \*

.. _`nfs_force_lookup_revalidate.description`:

Description
-----------

This forces the revalidation code in \ :c:func:`nfs_lookup_revalidate`\  to do a
full lookup on all child dentries of 'dir' whenever a change occurs
on the server that might have invalidated our dcache.

The caller should be holding dir->i_lock

.. This file was automatic generated / don't edit.

