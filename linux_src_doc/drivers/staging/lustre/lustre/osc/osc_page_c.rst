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

.. _`osc_lru_reserve`:

osc_lru_reserve
===============

.. c:function:: int osc_lru_reserve(const struct lu_env *env, struct osc_object *obj, struct osc_page *opg)

    :param const struct lu_env \*env:
        *undescribed*

    :param struct osc_object \*obj:
        *undescribed*

    :param struct osc_page \*opg:
        *undescribed*

.. _`osc_lru_reserve.description`:

Description
-----------

Usually the LRU slots are reserved in \ :c:func:`osc_io_iter_rw_init`\ .
Only in the case that the LRU slots are in extreme shortage, it should
have reserved enough slots for an IO.

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

.. This file was automatic generated / don't edit.

