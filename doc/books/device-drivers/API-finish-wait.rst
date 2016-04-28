.. -*- coding: utf-8; mode: rst -*-

.. _API-finish-wait:

===========
finish_wait
===========

*man finish_wait(9)*

*4.6.0-rc5*

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

Sets current thread back to running state and removes the wait
descriptor from the given waitqueue if still queued.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
