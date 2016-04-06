
.. _API-blk-rq-map-user-iov:

===================
blk_rq_map_user_iov
===================

*man blk_rq_map_user_iov(9)*

*4.6.0-rc1*

map user data to a request, for REQ_TYPE_BLOCK_PC usage


Synopsis
========

.. c:function:: int blk_rq_map_user_iov( struct request_queue * q, struct request * rq, struct rq_map_data * map_data, const struct iov_iter * iter, gfp_t gfp_mask )

Arguments
=========

``q``
    request queue where request should be inserted

``rq``
    request to map data to

``map_data``
    pointer to the rq_map_data holding pages (if necessary)

``iter``
    iovec iterator

``gfp_mask``
    memory allocation flags


Description
===========

Data will be mapped directly for zero copy I/O, if possible. Otherwise a kernel bounce buffer is used.

A matching ``blk_rq_unmap_user`` must be issued at the end of I/O, while still in process context.


Note
====

The mapped bio may need to be bounced through ``blk_queue_bounce`` before being submitted to the device, as pages mapped may be out of reach. It's the callers responsibility to
make sure this happens. The original bio must be passed back in to ``blk_rq_unmap_user`` for proper unmapping.
