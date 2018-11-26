.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/btree.c

.. _`nilfs_btree_node_broken`:

nilfs_btree_node_broken
=======================

.. c:function:: int nilfs_btree_node_broken(const struct nilfs_btree_node *node, size_t size, struct inode *inode, sector_t blocknr)

    verify consistency of btree node

    :param node:
        btree node block to be examined
    :type node: const struct nilfs_btree_node \*

    :param size:
        node size (in bytes)
    :type size: size_t

    :param inode:
        host inode of btree
    :type inode: struct inode \*

    :param blocknr:
        block number
    :type blocknr: sector_t

.. _`nilfs_btree_node_broken.return-value`:

Return Value
------------

If node is broken, 1 is returned. Otherwise, 0 is returned.

.. _`nilfs_btree_root_broken`:

nilfs_btree_root_broken
=======================

.. c:function:: int nilfs_btree_root_broken(const struct nilfs_btree_node *node, struct inode *inode)

    verify consistency of btree root node

    :param node:
        btree root node to be examined
    :type node: const struct nilfs_btree_node \*

    :param inode:
        host inode of btree
    :type inode: struct inode \*

.. _`nilfs_btree_root_broken.return-value`:

Return Value
------------

If node is broken, 1 is returned. Otherwise, 0 is returned.

.. _`nilfs_btree_get_next_key`:

nilfs_btree_get_next_key
========================

.. c:function:: int nilfs_btree_get_next_key(const struct nilfs_bmap *btree, const struct nilfs_btree_path *path, int minlevel, __u64 *nextkey)

    get next valid key from btree path array

    :param btree:
        bmap struct of btree
    :type btree: const struct nilfs_bmap \*

    :param path:
        array of nilfs_btree_path struct
    :type path: const struct nilfs_btree_path \*

    :param minlevel:
        start level
    :type minlevel: int

    :param nextkey:
        place to store the next valid key
    :type nextkey: __u64 \*

.. _`nilfs_btree_get_next_key.return-value`:

Return Value
------------

If a next key was found, 0 is returned. Otherwise,
-ENOENT is returned.

.. _`nilfs_btree_convert_and_insert`:

nilfs_btree_convert_and_insert
==============================

.. c:function:: int nilfs_btree_convert_and_insert(struct nilfs_bmap *btree, __u64 key, __u64 ptr, const __u64 *keys, const __u64 *ptrs, int n)

    :param btree:
        *undescribed*
    :type btree: struct nilfs_bmap \*

    :param key:
        *undescribed*
    :type key: __u64

    :param ptr:
        *undescribed*
    :type ptr: __u64

    :param keys:
        *undescribed*
    :type keys: const __u64 \*

    :param ptrs:
        *undescribed*
    :type ptrs: const __u64 \*

    :param n:
        *undescribed*
    :type n: int

.. This file was automatic generated / don't edit.

