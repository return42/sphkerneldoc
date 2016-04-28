.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-rq-issue:

====================
trace_block_rq_issue
====================

*man trace_block_rq_issue(9)*

*4.6.0-rc5*

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

Called when block operation request ``rq`` from queue ``q`` is sent to a
device driver for processing.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
