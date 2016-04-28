.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-block-bio-bounce:

======================
trace_block_bio_bounce
======================

*man trace_block_bio_bounce(9)*

*4.6.0-rc5*

used bounce buffer when processing block operation


Synopsis
========

.. c:function:: void trace_block_bio_bounce( struct request_queue * q, struct bio * bio )

Arguments
=========

``q``
    queue holding the block operation

``bio``
    block operation


Description
===========

A bounce buffer was used to handle the block operation ``bio`` in ``q``.
This occurs when hardware limitations prevent a direct transfer of data
between the ``bio`` data memory area and the IO device. Use of a bounce
buffer requires extra copying of data and decreases performance.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
