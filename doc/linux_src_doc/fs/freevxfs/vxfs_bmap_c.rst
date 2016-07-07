.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/freevxfs/vxfs_bmap.c

.. _`vxfs_bmap_ext4`:

vxfs_bmap_ext4
==============

.. c:function:: daddr_t vxfs_bmap_ext4(struct inode *ip, long bn)

    do bmap for ext4 extents

    :param struct inode \*ip:
        pointer to the inode we do bmap for

    :param long bn:
        *undescribed*

.. _`vxfs_bmap_ext4.description`:

Description
-----------

vxfs_bmap_ext4 performs the bmap operation for inodes with
ext4-style extents (which are much like the traditional UNIX
inode organisation).

.. _`vxfs_bmap_ext4.return`:

Return
------

The physical block number on success, else Zero.

.. _`vxfs_bmap_indir`:

vxfs_bmap_indir
===============

.. c:function:: daddr_t vxfs_bmap_indir(struct inode *ip, long indir, int size, long block)

    recursion for vxfs_bmap_typed

    :param struct inode \*ip:
        pointer to the inode we do bmap for

    :param long indir:
        indirect block we start reading at

    :param int size:
        size of the typed area to search

    :param long block:
        partially result from further searches

.. _`vxfs_bmap_indir.description`:

Description
-----------

vxfs_bmap_indir reads a \ :c:type:`struct vxfs_typed <vxfs_typed>`\  at \ ``indir``\ 
and performs the type-defined action.

.. _`vxfs_bmap_indir.return-value`:

Return Value
------------

The physical block number on success, else Zero.

.. _`vxfs_bmap_indir.note`:

Note
----

Kernelstack is rare.  Unrecurse?

.. _`vxfs_bmap_typed`:

vxfs_bmap_typed
===============

.. c:function:: daddr_t vxfs_bmap_typed(struct inode *ip, long iblock)

    bmap for typed extents

    :param struct inode \*ip:
        pointer to the inode we do bmap for

    :param long iblock:
        logical block

.. _`vxfs_bmap_typed.description`:

Description
-----------

Performs the bmap operation for typed extents.

.. _`vxfs_bmap_typed.return-value`:

Return Value
------------

The physical block number on success, else Zero.

.. _`vxfs_bmap1`:

vxfs_bmap1
==========

.. c:function:: daddr_t vxfs_bmap1(struct inode *ip, long iblock)

    vxfs-internal bmap operation

    :param struct inode \*ip:
        pointer to the inode we do bmap for

    :param long iblock:
        logical block

.. _`vxfs_bmap1.description`:

Description
-----------

vxfs_bmap1 perfoms a logical to physical block mapping
for vxfs-internal purposes.

.. _`vxfs_bmap1.return-value`:

Return Value
------------

The physical block number on success, else Zero.

.. This file was automatic generated / don't edit.

