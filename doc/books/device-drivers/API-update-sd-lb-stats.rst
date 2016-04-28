.. -*- coding: utf-8; mode: rst -*-

.. _API-update-sd-lb-stats:

==================
update_sd_lb_stats
==================

*man update_sd_lb_stats(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
