.. -*- coding: utf-8; mode: rst -*-

.. _API-update-sd-pick-busiest:

======================
update_sd_pick_busiest
======================

*man update_sd_pick_busiest(9)*

*4.6.0-rc5*

return 1 on busiest group


Synopsis
========

.. c:function:: bool update_sd_pick_busiest( struct lb_env * env, struct sd_lb_stats * sds, struct sched_group * sg, struct sg_lb_stats * sgs )

Arguments
=========

``env``
    The load balancing environment.

``sds``
    sched_domain statistics

``sg``
    sched_group candidate to be checked for being the busiest

``sgs``
    sched_group statistics


Description
===========

Determine if ``sg`` is a busier group than the previously selected
busiest group.


Return
======

``true`` if ``sg`` is a busier group than the previously selected
busiest group. ``false`` otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
