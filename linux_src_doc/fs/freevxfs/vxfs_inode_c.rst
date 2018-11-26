.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/freevxfs/vxfs_inode.c

.. _`vxfs_transmod`:

vxfs_transmod
=============

.. c:function:: umode_t vxfs_transmod(struct vxfs_inode_info *vip)

    mode for a VxFS inode

    :param vip:
        VxFS inode
    :type vip: struct vxfs_inode_info \*

.. _`vxfs_transmod.description`:

Description
-----------

vxfs_transmod returns a Linux mode_t for a given
VxFS inode structure.

.. _`vxfs_blkiget`:

vxfs_blkiget
============

.. c:function:: struct inode *vxfs_blkiget(struct super_block *sbp, u_long extent, ino_t ino)

    find inode based on extent #

    :param sbp:
        superblock of the filesystem we search in
    :type sbp: struct super_block \*

    :param extent:
        number of the extent to search
    :type extent: u_long

    :param ino:
        inode number to search
    :type ino: ino_t

.. _`vxfs_blkiget.description`:

Description
-----------

vxfs_blkiget searches inode \ ``ino``\  in the filesystem described by
\ ``sbp``\  in the extent \ ``extent``\ .
Returns the matching VxFS inode on success, else a NULL pointer.

.. _`vxfs_blkiget.note`:

NOTE
----

While \__vxfs_iget uses the pagecache vxfs_blkiget uses the
buffercache.  This function should not be used outside the
\ :c:func:`read_super`\  method, otherwise the data may be incoherent.

.. _`__vxfs_iget`:

\__vxfs_iget
============

.. c:function:: int __vxfs_iget(struct inode *ilistp, struct vxfs_inode_info *vip, ino_t ino)

    generic find inode facility

    :param ilistp:
        inode list
    :type ilistp: struct inode \*

    :param vip:
        VxFS inode to fill in
    :type vip: struct vxfs_inode_info \*

    :param ino:
        inode number
    :type ino: ino_t

.. _`__vxfs_iget.description`:

Description
-----------

Search the for inode number \ ``ino``\  in the filesystem
described by \ ``sbp``\ .  Use the specified inode table (@ilistp).
Returns the matching inode on success, else an error code.

.. _`vxfs_stiget`:

vxfs_stiget
===========

.. c:function:: struct inode *vxfs_stiget(struct super_block *sbp, ino_t ino)

    find inode using the structural inode list

    :param sbp:
        VFS superblock
    :type sbp: struct super_block \*

    :param ino:
        inode #
    :type ino: ino_t

.. _`vxfs_stiget.description`:

Description
-----------

Find inode \ ``ino``\  in the filesystem described by \ ``sbp``\  using
the structural inode list.
Returns the matching inode on success, else a NULL pointer.

.. _`vxfs_iget`:

vxfs_iget
=========

.. c:function:: struct inode *vxfs_iget(struct super_block *sbp, ino_t ino)

    get an inode

    :param sbp:
        the superblock to get the inode for
    :type sbp: struct super_block \*

    :param ino:
        the number of the inode to get
    :type ino: ino_t

.. _`vxfs_iget.description`:

Description
-----------

vxfs_read_inode creates an inode, reads the disk inode for \ ``ino``\  and fills
in all relevant fields in the new inode.

.. _`vxfs_evict_inode`:

vxfs_evict_inode
================

.. c:function:: void vxfs_evict_inode(struct inode *ip)

    remove inode from main memory

    :param ip:
        inode to discard.
    :type ip: struct inode \*

.. _`vxfs_evict_inode.description`:

Description
-----------

\ :c:func:`vxfs_evict_inode`\  is called on the final iput and frees the private
inode area.

.. This file was automatic generated / don't edit.

