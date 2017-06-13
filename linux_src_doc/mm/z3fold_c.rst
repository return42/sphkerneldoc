.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/z3fold.c

.. _`z3fold_pool`:

struct z3fold_pool
==================

.. c:type:: struct z3fold_pool

    stores metadata for each z3fold pool

.. _`z3fold_pool.definition`:

Definition
----------

.. code-block:: c

    struct z3fold_pool {
        spinlock_t lock;
        struct list_head unbuddied[NCHUNKS];
        struct list_head lru;
        atomic64_t pages_nr;
        const struct z3fold_ops *ops;
        struct zpool *zpool;
        const struct zpool_ops *zpool_ops;
    }

.. _`z3fold_pool.members`:

Members
-------

lock
    protects all pool fields and first\|last_chunk fields of any
    z3fold page in the pool

unbuddied
    array of lists tracking z3fold pages that contain 2- buddies;
    the lists each z3fold page is added to depends on the size of
    its free region.

lru
    list tracking the z3fold pages in LRU order by most recently
    added buddy.

pages_nr
    number of z3fold pages in the pool.

ops
    pointer to a structure of user defined operations specified at
    pool creation time.

zpool
    *undescribed*

zpool_ops
    *undescribed*

.. _`z3fold_pool.description`:

Description
-----------

This structure is allocated at pool creation time and maintains metadata
pertaining to a particular z3fold pool.

.. _`z3fold_create_pool`:

z3fold_create_pool
==================

.. c:function:: struct z3fold_pool *z3fold_create_pool(gfp_t gfp, const struct z3fold_ops *ops)

    create a new z3fold pool

    :param gfp_t gfp:
        gfp flags when allocating the z3fold pool structure

    :param const struct z3fold_ops \*ops:
        user-defined operations for the z3fold pool

.. _`z3fold_create_pool.return`:

Return
------

pointer to the new z3fold pool or NULL if the metadata allocation
failed.

.. _`z3fold_destroy_pool`:

z3fold_destroy_pool
===================

.. c:function:: void z3fold_destroy_pool(struct z3fold_pool *pool)

    destroys an existing z3fold pool

    :param struct z3fold_pool \*pool:
        the z3fold pool to be destroyed

.. _`z3fold_destroy_pool.description`:

Description
-----------

The pool should be emptied before this function is called.

.. _`z3fold_alloc`:

z3fold_alloc
============

.. c:function:: int z3fold_alloc(struct z3fold_pool *pool, size_t size, gfp_t gfp, unsigned long *handle)

    allocates a region of a given size

    :param struct z3fold_pool \*pool:
        z3fold pool from which to allocate

    :param size_t size:
        size in bytes of the desired allocation

    :param gfp_t gfp:
        gfp flags used if the pool needs to grow

    :param unsigned long \*handle:
        handle of the new allocation

.. _`z3fold_alloc.description`:

Description
-----------

This function will attempt to find a free region in the pool large enough to
satisfy the allocation request.  A search of the unbuddied lists is
performed first. If no suitable free region is found, then a new page is
allocated and added to the pool to satisfy the request.

gfp should not set \__GFP_HIGHMEM as highmem pages cannot be used
as z3fold pool pages.

.. _`z3fold_alloc.return`:

Return
------

0 if success and handle is set, otherwise -EINVAL if the size or
gfp arguments are invalid or -ENOMEM if the pool was unable to allocate
a new page.

.. _`z3fold_free`:

z3fold_free
===========

.. c:function:: void z3fold_free(struct z3fold_pool *pool, unsigned long handle)

    frees the allocation associated with the given handle

    :param struct z3fold_pool \*pool:
        pool in which the allocation resided

    :param unsigned long handle:
        handle associated with the allocation returned by \ :c:func:`z3fold_alloc`\ 

.. _`z3fold_free.description`:

Description
-----------

In the case that the z3fold page in which the allocation resides is under
reclaim, as indicated by the PG_reclaim flag being set, this function
only sets the first\|last_chunks to 0.  The page is actually freed
once both buddies are evicted (see \ :c:func:`z3fold_reclaim_page`\  below).

.. _`z3fold_reclaim_page`:

z3fold_reclaim_page
===================

.. c:function:: int z3fold_reclaim_page(struct z3fold_pool *pool, unsigned int retries)

    evicts allocations from a pool page and frees it

    :param struct z3fold_pool \*pool:
        pool from which a page will attempt to be evicted

    :param unsigned int retries:
        *undescribed*

.. _`z3fold_reclaim_page.description`:

Description
-----------

z3fold reclaim is different from normal system reclaim in that it is done
from the bottom, up. This is because only the bottom layer, z3fold, has
information on how the allocations are organized within each z3fold page.
This has the potential to create interesting locking situations between
z3fold and the user, however.

To avoid these, this is how \ :c:func:`z3fold_reclaim_page`\  should be called:
The user detects a page should be reclaimed and calls \ :c:func:`z3fold_reclaim_page`\ .
\ :c:func:`z3fold_reclaim_page`\  will remove a z3fold page from the pool LRU list and
call the user-defined eviction handler with the pool and handle as
arguments.

If the handle can not be evicted, the eviction handler should return
non-zero. \ :c:func:`z3fold_reclaim_page`\  will add the z3fold page back to the
appropriate list and try the next z3fold page on the LRU up to
a user defined number of retries.

If the handle is successfully evicted, the eviction handler should
return 0 \_and\_ should have called \ :c:func:`z3fold_free`\  on the handle. \ :c:func:`z3fold_free`\ 
contains logic to delay freeing the page if the page is under reclaim,
as indicated by the setting of the PG_reclaim flag on the underlying page.

If all buddies in the z3fold page are successfully evicted, then the
z3fold page can be freed.

.. _`z3fold_reclaim_page.return`:

Return
------

0 if page is successfully freed, otherwise -EINVAL if there are
no pages to evict or an eviction handler is not registered, -EAGAIN if
the retry limit was hit.

.. _`z3fold_map`:

z3fold_map
==========

.. c:function:: void *z3fold_map(struct z3fold_pool *pool, unsigned long handle)

    maps the allocation associated with the given handle

    :param struct z3fold_pool \*pool:
        pool in which the allocation resides

    :param unsigned long handle:
        handle associated with the allocation to be mapped

.. _`z3fold_map.description`:

Description
-----------

Extracts the buddy number from handle and constructs the pointer to the
correct starting chunk within the page.

.. _`z3fold_map.return`:

Return
------

a pointer to the mapped allocation

.. _`z3fold_unmap`:

z3fold_unmap
============

.. c:function:: void z3fold_unmap(struct z3fold_pool *pool, unsigned long handle)

    unmaps the allocation associated with the given handle

    :param struct z3fold_pool \*pool:
        pool in which the allocation resides

    :param unsigned long handle:
        handle associated with the allocation to be unmapped

.. _`z3fold_get_pool_size`:

z3fold_get_pool_size
====================

.. c:function:: u64 z3fold_get_pool_size(struct z3fold_pool *pool)

    gets the z3fold pool size in pages

    :param struct z3fold_pool \*pool:
        pool whose size is being queried

.. _`z3fold_get_pool_size.return`:

Return
------

size in pages of the given pool.

.. This file was automatic generated / don't edit.

