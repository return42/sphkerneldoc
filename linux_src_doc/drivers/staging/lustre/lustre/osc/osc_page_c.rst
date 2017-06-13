.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/osc/osc_page.c

.. _`osc_page_transfer_add`:

osc_page_transfer_add
=====================

.. c:function:: void osc_page_transfer_add(const struct lu_env *env, struct osc_page *opg, enum cl_req_type crt)

    either opportunistic (osc_page_cache_add()), or immediate (osc_page_submit()).

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_page \*opg:
        *undescribed*

    :param enum cl_req_type crt:
        *undescribed*

.. _`osc_page_submit`:

osc_page_submit
===============

.. c:function:: void osc_page_submit(const struct lu_env *env, struct osc_page *opg, enum cl_req_type crt, int brw_flags)

    transfer (i.e., transferred synchronously).

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_page \*opg:
        *undescribed*

    :param enum cl_req_type crt:
        *undescribed*

    :param int brw_flags:
        *undescribed*

.. _`lru_shrink_min`:

lru_shrink_min
==============

.. c:function:: int lru_shrink_min(struct client_obd *cli)

    number of pages to avoid running out of LRU slots.

    :param struct client_obd \*cli:
        *undescribed*

.. _`lru_shrink_max`:

lru_shrink_max
==============

.. c:function:: int lru_shrink_max(struct client_obd *cli)

    :param struct client_obd \*cli:
        *undescribed*

.. _`osc_cache_too_much`:

osc_cache_too_much
==================

.. c:function:: int osc_cache_too_much(struct client_obd *cli)

    we should free slots aggressively. In this way, slots are freed in a steady step to maintain fairness among OSCs.

    :param struct client_obd \*cli:
        *undescribed*

.. _`osc_cache_too_much.description`:

Description
-----------

Return how many LRU pages should be freed.

.. _`osc_lru_del`:

osc_lru_del
===========

.. c:function:: void osc_lru_del(struct client_obd *cli, struct osc_page *opg)

    has never finished(error occurred).

    :param struct client_obd \*cli:
        *undescribed*

    :param struct osc_page \*opg:
        *undescribed*

.. _`osc_lru_use`:

osc_lru_use
===========

.. c:function:: void osc_lru_use(struct client_obd *cli, struct osc_page *opg)

    :param struct client_obd \*cli:
        *undescribed*

    :param struct osc_page \*opg:
        *undescribed*

.. _`lru_page_busy`:

lru_page_busy
=============

.. c:function:: bool lru_page_busy(struct client_obd *cli, struct cl_page *page)

    :param struct client_obd \*cli:
        *undescribed*

    :param struct cl_page \*page:
        *undescribed*

.. _`lru_page_busy.description`:

Description
-----------

If unstable account is turned on, bulk transfer may hold one refcount
for recovery so we need to check vmpage refcount as well; otherwise,
even we can destroy cl_page but the corresponding vmpage can't be reused.

.. _`osc_lru_shrink`:

osc_lru_shrink
==============

.. c:function:: long osc_lru_shrink(const struct lu_env *env, struct client_obd *cli, long target, bool force)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct client_obd \*cli:
        *undescribed*

    :param long target:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`osc_lru_reclaim`:

osc_lru_reclaim
===============

.. c:function:: long osc_lru_reclaim(struct client_obd *cli, unsigned long npages)

    @npages of LRU slots. For performance consideration, it's better to drop LRU pages in batch. Therefore, the actual number is adjusted at least max_pages_per_rpc.

    :param struct client_obd \*cli:
        *undescribed*

    :param unsigned long npages:
        *undescribed*

.. _`osc_lru_alloc`:

osc_lru_alloc
=============

.. c:function:: int osc_lru_alloc(const struct lu_env *env, struct client_obd *cli, struct osc_page *opg)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct client_obd \*cli:
        *undescribed*

    :param struct osc_page \*opg:
        *undescribed*

.. _`osc_lru_alloc.description`:

Description
-----------

