.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ext4/ioctl.c

.. _`memswap`:

memswap
=======

.. c:function:: void memswap(void *a, void *b, size_t len)

    :param a:
        pointer to first memory area
    :type a: void \*

    :param b:
        pointer to second memory area
    :type b: void \*

    :param len:
        number of bytes to swap
    :type len: size_t

.. _`swap_inode_data`:

swap_inode_data
===============

.. c:function:: void swap_inode_data(struct inode *inode1, struct inode *inode2)

    This function is used for the primary swap between inode1 and inode2 and also to revert this primary swap in case of errors.

    :param inode1:
        pointer to first inode
    :type inode1: struct inode \*

    :param inode2:
        pointer to second inode
    :type inode2: struct inode \*

.. _`swap_inode_data.description`:

Description
-----------

Therefore you have to make sure, that calling this method twice
will revert all changes.

.. _`swap_inode_boot_loader`:

swap_inode_boot_loader
======================

.. c:function:: long swap_inode_boot_loader(struct super_block *sb, struct inode *inode)

    EXT4_BOOT_LOADER_INO. It will basically swap i_data and all other important fields of the inodes.

    :param sb:
        the super block of the filesystem
    :type sb: struct super_block \*

    :param inode:
        the inode to swap with EXT4_BOOT_LOADER_INO
    :type inode: struct inode \*

.. This file was automatic generated / don't edit.

