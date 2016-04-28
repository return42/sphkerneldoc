.. -*- coding: utf-8; mode: rst -*-

.. _API-get-request:

===========
get_request
===========

*man get_request(9)*

*4.6.0-rc5*

get a free request


Synopsis
========

.. c:function:: struct request * get_request( struct request_queue * q, int rw_flags, struct bio * bio, gfp_t gfp_mask )

Arguments
=========

``q``
    request_queue to allocate request from

``rw_flags``
    RW and SYNC flags

``bio``
    bio to allocate request for (can be ``NULL``)

``gfp_mask``
    allocation mask


Description
===========

Get a free request from ``q``. If ``__GFP_DIRECT_RECLAIM`` is set in
``gfp_mask``, this function keeps retrying under memory pressure and
fails iff ``q`` is dead.

Must be called with ``q``->queue_lock held and, Returns ERR_PTR on
failure, with ``q``->queue_lock held. Returns request pointer on
success, with ``q``->queue_lock *not held*.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
