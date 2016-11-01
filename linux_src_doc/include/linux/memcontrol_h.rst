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

.. _`mem_cgroup_lruvec`:

mem_cgroup_lruvec
=================

.. c:function:: struct lruvec *mem_cgroup_lruvec(struct pglist_data *pgdat, struct mem_cgroup *memcg)

    get the lru list vector for a node or a memcg zone

    :param struct pglist_data \*pgdat:
        *undescribed*

    :param struct mem_cgroup \*memcg:
        memcg of the wanted lruvec

.. _`mem_cgroup_lruvec.description`:

Description
-----------

Returns the lru list vector holding pages for a given \ ``node``\  or a given
\ ``memcg``\  and \ ``zone``\ . This can be the node lruvec, if the memory controller
is disabled.

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

