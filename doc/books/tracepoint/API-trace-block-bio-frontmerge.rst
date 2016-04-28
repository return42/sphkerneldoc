.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-bio-frontmerge:

==========================
trace_block_bio_frontmerge
==========================

*man trace_block_bio_frontmerge(9)*

*4.6.0-rc5*

merging block operation to the beginning of an existing operation


Synopsis
========

.. c:function:: void trace_block_bio_frontmerge( struct request_queue * q, struct request * rq, struct bio * bio )

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

Merging block IO operation ``bio`` to the beginning of an existing block
operation in queue ``q``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
