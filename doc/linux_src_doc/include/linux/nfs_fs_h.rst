.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/nfs_fs.h

.. _`nfs_save_change_attribute`:

nfs_save_change_attribute
=========================

.. c:function:: unsigned long nfs_save_change_attribute(struct inode *dir)

    Returns the inode attribute change cookie \ ``dir``\  - pointer to parent directory inode The "change attribute" is updated every time we finish an operation that will result in a metadata change on the server.

    :param struct inode \*dir:
        *undescribed*

.. _`nfs_verify_change_attribute`:

nfs_verify_change_attribute
===========================

.. c:function:: int nfs_verify_change_attribute(struct inode *dir, unsigned long chattr)

    Detects NFS remote directory changes \ ``dir``\  - pointer to parent directory inode \ ``chattr``\  - previously saved change attribute Return "false" if the verifiers doesn't match the change attribute. This would usually indicate that the directory contents have changed on the server, and that any dentries need revalidating.

    :param struct inode \*dir:
        *undescribed*

    :param unsigned long chattr:
        *undescribed*

.. This file was automatic generated / don't edit.

