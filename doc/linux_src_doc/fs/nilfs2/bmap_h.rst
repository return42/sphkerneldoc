.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/bmap.h

.. _`nilfs_bmap_ptr_req`:

union nilfs_bmap_ptr_req
========================

.. c:type:: struct nilfs_bmap_ptr_req

    request for bmap ptr

.. _`nilfs_bmap_ptr_req.definition`:

Definition
----------

.. code-block:: c

    union nilfs_bmap_ptr_req {
        __u64 bpr_ptr;
        struct nilfs_palloc_req bpr_req;
    }

.. _`nilfs_bmap_ptr_req.members`:

Members
-------

bpr_ptr
    bmap pointer

bpr_req
    request for persistent allocator

.. _`nilfs_bmap_stats`:

struct nilfs_bmap_stats
=======================

.. c:type:: struct nilfs_bmap_stats

    bmap statistics

.. _`nilfs_bmap_stats.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_bmap_stats {
        unsigned int bs_nblocks;
    }

.. _`nilfs_bmap_stats.members`:

Members
-------

bs_nblocks
    number of blocks created or deleted

.. _`nilfs_bmap_operations`:

struct nilfs_bmap_operations
============================

.. c:type:: struct nilfs_bmap_operations

    bmap operation table

.. _`nilfs_bmap_operations.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_bmap_operations {
        int (*bop_lookup)(const struct nilfs_bmap *, __u64, int, __u64 *);
        int (*bop_lookup_contig)(const struct nilfs_bmap *, __u64, __u64 *,unsigned int);
        int (*bop_insert)(struct nilfs_bmap *, __u64, __u64);
        int (*bop_delete)(struct nilfs_bmap *, __u64);
        void (*bop_clear)(struct nilfs_bmap *);
        int (*bop_propagate)(struct nilfs_bmap *, struct buffer_head *);
        void (*bop_lookup_dirty_buffers)(struct nilfs_bmap *,struct list_head *);
        int (*bop_assign)(struct nilfs_bmap *,struct buffer_head **,sector_t,union nilfs_binfo *);
        int (*bop_mark)(struct nilfs_bmap *, __u64, int);
        int (*bop_seek_key)(const struct nilfs_bmap *, __u64, __u64 *);
        int (*bop_last_key)(const struct nilfs_bmap *, __u64 *);
        int (*bop_check_insert)(const struct nilfs_bmap *, __u64);
        int (*bop_check_delete)(struct nilfs_bmap *, __u64);
        int (*bop_gather_data)(struct nilfs_bmap *, __u64 *, __u64 *, int);
    }

.. _`nilfs_bmap_operations.members`:

Members
-------

bop_lookup
    *undescribed*

bop_lookup_contig
    *undescribed*

bop_insert
    *undescribed*

bop_delete
    *undescribed*

bop_clear
    *undescribed*

bop_propagate
    *undescribed*

bop_lookup_dirty_buffers
    *undescribed*

bop_assign
    *undescribed*

bop_mark
    *undescribed*

bop_seek_key
    *undescribed*

bop_last_key
    *undescribed*

bop_check_insert
    *undescribed*

bop_check_delete
    *undescribed*

bop_gather_data
    *undescribed*

.. _`nilfs_bmap`:

struct nilfs_bmap
=================

.. c:type:: struct nilfs_bmap

    bmap structure

.. _`nilfs_bmap.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_bmap {
        union b_u;
        struct rw_semaphore b_sem;
        struct inode *b_inode;
        const struct nilfs_bmap_operations *b_ops;
        __u64 b_last_allocated_key;
        __u64 b_last_allocated_ptr;
        int b_ptr_type;
        int b_state;
        __u16 b_nchildren_per_block;
    }

.. _`nilfs_bmap.members`:

Members
-------

b_u
    raw data

b_sem
    semaphore

b_inode
    owner of bmap

b_ops
    bmap operation table

b_last_allocated_key
    last allocated key for data block

b_last_allocated_ptr
    last allocated ptr for data block

b_ptr_type
    pointer type

b_state
    state

b_nchildren_per_block
    maximum number of child nodes for non-root nodes

.. _`nilfs_bmap_store`:

struct nilfs_bmap_store
=======================

.. c:type:: struct nilfs_bmap_store

    shadow copy of bmap state

.. _`nilfs_bmap_store.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_bmap_store {
        __le64 data[NILFS_BMAP_SIZE / sizeof(__le64)];
        __u64 last_allocated_key;
        __u64 last_allocated_ptr;
        int state;
    }

.. _`nilfs_bmap_store.members`:

Members
-------

data
    cached raw block mapping of on-disk inode

last_allocated_key
    cached value of last allocated key for data block

last_allocated_ptr
    cached value of last allocated ptr for data block

state
    cached value of state field of bmap structure

.. This file was automatic generated / don't edit.

