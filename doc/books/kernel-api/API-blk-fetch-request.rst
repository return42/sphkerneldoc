.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-fetch-request:

=================
blk_fetch_request
=================

*man blk_fetch_request(9)*

*4.6.0-rc5*

fetch a request from a request queue


Synopsis
========

.. c:function:: struct request * blk_fetch_request( struct request_queue * q )

Arguments
=========

``q``
    request queue to fetch a request from


Description
===========

Return the request at the top of ``q``. The request is started on return
and LLD can start processing it immediately.


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
