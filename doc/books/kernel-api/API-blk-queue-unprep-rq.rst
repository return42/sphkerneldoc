.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-unprep-rq:

===================
blk_queue_unprep_rq
===================

*man blk_queue_unprep_rq(9)*

*4.6.0-rc5*

set an unprepare_request function for queue


Synopsis
========

.. c:function:: void blk_queue_unprep_rq( struct request_queue * q, unprep_rq_fn * ufn )

Arguments
=========

``q``
    queue

``ufn``
    unprepare_request function


Description
===========

It's possible for a queue to register an unprepare_request callback
which is invoked before the request is finally completed. The goal of
the function is to deallocate any data that was allocated in the
prepare_request callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
