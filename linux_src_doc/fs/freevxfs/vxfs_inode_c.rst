.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/freevxfs/vxfs_inode.c

.. _`vxfs_blkiget`:

vxfs_blkiget
============

.. c:function:: struct vxfs_inode_info *vxfs_blkiget(struct super_block *sbp, u_long extent, ino_t ino)

    find inode based on extent #

    :param struct super_block \*sbp:
        superblock of the filesystem we search in

    :param u_long extent:
        number of the extent to search

    :param ino_t ino:
        inode number to search

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

__vxfs_iget
===========

.. c:function:: struct vxfs_inode_info *__vxfs_iget(ino_t ino, struct inode *ilistp)

    generic find inode facility

    :param ino_t ino:
        inode number

    :param struct inode \*ilistp:
        inode list

.. _`__vxfs_iget.description`:

Description
-----------

Search the for inode number \ ``ino``\  in the filesystem
described by \ ``sbp``\ .  Use the specified inode table (\ ``ilistp``\ ).
Returns the matching VxFS inode on success, else an error code.

.. _`vxfs_stiget`:

vxfs_stiget
===========

.. c:function:: struct vxfs_inode_info *vxfs_stiget(struct super_block *sbp, ino_t ino)

    find inode using the structural inode list

    :param struct super_block \*sbp:
        VFS superblock

    :param ino_t ino:
        inode #

.. _`vxfs_stiget.description`:

Description
-----------

Find inode \ ``ino``\  in the filesystem described by \ ``sbp``\  using
the structural inode list.
Returns the matching VxFS inode on success, else a NULL pointer.

.. _`vxfs_transmod`:

vxfs_transmod
=============

.. c:function:: umode_t vxfs_transmod(struct vxfs_inode_info *vip)

    mode for a VxFS inode

    :param struct vxfs_inode_info \*vip:
        VxFS inode

.. _`vxfs_transmod.description`:

Description
-----------

vxfs_transmod returns a Linux mode_t for a given
VxFS inode structure.

.. _`vxfs_iinit`:

vxfs_iinit
==========

.. c:function:: void vxfs_iinit(struct inode *ip, struct vxfs_inode_info *vip)

    helper to fill inode fields

    :param struct inode \*ip:
        VFS inode

    :param struct vxfs_inode_info \*vip:
        VxFS inode

.. _`vxfs_iinit.description`:

Description
-----------

vxfs_instino is a helper function to fill in all relevant
fields in \ ``ip``\  from \ ``vip``\ .

.. _`vxfs_get_fake_inode`:

vxfs_get_fake_inode
===================

.. c:function:: struct inode *vxfs_get_fake_inode(struct super_block *sbp, struct vxfs_inode_info *vip)

    get fake inode structure

    :param struct super_block \*sbp:
        filesystem superblock

    :param struct vxfs_inode_info \*vip:
        fspriv inode

.. _`vxfs_get_fake_inode.description`:

Description
-----------

vxfs_fake_inode gets a fake inode (not in the inode hash) for a
superblock, vxfs_inode pair.
Returns the filled VFS inode.

.. _`vxfs_put_fake_inode`:

vxfs_put_fake_inode
===================

.. c:function:: void vxfs_put_fake_inode(struct inode *ip)

    free faked inode \*ip:                 VFS inode

    :param struct inode \*ip:
        *undescribed*

.. _`vxfs_put_fake_inode.description`:

Description
-----------

vxfs_put_fake_inode frees all data associated with \ ``ip``\ .

.. _`vxfs_iget`:

vxfs_iget
=========

.. c:function:: struct inode *vxfs_iget(struct super_block *sbp, ino_t ino)

    get an inode

    :param struct super_block \*sbp:
        the superblock to get the inode for

    :param ino_t ino:
        the number of the inode to get

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

    :param struct inode \*ip:
        inode to discard.

.. _`vxfs_evict_inode.description`:

Description
-----------

\ :c:func:`vxfs_evict_inode`\  is called on the final iput and frees the private
inode area.

.. This file was automatic generated / don't edit.

