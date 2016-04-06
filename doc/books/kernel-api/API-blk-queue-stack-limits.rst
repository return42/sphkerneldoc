
.. _API-blk-queue-stack-limits:

======================
blk_queue_stack_limits
======================

*man blk_queue_stack_limits(9)*

*4.6.0-rc1*

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
