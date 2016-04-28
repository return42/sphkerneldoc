.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-set-stacking-limits:

=======================
blk_set_stacking_limits
=======================

*man blk_set_stacking_limits(9)*

*4.6.0-rc5*

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

Returns a queue_limit struct to its default state. Should be used by
stacking drivers like DM that have no internal limits.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
