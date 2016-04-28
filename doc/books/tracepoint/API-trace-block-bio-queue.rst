.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-bio-queue:

=====================
trace_block_bio_queue
=====================

*man trace_block_bio_queue(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
