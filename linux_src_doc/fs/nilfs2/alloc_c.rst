.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/alloc.c

.. _`nilfs_palloc_groups_per_desc_block`:

nilfs_palloc_groups_per_desc_block
==================================

.. c:function:: unsigned long nilfs_palloc_groups_per_desc_block(const struct inode *inode)

    get the number of groups that a group descriptor block can maintain

    :param const struct inode \*inode:
        inode of metadata file using this allocator

.. _`nilfs_palloc_groups_count`:

nilfs_palloc_groups_count
=========================

.. c:function:: unsigned long nilfs_palloc_groups_count(const struct inode *inode)

    get maximum number of groups

    :param const struct inode \*inode:
        inode of metadata file using this allocator

.. _`nilfs_palloc_init_blockgroup`:

nilfs_palloc_init_blockgroup
============================

.. c:function:: int nilfs_palloc_init_blockgroup(struct inode *inode, unsigned int entry_size)

    initialize private variables for allocator

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param unsigned int entry_size:
        size of the persistent object

.. _`nilfs_palloc_group`:

nilfs_palloc_group
==================

.. c:function:: unsigned long nilfs_palloc_group(const struct inode *inode, __u64 nr, unsigned long *offset)

    get group number and offset from an entry number

    :param const struct inode \*inode:
        inode of metadata file using this allocator

    :param __u64 nr:
        serial number of the entry (e.g. inode number)

    :param unsigned long \*offset:
        pointer to store offset number in the group

.. _`nilfs_palloc_desc_blkoff`:

nilfs_palloc_desc_blkoff
========================

.. c:function:: unsigned long nilfs_palloc_desc_blkoff(const struct inode *inode, unsigned long group)

    get block offset of a group descriptor block

    :param const struct inode \*inode:
        inode of metadata file using this allocator

    :param unsigned long group:
        group number

.. _`nilfs_palloc_desc_blkoff.description`:

Description
-----------

nilfs_palloc_desc_blkoff() returns block offset of the descriptor
block which contains a descriptor of the specified group.

.. _`nilfs_palloc_bitmap_blkoff`:

nilfs_palloc_bitmap_blkoff
==========================

.. c:function:: unsigned long nilfs_palloc_bitmap_blkoff(const struct inode *inode, unsigned long group)

    get block offset of a bitmap block

    :param const struct inode \*inode:
        inode of metadata file using this allocator

    :param unsigned long group:
        group number

.. _`nilfs_palloc_bitmap_blkoff.description`:

Description
-----------

nilfs_palloc_bitmap_blkoff() returns block offset of the bitmap
block used to allocate/deallocate entries in the specified group.

.. _`nilfs_palloc_group_desc_nfrees`:

nilfs_palloc_group_desc_nfrees
==============================

.. c:function:: unsigned long nilfs_palloc_group_desc_nfrees(const struct nilfs_palloc_group_desc *desc, spinlock_t *lock)

    get the number of free entries in a group

    :param const struct nilfs_palloc_group_desc \*desc:
        pointer to descriptor structure for the group

    :param spinlock_t \*lock:
        spin lock protecting \ ``desc``\ 

.. _`nilfs_palloc_group_desc_add_entries`:

nilfs_palloc_group_desc_add_entries
===================================

.. c:function:: u32 nilfs_palloc_group_desc_add_entries(struct nilfs_palloc_group_desc *desc, spinlock_t *lock, u32 n)

    adjust count of free entries

    :param struct nilfs_palloc_group_desc \*desc:
        pointer to descriptor structure for the group

    :param spinlock_t \*lock:
        spin lock protecting \ ``desc``\ 

    :param u32 n:
        delta to be added

.. _`nilfs_palloc_entry_blkoff`:

nilfs_palloc_entry_blkoff
=========================

.. c:function:: unsigned long nilfs_palloc_entry_blkoff(const struct inode *inode, __u64 nr)

    get block offset of an entry block

    :param const struct inode \*inode:
        inode of metadata file using this allocator

    :param __u64 nr:
        serial number of the entry (e.g. inode number)

.. _`nilfs_palloc_desc_block_init`:

nilfs_palloc_desc_block_init
============================

.. c:function:: void nilfs_palloc_desc_block_init(struct inode *inode, struct buffer_head *bh, void *kaddr)

    initialize buffer of a group descriptor block

    :param struct inode \*inode:
        inode of metadata file

    :param struct buffer_head \*bh:
        buffer head of the buffer to be initialized

    :param void \*kaddr:
        kernel address mapped for the page including the buffer

