.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-getrq:

=================
trace_block_getrq
=================

*man trace_block_getrq(9)*

*4.6.0-rc5*

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

A request struct for queue ``q`` has been allocated to handle the block
IO operation ``bio``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
