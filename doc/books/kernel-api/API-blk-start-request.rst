.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-start-request:

=================
blk_start_request
=================

*man blk_start_request(9)*

*4.6.0-rc5*

start request processing on the driver


Synopsis
========

.. c:function:: void blk_start_request( struct request * req )

Arguments
=========

``req``
    request to dequeue


Description
===========

Dequeue ``req`` and start timeout timer on it. This hands off the
request to the driver.

Block internal functions which don't want to start timer should call
``blk_dequeue_request``.


Context
=======

queue_lock must be held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
