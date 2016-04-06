
.. _API-blk-run-queue:

=============
blk_run_queue
=============

*man blk_run_queue(9)*

*4.6.0-rc1*

run a single device queue


Synopsis
========

.. c:function:: void blk_run_queue( struct request_queue * q )

Arguments
=========

``q``
    The queue to run


Description
===========

Invoke request handling on this queue, if it has pending work to do. May be used to restart queueing when a request has completed.
