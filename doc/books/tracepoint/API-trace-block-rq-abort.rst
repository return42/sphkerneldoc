
.. _API-trace-block-rq-abort:

====================
trace_block_rq_abort
====================

*man trace_block_rq_abort(9)*

*4.6.0-rc1*

abort block operation request


Synopsis
========

.. c:function:: void trace_block_rq_abort( struct request_queue * q, struct request * rq )

Arguments
=========

``q``
    queue containing the block operation request

``rq``
    block IO operation request


Description
===========

Called immediately after pending block IO operation request ``rq`` in queue ``q`` is aborted. The fields in the operation request ``rq`` can be examined to determine which device
and sectors the pending operation would access.
