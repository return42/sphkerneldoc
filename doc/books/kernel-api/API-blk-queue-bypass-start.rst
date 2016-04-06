
.. _API-blk-queue-bypass-start:

======================
blk_queue_bypass_start
======================

*man blk_queue_bypass_start(9)*

*4.6.0-rc1*

enter queue bypass mode


Synopsis
========

.. c:function:: void blk_queue_bypass_start( struct request_queue * q )

Arguments
=========

``q``
    queue of interest


Description
===========

In bypass mode, only the dispatch FIFO queue of ``q`` is used. This function makes ``q`` enter bypass mode and drains all requests which were throttled or issued before. On return,
it's guaranteed that no request is being throttled or has ELVPRIV set and ``blk_queue_bypass`` ``true`` inside queue or RCU read lock.
