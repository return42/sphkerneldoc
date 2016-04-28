.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-rq-complete:

=======================
trace_block_rq_complete
=======================

*man trace_block_rq_complete(9)*

*4.6.0-rc5*

block IO operation completed by device driver


Synopsis
========

.. c:function:: void trace_block_rq_complete( struct request_queue * q, struct request * rq, unsigned int nr_bytes )

Arguments
=========

``q``
    queue containing the block operation request

``rq``
    block operations request

``nr_bytes``
    number of completed bytes


Description
===========

The block_rq_complete tracepoint event indicates that some portion of
operation request has been completed by the device driver. If the
``rq``->bio is ``NULL``, then there is absolutely no additional work to
do for the request. If ``rq``->bio is non-NULL then there is additional
work required to complete the request.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
