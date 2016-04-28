.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-requeue-request:

===================
blk_requeue_request
===================

*man blk_requeue_request(9)*

*4.6.0-rc5*

put a request back on queue


Synopsis
========

.. c:function:: void blk_requeue_request( struct request_queue * q, struct request * rq )

Arguments
=========

``q``
    request queue where request should be inserted

``rq``
    request to be inserted


Description
===========

Drivers often keep queueing requests until the hardware cannot accept
more, when that condition happens we need to put the request back on the
queue. Must be called with queue lock held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