.. _`nilfs_palloc_delete_block`:

nilfs_palloc_delete_block
=========================

.. c:function:: int nilfs_palloc_delete_block(struct inode *inode, unsigned long blkoff, struct nilfs_bh_assoc *prev, spinlock_t *lock)

    delete a block on the persistent allocator file

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param unsigned long blkoff:
        block offset

    :param struct nilfs_bh_assoc \*prev:
        nilfs_bh_assoc struct of the last used buffer

    :param spinlock_t \*lock:
        spin lock protecting \ ``prev``\ 

.. _`nilfs_palloc_get_desc_block`:

nilfs_palloc_get_desc_block
===========================

.. c:function:: int nilfs_palloc_get_desc_block(struct inode *inode, unsigned long group, int create, struct buffer_head **bhp)

    get buffer head of a group descriptor block

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param unsigned long group:
        group number

    :param int create:
        create flag

    :param struct buffer_head \*\*bhp:
        pointer to store the resultant buffer head

.. _`nilfs_palloc_get_bitmap_block`:

nilfs_palloc_get_bitmap_block
=============================

.. c:function:: int nilfs_palloc_get_bitmap_block(struct inode *inode, unsigned long group, int create, struct buffer_head **bhp)

    get buffer head of a bitmap block

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param unsigned long group:
        group number

    :param int create:
        create flag

    :param struct buffer_head \*\*bhp:
        pointer to store the resultant buffer head

.. _`nilfs_palloc_delete_bitmap_block`:

nilfs_palloc_delete_bitmap_block
================================

.. c:function:: int nilfs_palloc_delete_bitmap_block(struct inode *inode, unsigned long group)

    delete a bitmap block

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param unsigned long group:
        group number

.. _`nilfs_palloc_get_entry_block`:

nilfs_palloc_get_entry_block
============================

.. c:function:: int nilfs_palloc_get_entry_block(struct inode *inode, __u64 nr, int create, struct buffer_head **bhp)

    get buffer head of an entry block

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param __u64 nr:
        serial number of the entry (e.g. inode number)

    :param int create:
        create flag

    :param struct buffer_head \*\*bhp:
        pointer to store the resultant buffer head

.. _`nilfs_palloc_delete_entry_block`:

nilfs_palloc_delete_entry_block
===============================

.. c:function:: int nilfs_palloc_delete_entry_block(struct inode *inode, __u64 nr)

    delete an entry block

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param __u64 nr:
        serial number of the entry

.. _`nilfs_palloc_block_get_group_desc`:

nilfs_palloc_block_get_group_desc
=================================

.. c:function:: struct nilfs_palloc_group_desc *nilfs_palloc_block_get_group_desc(const struct inode *inode, unsigned long group, const struct buffer_head *bh, void *kaddr)

    get kernel address of a group descriptor

    :param const struct inode \*inode:
        inode of metadata file using this allocator

    :param unsigned long group:
        group number

    :param const struct buffer_head \*bh:
        buffer head of the buffer storing the group descriptor block

    :param void \*kaddr:
        kernel address mapped for the page including the buffer

.. _`nilfs_palloc_block_get_entry`:

nilfs_palloc_block_get_entry
============================

.. c:function:: void *nilfs_palloc_block_get_entry(const struct inode *inode, __u64 nr, const struct buffer_head *bh, void *kaddr)

    get kernel address of an entry

    :param const struct inode \*inode:
        inode of metadata file using this allocator

    :param __u64 nr:
        serial number of the entry (e.g. inode number)

    :param const struct buffer_head \*bh:
        buffer head of the buffer storing the entry block

    :param void \*kaddr:
        kernel address mapped for the page including the buffer

.. _`nilfs_palloc_find_available_slot`:

nilfs_palloc_find_available_slot
================================

.. c:function:: int nilfs_palloc_find_available_slot(unsigned char *bitmap, unsigned long target, unsigned int bsize, spinlock_t *lock)

    find available slot in a group

    :param unsigned char \*bitmap:
        bitmap of the group

    :param unsigned long target:
        offset number of an entry in the group (start point)

    :param unsigned int bsize:
        size in bits

    :param spinlock_t \*lock:
        spin lock protecting \ ``bitmap``\ 

