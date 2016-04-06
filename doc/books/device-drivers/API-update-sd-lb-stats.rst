
.. _API-update-sd-lb-stats:

==================
update_sd_lb_stats
==================

*man update_sd_lb_stats(9)*

*4.6.0-rc1*

Update sched_domain's statistics for load balancing.


Synopsis
========

.. c:function:: void update_sd_lb_stats( struct lb_env * env, struct sd_lb_stats * sds )

Arguments
=========

``env``
    The load balancing environment.

``sds``
    variable to hold the statistics for this sched_domain.
