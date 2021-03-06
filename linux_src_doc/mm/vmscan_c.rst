.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/vmscan.c

.. _`sane_reclaim`:

sane_reclaim
============

.. c:function:: bool sane_reclaim(struct scan_control *sc)

    is the usual dirty throttling mechanism operational?

    :param sc:
        scan_control in question
    :type sc: struct scan_control \*

.. _`sane_reclaim.description`:

Description
-----------

The normal page dirty throttling mechanism in \ :c:func:`balance_dirty_pages`\  is
completely broken with the legacy memcg and direct stalling in
\ :c:func:`shrink_page_list`\  is used for throttling instead, which lacks all the
niceties such as fairness, adaptive pausing, bandwidth proportional
allocation and configurability.

This function tests whether the vmscan currently in progress can assume
that the normal dirty throttling mechanism is operational.

.. _`lruvec_lru_size`:

lruvec_lru_size
===============

.. c:function:: unsigned long lruvec_lru_size(struct lruvec *lruvec, enum lru_list lru, int zone_idx)

    Returns the number of pages on the given LRU list.

    :param lruvec:
        lru vector
    :type lruvec: struct lruvec \*

    :param lru:
        lru to use
    :type lru: enum lru_list

    :param zone_idx:
        zones to consider (use MAX_NR_ZONES for the whole LRU list)
    :type zone_idx: int

.. _`shrink_slab`:

shrink_slab
===========

.. c:function:: unsigned long shrink_slab(gfp_t gfp_mask, int nid, struct mem_cgroup *memcg, int priority)

    shrink slab caches

    :param gfp_mask:
        allocation context
    :type gfp_mask: gfp_t

    :param nid:
        node whose slab caches to target
    :type nid: int

    :param memcg:
        memory cgroup whose slab caches to target
    :type memcg: struct mem_cgroup \*

    :param priority:
        the reclaim priority
    :type priority: int

.. _`shrink_slab.description`:

Description
-----------

Call the shrink functions to age shrinkable caches.

\ ``nid``\  is passed along to shrinkers with SHRINKER_NUMA_AWARE set,
unaware shrinkers will receive a node id of 0 instead.

\ ``memcg``\  specifies the memory cgroup to target. Unaware shrinkers
are called only if it is the root cgroup.

\ ``priority``\  is sc->priority, we take the number of objects and >> by priority
in order to get the scan target.

Returns the number of reclaimed slab objects.

.. _`putback_lru_page`:

putback_lru_page
================

.. c:function:: void putback_lru_page(struct page *page)

    put previously isolated page onto appropriate LRU list

    :param page:
        page to be put back to appropriate lru list
    :type page: struct page \*

.. _`putback_lru_page.description`:

Description
-----------

Add previously isolated \ ``page``\  to appropriate LRU list.
Page may still be unevictable for other reasons.

lru_lock must not be held, interrupts must be enabled.

.. _`isolate_lru_page`:

isolate_lru_page
================

.. c:function:: int isolate_lru_page(struct page *page)

    tries to isolate a page from its LRU list

    :param page:
        page to isolate from its LRU list
    :type page: struct page \*

.. _`isolate_lru_page.description`:

Description
-----------

Isolates a \ ``page``\  from an LRU list, clears PageLRU and adjusts the
vmstat statistic corresponding to whatever LRU list the page was on.

Returns 0 if the page was removed from an LRU list.
Returns -EBUSY if the page was not on an LRU list.

The returned page will have \ :c:func:`PageLRU`\  cleared.  If it was found on
the active list, it will have PageActive set.  If it was found on
the unevictable list, it will have the PageUnevictable bit set. That flag
may need to be cleared by the caller before letting the page go.

The vmstat statistic corresponding to the list on which the page was
found will be decremented.

.. _`isolate_lru_page.restrictions`:

Restrictions
------------


(1) Must be called with an elevated refcount on the page. This is a
fundamentnal difference from isolate_lru_pages (which is called
without a stable reference).
(2) the lru_lock must not be held.
(3) interrupts must be enabled.

.. _`check_move_unevictable_pages`:

check_move_unevictable_pages
============================

.. c:function:: void check_move_unevictable_pages(struct page **pages, int nr_pages)

    check pages for evictability and move to appropriate zone lru list

    :param pages:
        array of pages to check
    :type pages: struct page \*\*

    :param nr_pages:
        number of pages to check
    :type nr_pages: int

.. _`check_move_unevictable_pages.description`:

Description
-----------

Checks pages for evictability and moves them to the appropriate lru list.

This function is only used for SysV IPC SHM_UNLOCK.

.. This file was automatic generated / don't edit.

