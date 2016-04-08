
.. _API-gen-kill-estimator:

==================
gen_kill_estimator
==================

*man gen_kill_estimator(9)*

*4.6.0-rc1*

remove a rate estimator


Synopsis
========

.. c:function:: void gen_kill_estimator( struct gnet_stats_basic_packed * bstats, struct gnet_stats_rate_est64 * rate_est )

Arguments
=========

``bstats``
    basic statistics

``rate_est``
    rate estimator statistics


Description
===========

Removes the rate estimator specified by ``bstats`` and ``rate_est``.


Note
====

Caller should respect an RCU grace period before freeing stats_lock
