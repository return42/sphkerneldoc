
.. _API-trace-block-rq-insert:

=====================
trace_block_rq_insert
=====================

*man trace_block_rq_insert(9)*

*4.6.0-rc1*

insert block operation request into queue


Synopsis
========

.. c:function:: void trace_block_rq_insert( struct request_queue * q, struct request * rq )

Arguments
=========

``q``
    target queue

``rq``
    block IO operation request


Description
===========

Called immediately before block operation request ``rq`` is inserted into queue ``q``. The fields in the operation request ``rq`` struct can be examined to determine which device
and sectors the pending operation would access.
