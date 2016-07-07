.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/include/linux/libcfs/libcfs_hash.h

.. _`cfs_hash_keycmp`:

cfs_hash_keycmp
===============

.. c:function:: int cfs_hash_keycmp(struct cfs_hash *hs, const void *key, struct hlist_node *hnode)

    :param struct cfs_hash \*hs:
        *undescribed*

    :param const void \*key:
        *undescribed*

    :param struct hlist_node \*hnode:
        *undescribed*

.. _`cfs_hash_bd_get`:

cfs_hash_bd_get
===============

.. c:function:: void cfs_hash_bd_get(struct cfs_hash *hs, const void *key, struct cfs_hash_bd *bd)

    bucket descriptor), they are normally for hash-table without rehash

    :param struct cfs_hash \*hs:
        *undescribed*

    :param const void \*key:
        *undescribed*

    :param struct cfs_hash_bd \*bd:
        *undescribed*

.. _`cfs_hash_dual_bd_get`:

cfs_hash_dual_bd_get
====================

.. c:function:: void cfs_hash_dual_bd_get(struct cfs_hash *hs, const void *key, struct cfs_hash_bd *bds)

    bucket descriptor), they are safe for hash-table with rehash

    :param struct cfs_hash \*hs:
        *undescribed*

    :param const void \*key:
        *undescribed*

    :param struct cfs_hash_bd \*bds:
        *undescribed*

.. This file was automatic generated / don't edit.

