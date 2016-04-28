.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-gem-evict-vm:

=================
i915_gem_evict_vm
=================

*man i915_gem_evict_vm(9)*

*4.6.0-rc5*

Evict all idle vmas from a vm


Synopsis
========

.. c:function:: int i915_gem_evict_vm( struct i915_address_space * vm, bool do_idle )

Arguments
=========

``vm``
    Address space to cleanse

``do_idle``
    Boolean directing whether to idle first.


Description
===========

This function evicts all idles vmas from a vm. If all unpinned vmas
should be evicted the ``do_idle`` needs to be set to true.

This is used by the execbuf code as a last-ditch effort to defragment
the address space.


To clarify
==========

This is for freeing up virtual address space, not for freeing memory in
e.g. the shrinker.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
