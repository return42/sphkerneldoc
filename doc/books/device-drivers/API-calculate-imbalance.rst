
.. _API-calculate-imbalance:

===================
calculate_imbalance
===================

*man calculate_imbalance(9)*

*4.6.0-rc1*

Calculate the amount of imbalance present within the groups of a given sched_domain during load balance.


Synopsis
========

.. c:function:: void calculate_imbalance( struct lb_env * env, struct sd_lb_stats * sds )

Arguments
=========

``env``
    load balance environment

``sds``
    statistics of the sched_domain whose imbalance is to be calculated.
