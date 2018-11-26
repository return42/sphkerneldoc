.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/kernfs/inode.c

.. _`kernfs_setattr`:

kernfs_setattr
==============

.. c:function:: int kernfs_setattr(struct kernfs_node *kn, const struct iattr *iattr)

    set iattr on a node

    :param kn:
        target node
    :type kn: struct kernfs_node \*

    :param iattr:
        iattr to set
    :type iattr: const struct iattr \*

.. _`kernfs_setattr.description`:

Description
-----------

Returns 0 on success, -errno on failure.

.. _`kernfs_get_inode`:

kernfs_get_inode
================

.. c:function:: struct inode *kernfs_get_inode(struct super_block *sb, struct kernfs_node *kn)

    get inode for kernfs_node

    :param sb:
        super block
    :type sb: struct super_block \*

    :param kn:
        kernfs_node to allocate inode for
    :type kn: struct kernfs_node \*

.. _`kernfs_get_inode.description`:

Description
-----------

Get inode for \ ``kn``\ .  If such inode doesn't exist, a new inode is
allocated and basics are initialized.  New inode is returned
locked.

.. _`kernfs_get_inode.locking`:

LOCKING
-------

Kernel thread context (may sleep).

.. _`kernfs_get_inode.return`:

Return
------

Pointer to allocated inode on success, NULL on failure.

.. This file was automatic generated / don't edit.

