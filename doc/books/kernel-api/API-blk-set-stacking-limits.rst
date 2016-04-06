
.. _API-blk-set-stacking-limits:

=======================
blk_set_stacking_limits
=======================

*man blk_set_stacking_limits(9)*

*4.6.0-rc1*

set default limits for stacking devices


Synopsis
========

.. c:function:: void blk_set_stacking_limits( struct queue_limits * lim )

Arguments
=========

``lim``
    the queue_limits structure to reset


Description
===========

Returns a queue_limit struct to its default state. Should be used by stacking drivers like DM that have no internal limits.
