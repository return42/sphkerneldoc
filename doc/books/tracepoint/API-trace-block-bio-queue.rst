
.. _API-trace-block-bio-queue:

=====================
trace_block_bio_queue
=====================

*man trace_block_bio_queue(9)*

*4.6.0-rc1*

putting new block IO operation in queue


Synopsis
========

.. c:function:: void trace_block_bio_queue( struct request_queue * q, struct bio * bio )

Arguments
=========

``q``
    queue holding operation

``bio``
    new block operation


Description
===========

About to place the block IO operation ``bio`` into queue ``q``.
