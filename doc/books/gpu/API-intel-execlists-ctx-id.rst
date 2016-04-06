
.. _API-intel-execlists-ctx-id:

======================
intel_execlists_ctx_id
======================

*man intel_execlists_ctx_id(9)*

*4.6.0-rc1*

get the Execlists Context ID


Synopsis
========

.. c:function:: u32 intel_execlists_ctx_id( struct intel_context * ctx, struct intel_engine_cs * ring )

Arguments
=========

``ctx``
    Context to get the ID for

``ring``
    Engine to get the ID for


Description
===========

Do not confuse with ctx->id! Unfortunately we have a name overload


here
====

the old context ID we pass to userspace as a handler so that they can refer to a context, and the new context ID we pass to the ELSP so that the GPU can inform us of the context
status via interrupts.

The context ID is a portion of the context descriptor, so we can just extract the required part from the cached descriptor.


Return
======

20-bits globally unique context ID.
