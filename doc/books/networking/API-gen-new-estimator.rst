
.. _API-gen-new-estimator:

=================
gen_new_estimator
=================

*man gen_new_estimator(9)*

*4.6.0-rc1*

create a new rate estimator


Synopsis
========

.. c:function:: int gen_new_estimator( struct gnet_stats_basic_packed * bstats, struct gnet_stats_basic_cpu __percpu * cpu_bstats, struct gnet_stats_rate_est64 * rate_est, spinlock_t * stats_lock, struct nlattr * opt )

Arguments
=========

``bstats``
    basic statistics

``cpu_bstats``
    bstats per cpu

``rate_est``
    rate estimator statistics

``stats_lock``
    statistics lock

``opt``
    rate estimator configuration TLV


Description
===========

Creates a new rate estimator with ``bstats`` as source and ``rate_est`` as destination. A new timer with the interval specified in the configuration TLV is created. Upon each
interval, the latest statistics will be read from ``bstats`` and the estimated rate will be stored in ``rate_est`` with the statistics lock grabbed during this period.

Returns 0 on success or a negative error code.
