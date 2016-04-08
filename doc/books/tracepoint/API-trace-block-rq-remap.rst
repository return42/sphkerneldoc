
.. _API-trace-block-rq-remap:

====================
trace_block_rq_remap
====================

*man trace_block_rq_remap(9)*

*4.6.0-rc1*

map request for a block operation request


Synopsis
========

.. c:function:: void trace_block_rq_remap( struct request_queue * q, struct request * rq, dev_t dev, sector_t from )

Arguments
=========

``q``
    queue holding the operation

``rq``
    block IO operation request

``dev``
    device for the operation

``from``
    original sector for the operation


Description
===========

The block operation request ``rq`` in ``q`` has been remapped. The block operation request ``rq`` holds the current information and ``from`` hold the original sector.
