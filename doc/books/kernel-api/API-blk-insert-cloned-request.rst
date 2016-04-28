.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-insert-cloned-request:

=========================
blk_insert_cloned_request
=========================

*man blk_insert_cloned_request(9)*

*4.6.0-rc5*

Helper for stacking drivers to submit a request


Synopsis
========

.. c:function:: int blk_insert_cloned_request( struct request_queue * q, struct request * rq )

Arguments
=========

``q``
    the queue to submit the request

``rq``
    the request being queued


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
