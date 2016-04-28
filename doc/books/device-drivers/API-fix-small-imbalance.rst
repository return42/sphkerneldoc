.. -*- coding: utf-8; mode: rst -*-

.. _API-fix-small-imbalance:

===================
fix_small_imbalance
===================

*man fix_small_imbalance(9)*

*4.6.0-rc5*

Calculate the minor imbalance that exists amongst the groups of a
sched_domain, during load balancing.


Synopsis
========

.. c:function:: void fix_small_imbalance( struct lb_env * env, struct sd_lb_stats * sds )

Arguments
=========

``env``
    The load balancing environment.

``sds``
    Statistics of the sched_domain whose imbalance is to be calculated.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