.. _`nilfs_palloc_rest_groups_in_desc_block`:

nilfs_palloc_rest_groups_in_desc_block
======================================

.. c:function:: unsigned long nilfs_palloc_rest_groups_in_desc_block(const struct inode *inode, unsigned long curr, unsigned long max)

    get the remaining number of groups in a group descriptor block

    :param const struct inode \*inode:
        inode of metadata file using this allocator

    :param unsigned long curr:
        current group number

    :param unsigned long max:
        maximum number of groups

.. _`nilfs_palloc_count_desc_blocks`:

nilfs_palloc_count_desc_blocks
==============================

.. c:function:: int nilfs_palloc_count_desc_blocks(struct inode *inode, unsigned long *desc_blocks)

    count descriptor blocks number

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param unsigned long \*desc_blocks:
        descriptor blocks number [out]

.. _`nilfs_palloc_mdt_file_can_grow`:

nilfs_palloc_mdt_file_can_grow
==============================

.. c:function:: bool nilfs_palloc_mdt_file_can_grow(struct inode *inode, unsigned long desc_blocks)

    check potential opportunity for MDT file growing

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param unsigned long desc_blocks:
        known current descriptor blocks count

.. _`nilfs_palloc_count_max_entries`:

nilfs_palloc_count_max_entries
==============================

.. c:function:: int nilfs_palloc_count_max_entries(struct inode *inode, u64 nused, u64 *nmaxp)

    count max number of entries that can be described by descriptor blocks count

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param u64 nused:
        current number of used entries

    :param u64 \*nmaxp:
        max number of entries [out]

.. _`nilfs_palloc_prepare_alloc_entry`:

nilfs_palloc_prepare_alloc_entry
================================

.. c:function:: int nilfs_palloc_prepare_alloc_entry(struct inode *inode, struct nilfs_palloc_req *req)

    prepare to allocate a persistent object

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param struct nilfs_palloc_req \*req:
        nilfs_palloc_req structure exchanged for the allocation

.. _`nilfs_palloc_commit_alloc_entry`:

nilfs_palloc_commit_alloc_entry
===============================

.. c:function:: void nilfs_palloc_commit_alloc_entry(struct inode *inode, struct nilfs_palloc_req *req)

    finish allocation of a persistent object

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param struct nilfs_palloc_req \*req:
        nilfs_palloc_req structure exchanged for the allocation

.. _`nilfs_palloc_commit_free_entry`:

nilfs_palloc_commit_free_entry
==============================

.. c:function:: void nilfs_palloc_commit_free_entry(struct inode *inode, struct nilfs_palloc_req *req)

    finish deallocating a persistent object

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param struct nilfs_palloc_req \*req:
        nilfs_palloc_req structure exchanged for the removal

.. _`nilfs_palloc_abort_alloc_entry`:

nilfs_palloc_abort_alloc_entry
==============================

.. c:function:: void nilfs_palloc_abort_alloc_entry(struct inode *inode, struct nilfs_palloc_req *req)

    cancel allocation of a persistent object

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param struct nilfs_palloc_req \*req:
        nilfs_palloc_req structure exchanged for the allocation

.. _`nilfs_palloc_prepare_free_entry`:

nilfs_palloc_prepare_free_entry
===============================

.. c:function:: int nilfs_palloc_prepare_free_entry(struct inode *inode, struct nilfs_palloc_req *req)

    prepare to deallocate a persistent object

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param struct nilfs_palloc_req \*req:
        nilfs_palloc_req structure exchanged for the removal

.. _`nilfs_palloc_abort_free_entry`:

nilfs_palloc_abort_free_entry
=============================

.. c:function:: void nilfs_palloc_abort_free_entry(struct inode *inode, struct nilfs_palloc_req *req)

    cancel deallocating a persistent object

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param struct nilfs_palloc_req \*req:
        nilfs_palloc_req structure exchanged for the removal

.. _`nilfs_palloc_freev`:

nilfs_palloc_freev
==================

.. c:function:: int nilfs_palloc_freev(struct inode *inode, __u64 *entry_nrs, size_t nitems)

    deallocate a set of persistent objects

    :param struct inode \*inode:
        inode of metadata file using this allocator

    :param __u64 \*entry_nrs:
        array of entry numbers to be deallocated

    :param size_t nitems:
        number of entries stored in \ ``entry_nrs``\ 

.. This file was automatic generated / don't edit.

