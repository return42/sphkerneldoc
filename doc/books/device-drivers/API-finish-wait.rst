
.. _API-finish-wait:

===========
finish_wait
===========

*man finish_wait(9)*

*4.6.0-rc1*

clean up after waiting in a queue


Synopsis
========

.. c:function:: void finish_wait( wait_queue_head_t * q, wait_queue_t * wait )

Arguments
=========

``q``
    waitqueue waited on

``wait``
    wait descriptor


Description
===========

Sets current thread back to running state and removes the wait descriptor from the given waitqueue if still queued.
