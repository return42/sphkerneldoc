
.. _API-gen-estimator-active:

====================
gen_estimator_active
====================

*man gen_estimator_active(9)*

*4.6.0-rc1*

test if estimator is currently in use


Synopsis
========

.. c:function:: bool gen_estimator_active( const struct gnet_stats_basic_packed * bstats, const struct gnet_stats_rate_est64 * rate_est )

Arguments
=========

``bstats``
    basic statistics

``rate_est``
    rate estimator statistics


Description
===========

Returns true if estimator is active, and false if not.
