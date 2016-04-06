
.. _API-intel-lr-context-size:

=====================
intel_lr_context_size
=====================

*man intel_lr_context_size(9)*

*4.6.0-rc1*

return the size of the context for an engine


Synopsis
========

.. c:function:: uint32_t intel_lr_context_size( struct intel_engine_cs * ring )

Arguments
=========

``ring``
    which engine to find the context size for


Description
===========

Each engine may require a different amount of space for a context image, so when allocating (or copying) an image, this function can be used to find the right size for the specific
engine.


Return
======

size (in bytes) of an engine-specific context image


Note
====

this size includes the HWSP, which is part of the context image in LRC mode, but does not include the “shared data page” used with GuC submission. The caller should account for
this if using the GuC.
