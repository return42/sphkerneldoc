.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/btree.c

.. _`nilfs_btree_node_broken`:

nilfs_btree_node_broken
=======================

.. c:function:: int nilfs_btree_node_broken(const struct nilfs_btree_node *node, size_t size, struct inode *inode, sector_t blocknr)

    verify consistency of btree node

    :param const struct nilfs_btree_node \*node:
        btree node block to be examined

    :param size_t size:
        node size (in bytes)

    :param struct inode \*inode:
        host inode of btree

    :param sector_t blocknr:
        block number

.. _`nilfs_btree_node_broken.return-value`:

Return Value
------------

If node is broken, 1 is returned. Otherwise, 0 is returned.

.. _`nilfs_btree_root_broken`:

nilfs_btree_root_broken
=======================

.. c:function:: int nilfs_btree_root_broken(const struct nilfs_btree_node *node, struct inode *inode)

    verify consistency of btree root node

    :param const struct nilfs_btree_node \*node:
        btree root node to be examined

    :param struct inode \*inode:
        host inode of btree

.. _`nilfs_btree_root_broken.return-value`:

Return Value
------------

If node is broken, 1 is returned. Otherwise, 0 is returned.

.. _`nilfs_btree_get_next_key`:

nilfs_btree_get_next_key
========================

.. c:function:: int nilfs_btree_get_next_key(const struct nilfs_bmap *btree, const struct nilfs_btree_path *path, int minlevel, __u64 *nextkey)

    get next valid key from btree path array

    :param const struct nilfs_bmap \*btree:
        bmap struct of btree

    :param const struct nilfs_btree_path \*path:
        array of nilfs_btree_path struct

    :param int minlevel:
        start level

    :param __u64 \*nextkey:
        place to store the next valid key

.. _`nilfs_btree_get_next_key.return-value`:

Return Value
------------

If a next key was found, 0 is returned. Otherwise,
-ENOENT is returned.

.. _`nilfs_btree_convert_and_insert`:

nilfs_btree_convert_and_insert
==============================

.. c:function:: int nilfs_btree_convert_and_insert(struct nilfs_bmap *btree, __u64 key, __u64 ptr, const __u64 *keys, const __u64 *ptrs, int n)

    :param struct nilfs_bmap \*btree:
        *undescribed*

    :param __u64 key:
        *undescribed*

    :param __u64 ptr:
        *undescribed*

    :param const __u64 \*keys:
        *undescribed*

    :param const __u64 \*ptrs:
        *undescribed*

    :param int n:
        *undescribed*

.. This file was automatic generated / don't edit.