Usually the LRU slots are reserved in \ :c:func:`osc_io_iter_rw_init`\ .
Only in the case that the LRU slots are in extreme shortage, it should
have reserved enough slots for an IO.

.. _`osc_lru_reserve`:

osc_lru_reserve
===============

.. c:function:: unsigned long osc_lru_reserve(struct client_obd *cli, unsigned long npages)

    :param struct client_obd \*cli:
        *undescribed*

    :param unsigned long npages:
        *undescribed*

.. _`osc_lru_reserve.description`:

Description
-----------

The benefit of doing this is to reduce contention against atomic counter
cl_lru_left by changing it from per-page access to per-IO access.

.. _`osc_lru_unreserve`:

osc_lru_unreserve
=================

.. c:function:: void osc_lru_unreserve(struct client_obd *cli, unsigned long npages)

    :param struct client_obd \*cli:
        *undescribed*

    :param unsigned long npages:
        *undescribed*

.. _`osc_lru_unreserve.description`:

Description
-----------

LRU slots reserved by \ :c:func:`osc_lru_reserve`\  may have entries left due to several
reasons such as page already existing or I/O error. Those reserved slots
should be freed by calling this function.

.. _`unstable_page_accounting`:

unstable_page_accounting
========================

.. c:function:: void unstable_page_accounting(struct ptlrpc_bulk_desc *desc, int factor)

    same page pgdat to get better performance. In practice this can work pretty good because the pages in the same RPC are likely from the same page zone.

    :param struct ptlrpc_bulk_desc \*desc:
        *undescribed*

    :param int factor:
        *undescribed*

.. _`osc_dec_unstable_pages`:

osc_dec_unstable_pages
======================

.. c:function:: void osc_dec_unstable_pages(struct ptlrpc_request *req)

    increment operations performed in osc_inc_unstable_pages. It is registered as the RPC request callback, and is executed when the bulk RPC is committed on the server. Thus at this point, the pages involved in the bulk transfer are no longer considered unstable.

    :param struct ptlrpc_request \*req:
        *undescribed*

.. _`osc_dec_unstable_pages.description`:

Description
-----------

If this function is called, the request should have been committed
or req:rq_unstable must have been set; it implies that the unstable
statistic have been added.

.. _`osc_over_unstable_soft_limit`:

osc_over_unstable_soft_limit
============================

.. c:function:: bool osc_over_unstable_soft_limit(struct client_obd *cli)

    This function will be called by every BRW RPC so it's critical to make this function fast.

    :param struct client_obd \*cli:
        *undescribed*

.. _`osc_cache_shrink_count`:

osc_cache_shrink_count
======================

.. c:function:: unsigned long osc_cache_shrink_count(struct shrinker *sk, struct shrink_control *sc)

    :param struct shrinker \*sk:
        *undescribed*

    :param struct shrink_control \*sc:
        *undescribed*

.. _`osc_cache_shrink_count.return`:

Return
------

return # of cached LRU pages times reclaimation tendency
SHRINK_STOP if it cannot do any scanning in this time

.. _`osc_cache_shrink_scan`:

osc_cache_shrink_scan
=====================

.. c:function:: unsigned long osc_cache_shrink_scan(struct shrinker *sk, struct shrink_control *sc)

    >nr_to_scan cached LRU pages

    :param struct shrinker \*sk:
        *undescribed*

    :param struct shrink_control \*sc:
        *undescribed*

.. _`osc_cache_shrink_scan.return`:

Return
------

number of cached LRU pages reclaimed
SHRINK_STOP if it cannot do any scanning in this time

Linux kernel will loop calling this shrinker scan routine with
sc->nr_to_scan = SHRINK_BATCH(128 for now) until kernel got enough memory.

If sc->nr_to_scan is 0, the VM is querying the cache size, we don't need
to scan and try to reclaim LRU pages, just return 0 and
\ :c:func:`osc_cache_shrink_count`\  will report the LRU page number.

.. This file was automatic generated / don't edit.

