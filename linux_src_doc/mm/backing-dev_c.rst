.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/backing-dev.c

.. _`wb_congested_get_create`:

wb_congested_get_create
=======================

.. c:function:: struct bdi_writeback_congested *wb_congested_get_create(struct backing_dev_info *bdi, int blkcg_id, gfp_t gfp)

    get or create a wb_congested

    :param bdi:
        associated bdi
    :type bdi: struct backing_dev_info \*

    :param blkcg_id:
        ID of the associated blkcg
    :type blkcg_id: int

    :param gfp:
        allocation mask
    :type gfp: gfp_t

.. _`wb_congested_get_create.description`:

Description
-----------

Look up the wb_congested for \ ``blkcg_id``\  on \ ``bdi``\ .  If missing, create one.
The returned wb_congested has its reference count incremented.  Returns
NULL on failure.

.. _`wb_congested_put`:

wb_congested_put
================

.. c:function:: void wb_congested_put(struct bdi_writeback_congested *congested)

    put a wb_congested

    :param congested:
        wb_congested to put
    :type congested: struct bdi_writeback_congested \*

.. _`wb_congested_put.description`:

Description
-----------

Put \ ``congested``\  and destroy it if the refcnt reaches zero.

.. _`wb_get_create`:

wb_get_create
=============

.. c:function:: struct bdi_writeback *wb_get_create(struct backing_dev_info *bdi, struct cgroup_subsys_state *memcg_css, gfp_t gfp)

    get wb for a given memcg, create if necessary

    :param bdi:
        target bdi
    :type bdi: struct backing_dev_info \*

    :param memcg_css:
        cgroup_subsys_state of the target memcg (must have positive ref)
    :type memcg_css: struct cgroup_subsys_state \*

    :param gfp:
        allocation mask to use
    :type gfp: gfp_t

.. _`wb_get_create.description`:

Description
-----------

Try to get the wb for \ ``memcg_css``\  on \ ``bdi``\ .  If it doesn't exist, try to
create one.  The returned wb has its refcount incremented.

This function uses \ :c:func:`css_get`\  on \ ``memcg_css``\  and thus expects its refcnt
to be positive on invocation.  IOW, \ :c:func:`rcu_read_lock`\  protection on
\ ``memcg_css``\  isn't enough.  try_get it before calling this function.

A wb is keyed by its associated memcg.  As blkcg implicitly enables
memcg on the default hierarchy, memcg association is guaranteed to be
more specific (equal or descendant to the associated blkcg) and thus can
identify both the memcg and blkcg associations.

Because the blkcg associated with a memcg may change as blkcg is enabled
and disabled closer to root in the hierarchy, each wb keeps track of
both the memcg and blkcg associated with it and verifies the blkcg on
each lookup.  On mismatch, the existing wb is discarded and a new one is
created.

.. _`wb_memcg_offline`:

wb_memcg_offline
================

.. c:function:: void wb_memcg_offline(struct mem_cgroup *memcg)

    kill all wb's associated with a memcg being offlined

    :param memcg:
        memcg being offlined
    :type memcg: struct mem_cgroup \*

.. _`wb_memcg_offline.description`:

Description
-----------

Also prevents creation of any new wb's associated with \ ``memcg``\ .

.. _`wb_blkcg_offline`:

wb_blkcg_offline
================

.. c:function:: void wb_blkcg_offline(struct blkcg *blkcg)

    kill all wb's associated with a blkcg being offlined

    :param blkcg:
        blkcg being offlined
    :type blkcg: struct blkcg \*

.. _`wb_blkcg_offline.description`:

Description
-----------

Also prevents creation of any new wb's associated with \ ``blkcg``\ .

.. _`congestion_wait`:

congestion_wait
===============

.. c:function:: long congestion_wait(int sync, long timeout)

    wait for a backing_dev to become uncongested

    :param sync:
        SYNC or ASYNC IO
    :type sync: int

    :param timeout:
        timeout in jiffies
    :type timeout: long

.. _`congestion_wait.description`:

Description
-----------

Waits for up to \ ``timeout``\  jiffies for a backing_dev (any backing_dev) to exit
write congestion.  If no backing_devs are congested then just wait for the
next write to be completed.

.. _`wait_iff_congested`:

wait_iff_congested
==================

.. c:function:: long wait_iff_congested(int sync, long timeout)

    Conditionally wait for a backing_dev to become uncongested or a pgdat to complete writes

    :param sync:
        SYNC or ASYNC IO
    :type sync: int

    :param timeout:
        timeout in jiffies
    :type timeout: long

.. _`wait_iff_congested.description`:

Description
-----------

In the event of a congested backing_dev (any backing_dev) this waits
for up to \ ``timeout``\  jiffies for either a BDI to exit congestion of the
given \ ``sync``\  queue or a write to complete.

The return value is 0 if the sleep is for the full timeout. Otherwise,
it is the number of jiffies that were still remaining when the function
returned. return_value == timeout implies the function did not sleep.

.. This file was automatic generated / don't edit.

