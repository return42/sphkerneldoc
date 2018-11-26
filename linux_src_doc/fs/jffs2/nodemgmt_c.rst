.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/jffs2/nodemgmt.c

.. _`jffs2_do_reserve_space`:

jffs2_do_reserve_space
======================

.. c:function:: int jffs2_do_reserve_space(struct jffs2_sb_info *c, uint32_t minsize, uint32_t *len, uint32_t sumsize)

    request physical space to write nodes to flash

    :param c:
        superblock info
    :type c: struct jffs2_sb_info \*

    :param minsize:
        Minimum acceptable size of allocation
    :type minsize: uint32_t

    :param len:
        Returned value of allocation length
    :type len: uint32_t \*

    :param sumsize:
        *undescribed*
    :type sumsize: uint32_t

.. _`jffs2_do_reserve_space.description`:

Description
-----------

Requests a block of physical space on the flash. Returns zero for success
and puts 'len' into the appropriate place, or returns -ENOSPC or other
error if appropriate. Doesn't return len since that's

If it returns zero, \ :c:func:`jffs2_reserve_space`\  also downs the per-filesystem
allocation semaphore, to prevent more than one allocation from being
active at any time. The semaphore is later released by \ :c:func:`jffs2_commit_allocation`\ 

\ :c:func:`jffs2_reserve_space`\  may trigger garbage collection in order to make room
for the requested allocation.

.. _`jffs2_add_physical_node_ref`:

jffs2_add_physical_node_ref
===========================

.. c:function:: struct jffs2_raw_node_ref *jffs2_add_physical_node_ref(struct jffs2_sb_info *c, uint32_t ofs, uint32_t len, struct jffs2_inode_cache *ic)

    add a physical node reference to the list

    :param c:
        superblock info
    :type c: struct jffs2_sb_info \*

    :param ofs:
        *undescribed*
    :type ofs: uint32_t

    :param len:
        length of this physical node
    :type len: uint32_t

    :param ic:
        *undescribed*
    :type ic: struct jffs2_inode_cache \*

.. _`jffs2_add_physical_node_ref.description`:

Description
-----------

Should only be used to report nodes for which space has been allocated
by jffs2_reserve_space.

Must be called with the alloc_sem held.

.. This file was automatic generated / don't edit.

