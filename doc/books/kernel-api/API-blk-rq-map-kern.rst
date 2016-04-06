
.. _API-blk-rq-map-kern:

===============
blk_rq_map_kern
===============

*man blk_rq_map_kern(9)*

*4.6.0-rc1*

map kernel data to a request, for REQ_TYPE_BLOCK_PC usage


Synopsis
========

.. c:function:: int blk_rq_map_kern( struct request_queue * q, struct request * rq, void * kbuf, unsigned int len, gfp_t gfp_mask )

Arguments
=========

``q``
    request queue where request should be inserted

``rq``
    request to fill

``kbuf``
    the kernel buffer

``len``
    length of user data

``gfp_mask``
    memory allocation flags


Description
===========

Data will be mapped directly if possible. Otherwise a bounce buffer is used. Can be called multiple times to append multiple buffers.
