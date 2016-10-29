.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/gen_estimator.c

.. _`gen_new_estimator`:

gen_new_estimator
=================

.. c:function:: int gen_new_estimator(struct gnet_stats_basic_packed *bstats, struct gnet_stats_basic_cpu __percpu *cpu_bstats, struct gnet_stats_rate_est64 *rate_est, spinlock_t *stats_lock, struct nlattr *opt)

    create a new rate estimator

    :param struct gnet_stats_basic_packed \*bstats:
        basic statistics

    :param struct gnet_stats_basic_cpu __percpu \*cpu_bstats:
        bstats per cpu

    :param struct gnet_stats_rate_est64 \*rate_est:
        rate estimator statistics

    :param spinlock_t \*stats_lock:
        statistics lock

    :param struct nlattr \*opt:
        rate estimator configuration TLV

.. _`gen_new_estimator.description`:

Description
-----------

Creates a new rate estimator with \ :c:type:`struct bstats <bstats>` as source and \ :c:type:`struct rate_est <rate_est>`
as destination. A new timer with the interval specified in the
configuration TLV is created. Upon each interval, the latest statistics
will be read from \ :c:type:`struct bstats <bstats>` and the estimated rate will be stored in
\ :c:type:`struct rate_est <rate_est>` with the statistics lock grabbed during this period.

Returns 0 on success or a negative error code.

.. _`gen_kill_estimator`:

gen_kill_estimator
==================

.. c:function:: void gen_kill_estimator(struct gnet_stats_basic_packed *bstats, struct gnet_stats_rate_est64 *rate_est)

    remove a rate estimator

    :param struct gnet_stats_basic_packed \*bstats:
        basic statistics

    :param struct gnet_stats_rate_est64 \*rate_est:
        rate estimator statistics

.. _`gen_kill_estimator.description`:

Description
-----------

Removes the rate estimator specified by \ :c:type:`struct bstats <bstats>` and \ :c:type:`struct rate_est <rate_est>`.

Note : Caller should respect an RCU grace period before freeing stats_lock

.. _`gen_replace_estimator`:

gen_replace_estimator
=====================

.. c:function:: int gen_replace_estimator(struct gnet_stats_basic_packed *bstats, struct gnet_stats_basic_cpu __percpu *cpu_bstats, struct gnet_stats_rate_est64 *rate_est, spinlock_t *stats_lock, struct nlattr *opt)

    replace rate estimator configuration

    :param struct gnet_stats_basic_packed \*bstats:
        basic statistics

    :param struct gnet_stats_basic_cpu __percpu \*cpu_bstats:
        bstats per cpu

    :param struct gnet_stats_rate_est64 \*rate_est:
        rate estimator statistics

    :param spinlock_t \*stats_lock:
        statistics lock

    :param struct nlattr \*opt:
        rate estimator configuration TLV

.. _`gen_replace_estimator.description`:

Description
-----------

Replaces the configuration of a rate estimator by calling
\ :c:func:`gen_kill_estimator`\  and \ :c:func:`gen_new_estimator`\ .

Returns 0 on success or a negative error code.

.. _`gen_estimator_active`:

gen_estimator_active
====================

.. c:function:: bool gen_estimator_active(const struct gnet_stats_basic_packed *bstats, const struct gnet_stats_rate_est64 *rate_est)

    test if estimator is currently in use

    :param const struct gnet_stats_basic_packed \*bstats:
        basic statistics

    :param const struct gnet_stats_rate_est64 \*rate_est:
        rate estimator statistics

.. _`gen_estimator_active.description`:

Description
-----------

Returns true if estimator is active, and false if not.

.. This file was automatic generated / don't edit.
