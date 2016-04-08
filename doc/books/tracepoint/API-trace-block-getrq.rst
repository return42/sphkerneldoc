
.. _API-trace-block-getrq:

=================
trace_block_getrq
=================

*man trace_block_getrq(9)*

*4.6.0-rc1*

get a free request entry in queue for block IO operations


Synopsis
========

.. c:function:: void trace_block_getrq( struct request_queue * q, struct bio * bio, int rw )

Arguments
=========

``q``
    queue for operations

``bio``
    pending block IO operation

``rw``
    low bit indicates a read (``0``) or a write (``1``)


Description
===========

A request struct for queue ``q`` has been allocated to handle the block IO operation ``bio``.
