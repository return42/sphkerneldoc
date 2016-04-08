
.. _API-trace-block-rq-issue:

====================
trace_block_rq_issue
====================

*man trace_block_rq_issue(9)*

*4.6.0-rc1*

issue pending block IO request operation to device driver


Synopsis
========

.. c:function:: void trace_block_rq_issue( struct request_queue * q, struct request * rq )

Arguments
=========

``q``
    queue holding operation

``rq``
    block IO operation operation request


Description
===========

Called when block operation request ``rq`` from queue ``q`` is sent to a device driver for processing.
