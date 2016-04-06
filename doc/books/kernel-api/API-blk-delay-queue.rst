
.. _API-blk-delay-queue:

===============
blk_delay_queue
===============

*man blk_delay_queue(9)*

*4.6.0-rc1*

restart queueing after defined interval


Synopsis
========

.. c:function:: void blk_delay_queue( struct request_queue * q, unsigned long msecs )

Arguments
=========

``q``
    The ``struct request_queue`` in question

``msecs``
    Delay in msecs


Description
===========

Sometimes queueing needs to be postponed for a little while, to allow resources to come back. This function will make sure that queueing is restarted around the specified time.
Queue lock must be held.
