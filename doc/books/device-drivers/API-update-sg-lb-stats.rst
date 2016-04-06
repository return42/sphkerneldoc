
.. _API-update-sg-lb-stats:

==================
update_sg_lb_stats
==================

*man update_sg_lb_stats(9)*

*4.6.0-rc1*

Update sched_group's statistics for load balancing.


Synopsis
========

.. c:function:: void update_sg_lb_stats( struct lb_env * env, struct sched_group * group, int load_idx, int local_group, struct sg_lb_stats * sgs, bool * overload )

Arguments
=========

``env``
    The load balancing environment.

``group``
    sched_group whose statistics are to be updated.

``load_idx``
    Load index of sched_domain of this_cpu for load calc.

``local_group``
    Does group contain this_cpu.

``sgs``
    variable to hold the statistics for this group.

``overload``
    Indicate more than one runnable task for any CPU.
