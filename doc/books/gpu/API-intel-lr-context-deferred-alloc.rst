
.. _API-intel-lr-context-deferred-alloc:

===============================
intel_lr_context_deferred_alloc
===============================

*man intel_lr_context_deferred_alloc(9)*

*4.6.0-rc1*

create the LRC specific bits of a context


Synopsis
========

.. c:function:: int intel_lr_context_deferred_alloc( struct intel_context * ctx, struct intel_engine_cs * ring )

Arguments
=========

``ctx``
    LR context to create.

``ring``
    engine to be used with the context.


Description
===========

This function can be called more than once, with different engines, if we plan to use the context with them. The context backing objects and the ringbuffers (specially the
ringbuffer backing objects) suck a lot of memory up, and that's why


the creation is a deferred call
===============================

it's better to make sure first that we need to use a given ring with the context.


Return
======

non-zero on error.
