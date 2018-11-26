.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/kthread.c

.. _`ecryptfs_threadfn`:

ecryptfs_threadfn
=================

.. c:function:: int ecryptfs_threadfn(void *ignored)

    :param ignored:
        ignored
    :type ignored: void \*

.. _`ecryptfs_threadfn.description`:

Description
-----------

The eCryptfs kernel thread that has the responsibility of getting
the lower file with RW permissions.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_privileged_open`:

ecryptfs_privileged_open
========================

.. c:function:: int ecryptfs_privileged_open(struct file **lower_file, struct dentry *lower_dentry, struct vfsmount *lower_mnt, const struct cred *cred)

    :param lower_file:
        Result of dentry_open by root on lower dentry
    :type lower_file: struct file \*\*

    :param lower_dentry:
        Lower dentry for file to open
    :type lower_dentry: struct dentry \*

    :param lower_mnt:
        Lower vfsmount for file to open
    :type lower_mnt: struct vfsmount \*

    :param cred:
        *undescribed*
    :type cred: const struct cred \*

.. _`ecryptfs_privileged_open.description`:

Description
-----------

This function gets a r/w file opened against the lower dentry.

Returns zero on success; non-zero otherwise

.. This file was automatic generated / don't edit.

