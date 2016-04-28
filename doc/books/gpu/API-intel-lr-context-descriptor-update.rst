.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-lr-context-descriptor-update:

==================================
intel_lr_context_descriptor_update
==================================

*man intel_lr_context_descriptor_update(9)*

*4.6.0-rc5*

calculate & cache the descriptor descriptor for a pinned context


Synopsis
========

.. c:function:: void intel_lr_context_descriptor_update( struct intel_context * ctx, struct intel_engine_cs * ring )

Arguments
=========

``ctx``
    Context to work on

``ring``
    Engine the descriptor will be used with


Description
===========

The context descriptor encodes various attributes of a context,
including its GTT address and some flags. Because it's fairly expensive
to calculate, we'll just do it once and cache the result, which remains
valid until the context is unpinned.

This is what a descriptor looks like, from LSB to MSB: bits 0-11: flags,
GEN8_CTX_* (cached in ctx_desc_template) bits 12-31: LRCA, GTT
address of (the HWSP of) this context bits 32-51: ctx ID, a globally
unique tag (the LRCA again!) bits 52-63: reserved, may encode the engine
ID (for GuC)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
