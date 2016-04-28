.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-lr-context-free:

=====================
intel_lr_context_free
=====================

*man intel_lr_context_free(9)*

*4.6.0-rc5*

free the LRC specific bits of a context


Synopsis
========

.. c:function:: void intel_lr_context_free( struct intel_context * ctx )

Arguments
=========

``ctx``
    the LR context to free.


The real context freeing is done in i915_gem_context_free
=========================================================

this only


takes care of the bits that are LRC related
===========================================

the per-engine backing objects and the logical ringbuffer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
