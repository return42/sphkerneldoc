.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-add-trace-rq:

================
blk_add_trace_rq
================

*man blk_add_trace_rq(9)*

*4.6.0-rc5*

Add a trace for a request oriented action


Synopsis
========

.. c:function:: void blk_add_trace_rq( struct request_queue * q, struct request * rq, unsigned int nr_bytes, u32 what )

Arguments
=========

``q``
    queue the io is for

``rq``
    the source request

``nr_bytes``
    number of completed bytes

``what``
    the action


Description
===========

Records an action against a request. Will log the bio offset + size.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
