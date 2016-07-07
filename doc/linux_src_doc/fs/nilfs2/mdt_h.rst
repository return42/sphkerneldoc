.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/mdt.h

.. _`nilfs_shadow_map`:

struct nilfs_shadow_map
=======================

.. c:type:: struct nilfs_shadow_map

    shadow mapping of meta data file

.. _`nilfs_shadow_map.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_shadow_map {
        struct nilfs_bmap_store bmap_store;
        struct address_space frozen_data;
        struct address_space frozen_btnodes;
        struct list_head frozen_buffers;
    }

.. _`nilfs_shadow_map.members`:

Members
-------

bmap_store
    shadow copy of bmap state

frozen_data
    shadowed dirty data pages

frozen_btnodes
    shadowed dirty b-tree nodes' pages

frozen_buffers
    list of frozen buffers

.. _`nilfs_mdt_info`:

struct nilfs_mdt_info
=====================

.. c:type:: struct nilfs_mdt_info

    on-memory private data of meta data files

.. _`nilfs_mdt_info.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_mdt_info {
        struct rw_semaphore mi_sem;
        struct blockgroup_lock *mi_bgl;
        unsigned int mi_entry_size;
        unsigned int mi_first_entry_offset;
        unsigned long mi_entries_per_block;
        struct nilfs_palloc_cache *mi_palloc_cache;
        struct nilfs_shadow_map *mi_shadow;
        unsigned long mi_blocks_per_group;
        unsigned long mi_blocks_per_desc_block;
    }

.. _`nilfs_mdt_info.members`:

Members
-------

mi_sem
    reader/writer semaphore for meta data operations

mi_bgl
    per-blockgroup locking

mi_entry_size
    size of an entry

mi_first_entry_offset
    offset to the first entry

mi_entries_per_block
    number of entries in a block

mi_palloc_cache
    persistent object allocator cache

mi_shadow
    shadow of bmap and page caches

mi_blocks_per_group
    number of blocks in a group

mi_blocks_per_desc_block
    number of blocks per descriptor block

.. This file was automatic generated / don't edit.

