.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-set-default-limits:

======================
blk_set_default_limits
======================

*man blk_set_default_limits(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
