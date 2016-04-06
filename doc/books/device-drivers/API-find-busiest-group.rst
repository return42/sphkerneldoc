
.. _API-find-busiest-group:

==================
find_busiest_group
==================

*man find_busiest_group(9)*

*4.6.0-rc1*

Returns the busiest group within the sched_domain if there is an imbalance. If there isn't an imbalance, and the user has opted for power-savings, it returns a group whose CPUs
can be put to idle by rebalancing those tasks elsewhere, if such a group exists.


Synopsis
========

.. c:function:: struct sched_group ⋆ find_busiest_group( struct lb_env * env )

Arguments
=========

``env``
    The load balancing environment.


Description
===========

Also calculates the amount of weighted load which should be moved to restore balance.


Return
======

- The busiest group if imbalance exists. - If no imbalance and user has opted for power-savings balance, return the least loaded group whose CPUs can be put to idle by rebalancing
its tasks onto our group.
