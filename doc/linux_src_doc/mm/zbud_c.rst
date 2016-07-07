.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/zbud.c

.. _`zbud_pool`:

struct zbud_pool
================

.. c:type:: struct zbud_pool

    stores metadata for each zbud pool

.. _`zbud_pool.definition`:

Definition
----------

.. code-block:: c

    struct zbud_pool {
        spinlock_t lock;
        struct list_head unbuddied[NCHUNKS];
        struct list_head buddied;
        struct list_head lru;
        u64 pages_nr;
        const struct zbud_ops *ops;
        #ifdef CONFIG_ZPOOL
        struct zpool *zpool;
        const struct zpool_ops *zpool_ops;
        #endif
    }

.. _`zbud_pool.members`:

Members
-------

lock
    protects all pool fields and first\|last_chunk fields of any
    zbud page in the pool

unbuddied
    array of lists tracking zbud pages that only contain one buddy;
    the lists each zbud page is added to depends on the size of
    its free region.

buddied
    list tracking the zbud pages that contain two buddies;
    these zbud pages are full

lru
    list tracking the zbud pages in LRU order by most recently
    added buddy.

pages_nr
    number of zbud pages in the pool.

ops
    pointer to a structure of user defined operations specified at
    pool creation time.

zpool
    *undescribed*

zpool_ops
    *undescribed*

.. _`zbud_pool.description`:

Description
-----------

This structure is allocated at pool creation time and maintains metadata
pertaining to a particular zbud pool.

.. _`zbud_create_pool`:

zbud_create_pool
================

.. c:function:: struct zbud_pool *zbud_create_pool(gfp_t gfp, const struct zbud_ops *ops)

    create a new zbud pool

    :param gfp_t gfp:
        gfp flags when allocating the zbud pool structure

    :param const struct zbud_ops \*ops:
        user-defined operations for the zbud pool

.. _`zbud_create_pool.return`:

Return
------

pointer to the new zbud pool or NULL if the metadata allocation
failed.

.. _`zbud_destroy_pool`:

zbud_destroy_pool
=================

.. c:function:: void zbud_destroy_pool(struct zbud_pool *pool)

    destroys an existing zbud pool

    :param struct zbud_pool \*pool:
        the zbud pool to be destroyed

.. _`zbud_destroy_pool.description`:

Description
-----------

The pool should be emptied before this function is called.

.. _`zbud_alloc`:

zbud_alloc
==========

.. c:function:: int zbud_alloc(struct zbud_pool *pool, size_t size, gfp_t gfp, unsigned long *handle)

    allocates a region of a given size

    :param struct zbud_pool \*pool:
        zbud pool from which to allocate

    :param size_t size:
        size in bytes of the desired allocation

    :param gfp_t gfp:
        gfp flags used if the pool needs to grow

    :param unsigned long \*handle:
        handle of the new allocation

.. _`zbud_alloc.description`:

Description
-----------

This function will attempt to find a free region in the pool large enough to
satisfy the allocation request.  A search of the unbuddied lists is
performed first. If no suitable free region is found, then a new page is
allocated and added to the pool to satisfy the request.

gfp should not set \__GFP_HIGHMEM as highmem pages cannot be used
as zbud pool pages.

.. _`zbud_alloc.return`:

Return
------

0 if success and handle is set, otherwise -EINVAL if the size or
gfp arguments are invalid or -ENOMEM if the pool was unable to allocate
a new page.

.. _`zbud_free`:

zbud_free
=========

.. c:function:: void zbud_free(struct zbud_pool *pool, unsigned long handle)

    frees the allocation associated with the given handle

    :param struct zbud_pool \*pool:
        pool in which the allocation resided

    :param unsigned long handle:
        handle associated with the allocation returned by \ :c:func:`zbud_alloc`\ 

.. _`zbud_free.description`:

Description
-----------

In the case that the zbud page in which the allocation resides is under
reclaim, as indicated by the PG_reclaim flag being set, this function
only sets the first\|last_chunks to 0.  The page is actually freed
once both buddies are evicted (see \ :c:func:`zbud_reclaim_page`\  below).

.. _`zbud_reclaim_page`:

zbud_reclaim_page
=================

.. c:function:: int zbud_reclaim_page(struct zbud_pool *pool, unsigned int retries)

    evicts allocations from a pool page and frees it

    :param struct zbud_pool \*pool:
        pool from which a page will attempt to be evicted

    :param unsigned int retries:
        *undescribed*

.. _`zbud_reclaim_page.description`:

Description
-----------

zbud reclaim is different from normal system reclaim in that the reclaim is
done from the bottom, up.  This is because only the bottom layer, zbud, has
information on how the allocations are organized within each zbud page. This
has the potential to create interesting locking situations between zbud and
the user, however.

To avoid these, this is how \ :c:func:`zbud_reclaim_page`\  should be called:
The user detects a page should be reclaimed and calls \ :c:func:`zbud_reclaim_page`\ .
\ :c:func:`zbud_reclaim_page`\  will remove a zbud page from the pool LRU list and call
the user-defined eviction handler with the pool and handle as arguments.

If the handle can not be evicted, the eviction handler should return
non-zero. \ :c:func:`zbud_reclaim_page`\  will add the zbud page back to the
appropriate list and try the next zbud page on the LRU up to
a user defined number of retries.

If the handle is successfully evicted, the eviction handler should
return 0 \_and\_ should have called \ :c:func:`zbud_free`\  on the handle. \ :c:func:`zbud_free`\ 
contains logic to delay freeing the page if the page is under reclaim,
as indicated by the setting of the PG_reclaim flag on the underlying page.

If all buddies in the zbud page are successfully evicted, then the
zbud page can be freed.

.. _`zbud_reclaim_page.return`:

Return
------

0 if page is successfully freed, otherwise -EINVAL if there are
no pages to evict or an eviction handler is not registered, -EAGAIN if
the retry limit was hit.

.. _`zbud_map`:

zbud_map
========

.. c:function:: void *zbud_map(struct zbud_pool *pool, unsigned long handle)

    maps the allocation associated with the given handle

    :param struct zbud_pool \*pool:
        pool in which the allocation resides

    :param unsigned long handle:
        handle associated with the allocation to be mapped

.. _`zbud_map.description`:

Description
-----------

While trivial for zbud, the mapping functions for others allocators
implementing this allocation API could have more complex information encoded
in the handle and could create temporary mappings to make the data
accessible to the user.

.. _`zbud_map.return`:

Return
------

a pointer to the mapped allocation

.. _`zbud_unmap`:

zbud_unmap
==========

.. c:function:: void zbud_unmap(struct zbud_pool *pool, unsigned long handle)

    maps the allocation associated with the given handle

    :param struct zbud_pool \*pool:
        pool in which the allocation resides

    :param unsigned long handle:
        handle associated with the allocation to be unmapped

.. _`zbud_get_pool_size`:

zbud_get_pool_size
==================

.. c:function:: u64 zbud_get_pool_size(struct zbud_pool *pool)

    gets the zbud pool size in pages

    :param struct zbud_pool \*pool:
        pool whose size is being queried

.. _`zbud_get_pool_size.return`:

Return
------

size in pages of the given pool.  The pool lock need not be
taken to access pages_nr.

.. This file was automatic generated / don't edit.

