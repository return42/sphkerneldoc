.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-rq-abort:

====================
trace_block_rq_abort
====================

*man trace_block_rq_abort(9)*

*4.6.0-rc5*

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

Called immediately after pending block IO operation request ``rq`` in
queue ``q`` is aborted. The fields in the operation request ``rq`` can
be examined to determine which device and sectors the pending operation
would access.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
