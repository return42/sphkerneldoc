.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-bio-complete:

========================
trace_block_bio_complete
========================

*man trace_block_bio_complete(9)*

*4.6.0-rc5*

completed all work on the block operation


Synopsis
========

.. c:function:: void trace_block_bio_complete( struct request_queue * q, struct bio * bio, int error )

Arguments
=========

``q``
    queue holding the block operation

``bio``
    block operation completed

``error``
    io error value


Description
===========

This tracepoint indicates there is no further work to do on this block
IO operation ``bio``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
