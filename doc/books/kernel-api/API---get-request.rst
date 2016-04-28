.. -*- coding: utf-8; mode: rst -*-

.. _API---get-request:

=============
__get_request
=============

*man __get_request(9)*

*4.6.0-rc5*

get a free request


Synopsis
========

.. c:function:: struct request * __get_request( struct request_list * rl, int rw_flags, struct bio * bio, gfp_t gfp_mask )

Arguments
=========

``rl``
    request list to allocate from

``rw_flags``
    RW and SYNC flags

``bio``
    bio to allocate request for (can be ``NULL``)

``gfp_mask``
    allocation mask


Description
===========

Get a free request from ``q``. This function may fail under memory
pressure or if ``q`` is dead.

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
