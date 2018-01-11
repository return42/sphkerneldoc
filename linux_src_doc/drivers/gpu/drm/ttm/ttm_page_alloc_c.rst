.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/ttm/ttm_page_alloc.c

.. _`ttm_page_pool`:

struct ttm_page_pool
====================

.. c:type:: struct ttm_page_pool

    Pool to reuse recently allocated uc/wc pages.

.. _`ttm_page_pool.definition`:

Definition
----------

.. code-block:: c

    struct ttm_page_pool {
        spinlock_t lock;
        bool fill_lock;
        struct list_head list;
        gfp_t gfp_flags;
        unsigned npages;
        char *name;
        unsigned long nfrees;
        unsigned long nrefills;
        unsigned int order;
    }

.. _`ttm_page_pool.members`:

Members
-------

lock
    Protects the shared pool from concurrnet access. Must be used with
    irqsave/irqrestore variants because pool allocator maybe called from
    delayed work.

fill_lock
    Prevent concurrent calls to fill.

list
    Pool of free uc/wc pages for fast reuse.

gfp_flags
    Flags to pass for alloc_page.

npages
    Number of pages in pool.

name
    *undescribed*

nfrees
    *undescribed*

nrefills
    *undescribed*

order
    *undescribed*

.. _`ttm_pool_manager`:

struct ttm_pool_manager
=======================

.. c:type:: struct ttm_pool_manager

    Holds memory pools for fst allocation

.. _`ttm_pool_manager.definition`:

Definition
----------

.. code-block:: c

    struct ttm_pool_manager {
        struct kobject kobj;
        struct shrinker mm_shrink;
        struct ttm_pool_opts options;
        union {
            struct ttm_page_pool pools[NUM_POOLS];
            struct {
                struct ttm_page_pool wc_pool;
                struct ttm_page_pool uc_pool;
                struct ttm_page_pool wc_pool_dma32;
                struct ttm_page_pool uc_pool_dma32;
                struct ttm_page_pool wc_pool_huge;
                struct ttm_page_pool uc_pool_huge;
            } ;
        } ;
    }

.. _`ttm_pool_manager.members`:

Members
-------

kobj
    *undescribed*

mm_shrink
    *undescribed*

options
    *undescribed*

{unnamed_union}
    anonymous

pools
    All pool objects in use.

{unnamed_struct}
    anonymous

wc_pool
    *undescribed*

uc_pool
    *undescribed*

wc_pool_dma32
    *undescribed*

uc_pool_dma32
    *undescribed*

wc_pool_huge
    *undescribed*

uc_pool_huge
    *undescribed*

.. _`ttm_pool_manager.description`:

Description
-----------

Manager is read only object for pool code so it doesn't need locking.

.. _`ttm_pages_put`:

ttm_pages_put
=============

.. c:function:: void ttm_pages_put(struct page  *pages, unsigned npages, unsigned int order)

    :param struct page  \*pages:
        *undescribed*

    :param unsigned npages:
        *undescribed*

    :param unsigned int order:
        *undescribed*

.. _`ttm_page_pool_free`:

ttm_page_pool_free
==================

.. c:function:: int ttm_page_pool_free(struct ttm_page_pool *pool, unsigned nr_free, bool use_static)

    :param struct ttm_page_pool \*pool:
        to free the pages from

    :param unsigned nr_free:
        *undescribed*

    :param bool use_static:
        Safe to use static buffer

.. _`ttm_page_pool_free.description`:

Description
-----------

To prevent hogging the ttm_swap process we only free NUM_PAGES_TO_ALLOC
number of pages in one go.

.. _`ttm_pool_shrink_scan`:

ttm_pool_shrink_scan
====================

.. c:function:: unsigned long ttm_pool_shrink_scan(struct shrinker *shrink, struct shrink_control *sc)

    :param struct shrinker \*shrink:
        *undescribed*

    :param struct shrink_control \*sc:
        *undescribed*

.. _`ttm_pool_shrink_scan.xxx`:

XXX
---

(dchinner) Deadlock warning!

This code is crying out for a shrinker per pool....

.. _`ttm_handle_caching_state_failure`:

ttm_handle_caching_state_failure
================================

.. c:function:: void ttm_handle_caching_state_failure(struct list_head *pages, int ttm_flags, enum ttm_caching_state cstate, struct page **failed_pages, unsigned cpages)

    any pages that have changed their caching state already put them to the pool.

    :param struct list_head \*pages:
        *undescribed*

    :param int ttm_flags:
        *undescribed*

    :param enum ttm_caching_state cstate:
        *undescribed*

    :param struct page \*\*failed_pages:
        *undescribed*

    :param unsigned cpages:
        *undescribed*

.. _`ttm_alloc_new_pages`:

ttm_alloc_new_pages
===================

.. c:function:: int ttm_alloc_new_pages(struct list_head *pages, gfp_t gfp_flags, int ttm_flags, enum ttm_caching_state cstate, unsigned count, unsigned order)

    :param struct list_head \*pages:
        *undescribed*

    :param gfp_t gfp_flags:
        *undescribed*

    :param int ttm_flags:
        *undescribed*

    :param enum ttm_caching_state cstate:
        *undescribed*

    :param unsigned count:
        *undescribed*

    :param unsigned order:
        *undescribed*

.. _`ttm_alloc_new_pages.description`:

Description
-----------

This function is reentrant if caller updates count depending on number of
pages returned in pages array.

.. _`ttm_page_pool_fill_locked`:

ttm_page_pool_fill_locked
=========================

.. c:function:: void ttm_page_pool_fill_locked(struct ttm_page_pool *pool, int ttm_flags, enum ttm_caching_state cstate, unsigned count, unsigned long *irq_flags)

    pages is small.

    :param struct ttm_page_pool \*pool:
        *undescribed*

    :param int ttm_flags:
        *undescribed*

    :param enum ttm_caching_state cstate:
        *undescribed*

    :param unsigned count:
        *undescribed*

    :param unsigned long \*irq_flags:
        *undescribed*

.. _`ttm_page_pool_get_pages`:

ttm_page_pool_get_pages
=======================

.. c:function:: int ttm_page_pool_get_pages(struct ttm_page_pool *pool, struct list_head *pages, int ttm_flags, enum ttm_caching_state cstate, unsigned count, unsigned order)

    :param struct ttm_page_pool \*pool:
        *undescribed*

    :param struct list_head \*pages:
        *undescribed*

    :param int ttm_flags:
        *undescribed*

    :param enum ttm_caching_state cstate:
        *undescribed*

    :param unsigned count:
        *undescribed*

    :param unsigned order:
        *undescribed*

.. _`ttm_page_pool_get_pages.description`:

Description
-----------

@return zero for success or negative error code.

.. This file was automatic generated / don't edit.

