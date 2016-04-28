.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-add-trace-rq-remap:

======================
blk_add_trace_rq_remap
======================

*man blk_add_trace_rq_remap(9)*

*4.6.0-rc5*

Add a trace for a request-remap operation


Synopsis
========

.. c:function:: void blk_add_trace_rq_remap( void * ignore, struct request_queue * q, struct request * rq, dev_t dev, sector_t from )

Arguments
=========

``ignore``
    trace callback data parameter (not used)

``q``
    queue the io is for

``rq``
    the source request

``dev``
    target device

``from``
    source sector


Description
===========

Device mapper remaps request to other devices. Add a trace for that
action.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
