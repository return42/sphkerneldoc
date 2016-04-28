.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-vma-bind:

=============
i915_vma_bind
=============

*man i915_vma_bind(9)*

*4.6.0-rc5*

Sets up PTEs for an VMA in it's corresponding address space.


Synopsis
========

.. c:function:: int i915_vma_bind( struct i915_vma * vma, enum i915_cache_level cache_level, u32 flags )

Arguments
=========

``vma``
    VMA to map

``cache_level``
    mapping cache level

``flags``
    flags like global or local mapping


Description
===========

DMA addresses are taken from the scatter-gather table of this object (or
of this VMA in case of non-default GGTT views) and PTE entries set up.
Note that DMA addresses are also the only part of the SG table we care
about.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
