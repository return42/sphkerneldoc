.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-queue-end-tag:

=================
blk_queue_end_tag
=================

*man blk_queue_end_tag(9)*

*4.6.0-rc5*

end tag operations for a request


Synopsis
========

.. c:function:: void blk_queue_end_tag( struct request_queue * q, struct request * rq )

Arguments
=========

``q``
    the request queue for the device

``rq``
    the request that has completed


Description
===========

Typically called when ``end_that_request_first`` returns ``0``, meaning
all transfers have been done for a request. It's important to call this
function before ``end_that_request_last``, as that will put the request
back on the free list thus corrupting the internal tag list.


Notes
=====

queue lock must be held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
