.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-stack-limits:

======================
blk_queue_stack_limits
======================

*man blk_queue_stack_limits(9)*

*4.6.0-rc5*

inherit underlying queue limits for stacked drivers


Synopsis
========

.. c:function:: void blk_queue_stack_limits( struct request_queue * t, struct request_queue * b )

Arguments
=========

``t``
    the stacking driver (top)

``b``
    the underlying device (bottom)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
