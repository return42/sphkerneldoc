.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/memcontrol.h

.. _`mem_cgroup_events`:

mem_cgroup_events
=================

.. c:function:: void mem_cgroup_events(struct mem_cgroup *memcg, enum mem_cgroup_events_index idx, unsigned int nr)

    count memory events against a cgroup

    :param struct mem_cgroup \*memcg:
        the memory cgroup

    :param enum mem_cgroup_events_index idx:
        the event index

    :param unsigned int nr:
        the number of events to account for

.. _`mem_cgroup_from_id`:

mem_cgroup_from_id
==================

.. c:function:: struct mem_cgroup *mem_cgroup_from_id(unsigned short id)

    look up a memcg from an id

    :param unsigned short id:
        the id to look up

.. _`mem_cgroup_from_id.description`:

Description
-----------

Caller must hold \ :c:func:`rcu_read_lock`\  and use \ :c:func:`css_tryget`\  as necessary.

.. _`parent_mem_cgroup`:

parent_mem_cgroup
=================

.. c:function:: struct mem_cgroup *parent_mem_cgroup(struct mem_cgroup *memcg)

    find the accounting parent of a memcg

    :param struct mem_cgroup \*memcg:
        memcg whose parent to find

.. _`parent_mem_cgroup.description`:

Description
-----------

Returns the parent memcg, or NULL if this is the root or the memory
controller is in legacy no-hierarchy mode.

.. _`mem_cgroup_update_page_stat`:

mem_cgroup_update_page_stat
===========================

.. c:function:: void mem_cgroup_update_page_stat(struct page *page, enum mem_cgroup_stat_index idx, int val)

    update page state statistics

    :param struct page \*page:
        the page

    :param enum mem_cgroup_stat_index idx:
        page state item to account

    :param int val:
        number of pages (positive or negative)

.. _`mem_cgroup_update_page_stat.description`:

Description
-----------

The \ ``page``\  must be locked or the caller must use \ :c:func:`lock_page_memcg`\ 
to prevent double accounting when the page is concurrently being

.. _`mem_cgroup_update_page_stat.moved-to-another-memcg`:

moved to another memcg
----------------------


lock_page(page) or lock_page_memcg(page)
if (TestClearPageState(page))
mem_cgroup_update_page_stat(page, state, -1);
unlock_page(page) or unlock_page_memcg(page)

.. _`memcg_kmem_charge`:

memcg_kmem_charge
=================

.. c:function:: int memcg_kmem_charge(struct page *page, gfp_t gfp, int order)

    charge a kmem page

    :param struct page \*page:
        page to charge

    :param gfp_t gfp:
        reclaim mode

    :param int order:
        allocation order

.. _`memcg_kmem_charge.description`:

Description
-----------

Returns 0 on success, an error code on failure.

.. _`memcg_kmem_uncharge`:

memcg_kmem_uncharge
===================

.. c:function:: void memcg_kmem_uncharge(struct page *page, int order)

    uncharge a kmem page

    :param struct page \*page:
        page to uncharge

    :param int order:
        allocation order

.. _`memcg_kmem_get_cache`:

memcg_kmem_get_cache
====================

.. c:function:: struct kmem_cache *memcg_kmem_get_cache(struct kmem_cache *cachep, gfp_t gfp)

    selects the correct per-memcg cache for allocation

    :param struct kmem_cache \*cachep:
        the original global kmem cache

    :param gfp_t gfp:
        *undescribed*

.. _`memcg_kmem_get_cache.description`:

Description
-----------

All memory allocated from a per-memcg cache is charged to the owner memcg.

.. _`memcg_kmem_update_page_stat`:

memcg_kmem_update_page_stat
===========================

.. c:function:: void memcg_kmem_update_page_stat(struct page *page, enum mem_cgroup_stat_index idx, int val)

    update kmem page state statistics

    :param struct page \*page:
        the page

    :param enum mem_cgroup_stat_index idx:
        page state item to account

    :param int val:
        number of pages (positive or negative)

.. This file was automatic generated / don't edit.

