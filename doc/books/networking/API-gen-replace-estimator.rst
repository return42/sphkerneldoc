
.. _API-gen-replace-estimator:

=====================
gen_replace_estimator
=====================

*man gen_replace_estimator(9)*

*4.6.0-rc1*

replace rate estimator configuration


Synopsis
========

.. c:function:: int gen_replace_estimator( struct gnet_stats_basic_packed * bstats, struct gnet_stats_basic_cpu __percpu * cpu_bstats, struct gnet_stats_rate_est64 * rate_est, spinlock_t * stats_lock, struct nlattr * opt )

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

Replaces the configuration of a rate estimator by calling ``gen_kill_estimator`` and ``gen_new_estimator``.

Returns 0 on success or a negative error code.
