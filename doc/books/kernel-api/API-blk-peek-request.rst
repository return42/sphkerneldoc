
.. _API-blk-peek-request:

================
blk_peek_request
================

*man blk_peek_request(9)*

*4.6.0-rc1*

peek at the top of a request queue


Synopsis
========

.. c:function:: struct request ⋆ blk_peek_request( struct request_queue * q )

Arguments
=========

``q``
    request queue to peek at


Description
===========

Return the request at the top of ``q``. The returned request should be started using ``blk_start_request`` before LLD starts processing it.


Return
======

Pointer to the request at the top of ``q`` if available. Null otherwise.


Context
=======

queue_lock must be held.
