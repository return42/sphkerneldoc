
.. _API-trace-block-bio-backmerge:

=========================
trace_block_bio_backmerge
=========================

*man trace_block_bio_backmerge(9)*

*4.6.0-rc1*

merging block operation to the end of an existing operation


Synopsis
========

.. c:function:: void trace_block_bio_backmerge( struct request_queue * q, struct request * rq, struct bio * bio )

Arguments
=========

``q``
    queue holding operation

``rq``
    request bio is being merged into

``bio``
    new block operation to merge


Description
===========

Merging block request ``bio`` to the end of an existing block request in queue ``q``.
