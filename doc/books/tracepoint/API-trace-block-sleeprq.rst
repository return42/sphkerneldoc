
.. _API-trace-block-sleeprq:

===================
trace_block_sleeprq
===================

*man trace_block_sleeprq(9)*

*4.6.0-rc1*

waiting to get a free request entry in queue for block IO operation


Synopsis
========

.. c:function:: void trace_block_sleeprq( struct request_queue * q, struct bio * bio, int rw )

Arguments
=========

``q``
    queue for operation

``bio``
    pending block IO operation

``rw``
    low bit indicates a read (``0``) or a write (``1``)


Description
===========

In the case where a request struct cannot be provided for queue ``q`` the process needs to wait for an request struct to become available. This tracepoint event is generated each
time the process goes to sleep waiting for request struct become available.
