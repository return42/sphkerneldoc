
.. _API-fix-small-imbalance:

===================
fix_small_imbalance
===================

*man fix_small_imbalance(9)*

*4.6.0-rc1*

Calculate the minor imbalance that exists amongst the groups of a sched_domain, during load balancing.


Synopsis
========

.. c:function:: void fix_small_imbalance( struct lb_env * env, struct sd_lb_stats * sds )

Arguments
=========

``env``
    The load balancing environment.

``sds``
    Statistics of the sched_domain whose imbalance is to be calculated.
