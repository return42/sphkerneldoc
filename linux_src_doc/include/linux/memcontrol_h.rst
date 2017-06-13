.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/memcontrol.h

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

.. _`mod_memcg_page_state`:

mod_memcg_page_state
====================

.. c:function:: void mod_memcg_page_state(struct page *page, enum memcg_stat_item idx, int val)

    update page state statistics

    :param struct page \*page:
        the page

    :param enum memcg_stat_item idx:
        page state item to account

    :param int val:
        number of pages (positive or negative)

.. _`mod_memcg_page_state.description`:

Description
-----------

The \ ``page``\  must be locked or the caller must use \ :c:func:`lock_page_memcg`\ 
to prevent double accounting when the page is concurrently being

.. _`mod_memcg_page_state.moved-to-another-memcg`:

moved to another memcg
----------------------


lock_page(page) or lock_page_memcg(page)
if (TestClearPageState(page))
mod_memcg_page_state(page, state, -1);
unlock_page(page) or unlock_page_memcg(page)

Kernel pages are an exception to this, since they'll never move.

.. _`memcg_kmem_update_page_stat`:

memcg_kmem_update_page_stat
===========================

.. c:function:: void memcg_kmem_update_page_stat(struct page *page, enum memcg_stat_item idx, int val)

    update kmem page state statistics

    :param struct page \*page:
        the page

    :param enum memcg_stat_item idx:
        page state item to account

    :param int val:
        number of pages (positive or negative)

.. This file was automatic generated / don't edit.

