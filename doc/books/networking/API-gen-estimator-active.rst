.. -*- coding: utf-8; mode: rst -*-

.. _API-gen-estimator-active:

====================
gen_estimator_active
====================

*man gen_estimator_active(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
