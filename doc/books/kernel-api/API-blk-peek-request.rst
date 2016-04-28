.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-peek-request:

================
blk_peek_request
================

*man blk_peek_request(9)*

*4.6.0-rc5*

peek at the top of a request queue


Synopsis
========

.. c:function:: struct request * blk_peek_request( struct request_queue * q )

Arguments
=========

``q``
    request queue to peek at


Description
===========

Return the request at the top of ``q``. The returned request should be
started using ``blk_start_request`` before LLD starts processing it.


Return
======

Pointer to the request at the top of ``q`` if available. Null otherwise.


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
