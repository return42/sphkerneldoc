.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-cloned-rq-check-limits:

==========================
blk_cloned_rq_check_limits
==========================

*man blk_cloned_rq_check_limits(9)*

*4.6.0-rc5*

Helper function to check a cloned request for new the queue limits


Synopsis
========

.. c:function:: int blk_cloned_rq_check_limits( struct request_queue * q, struct request * rq )

Arguments
=========

``q``
    the queue

``rq``
    the request being checked


Description
===========

``rq`` may have been made based on weaker limitations of upper-level
queues in request stacking drivers, and it may violate the limitation of
``q``. Since the block layer and the underlying device driver trust
``rq`` after it is inserted to ``q``, it should be checked against ``q``
before the insertion using this generic function.

Request stacking drivers like request-based dm may change the queue
limits when retrying requests on other queues. Those requests need to be
checked against the new queue limits again during dispatch.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
