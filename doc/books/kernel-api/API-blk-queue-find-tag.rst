
.. _API-blk-queue-find-tag:

==================
blk_queue_find_tag
==================

*man blk_queue_find_tag(9)*

*4.6.0-rc1*

find a request by its tag and queue


Synopsis
========

.. c:function:: struct request ⋆ blk_queue_find_tag( struct request_queue * q, int tag )

Arguments
=========

``q``
    The request queue for the device

``tag``
    The tag of the request


Notes
=====

Should be used when a device returns a tag and you want to match it with a request.

no locks need be held.
