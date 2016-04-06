
.. _API-blk-set-default-limits:

======================
blk_set_default_limits
======================

*man blk_set_default_limits(9)*

*4.6.0-rc1*

reset limits to default values


Synopsis
========

.. c:function:: void blk_set_default_limits( struct queue_limits * lim )

Arguments
=========

``lim``
    the queue_limits structure to reset


Description
===========

Returns a queue_limit struct to its default state.
