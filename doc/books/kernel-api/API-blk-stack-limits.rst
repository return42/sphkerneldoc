.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-stack-limits:

================
blk_stack_limits
================

*man blk_stack_limits(9)*

*4.6.0-rc5*

adjust queue_limits for stacked devices


Synopsis
========

.. c:function:: int blk_stack_limits( struct queue_limits * t, struct queue_limits * b, sector_t start )

Arguments
=========

``t``
    the stacking driver limits (top device)

``b``
    the underlying queue limits (bottom, component device)

``start``
    first data sector within component device


Description
===========

This function is used by stacking drivers like MD and DM to ensure that
all component devices have compatible block sizes and alignments. The
stacking driver must provide a queue_limits struct (top) and then
iteratively call the stacking function for all component (bottom)
devices. The stacking function will attempt to combine the values and
ensure proper alignment.

Returns 0 if the top and bottom queue_limits are compatible. The top
device's block sizes and alignment offsets may be adjusted to ensure
alignment with the bottom device. If no compatible sizes and alignments
exist, -1 is returned and the resulting top queue_limits will have the
misaligned flag set to indicate that the alignment_offset is undefined.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
