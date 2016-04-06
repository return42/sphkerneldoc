
.. _API-gen8-init-perctx-bb:

===================
gen8_init_perctx_bb
===================

*man gen8_init_perctx_bb(9)*

*4.6.0-rc1*

initialize per ctx batch with WA


Synopsis
========

.. c:function:: int gen8_init_perctx_bb( struct intel_engine_cs * ring, struct i915_wa_ctx_bb * wa_ctx, uint32_t *const batch, uint32_t * offset )

Arguments
=========

``ring``
    only applicable for RCS

``wa_ctx``
    structure representing wa_ctx

``batch``
    page in which WA are loaded

``offset``
    This field specifies the start of this batch. This batch is started immediately after indirect_ctx batch. Since we ensure that indirect_ctx ends on a cacheline this batch is
    aligned automatically.


offset
======

specifies start of the batch, should be cache-aligned.


size
====

size of the batch in DWORDS but HW expects in terms of cachelines


Description
===========

The number of DWORDS written are returned using this field.

This batch is terminated with MI_BATCH_BUFFER_END and so we need not add padding to align it with cacheline as padding after MI_BATCH_BUFFER_END is redundant.
