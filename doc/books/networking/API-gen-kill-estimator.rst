.. -*- coding: utf-8; mode: rst -*-

.. _API-gen-kill-estimator:

==================
gen_kill_estimator
==================

*man gen_kill_estimator(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
