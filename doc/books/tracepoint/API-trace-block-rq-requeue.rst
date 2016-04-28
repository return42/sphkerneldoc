.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-rq-requeue:

======================
trace_block_rq_requeue
======================

*man trace_block_rq_requeue(9)*

*4.6.0-rc5*

place block IO request back on a queue


Synopsis
========

.. c:function:: void trace_block_rq_requeue( struct request_queue * q, struct request * rq )

Arguments
=========

``q``
    queue holding operation

``rq``
    block IO operation request


Description
===========

The block operation request ``rq`` is being placed back into queue
``q``. For some reason the request was not completed and needs to be put
back in the queue.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
