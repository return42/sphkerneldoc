
.. _API-gen8-init-indirectctx-bb:

========================
gen8_init_indirectctx_bb
========================

*man gen8_init_indirectctx_bb(9)*

*4.6.0-rc1*

initialize indirect ctx batch with WA


Synopsis
========

.. c:function:: int gen8_init_indirectctx_bb( struct intel_engine_cs * ring, struct i915_wa_ctx_bb * wa_ctx, uint32_t *const batch, uint32_t * offset )

Arguments
=========

``ring``
    only applicable for RCS

``wa_ctx``
    structure representing wa_ctx

``batch``
    page in which WA are loaded

``offset``
    This field specifies the start of the batch, it should be cache-aligned otherwise it is adjusted accordingly. Typically we only have one indirect_ctx and per_ctx batch buffer
    which are initialized at the beginning and shared across all contexts but this field helps us to have multiple batches at different offsets and select them based on a criteria.
    At the moment this batch always start at the beginning of the page and at this point we don't have multiple wa_ctx batch buffers.


offset
======

specifies start of the batch, should be cache-aligned. This is updated with the offset value received as input.


size
====

size of the batch in DWORDS but HW expects in terms of cachelines


Description
===========

The number of WA applied are not known at the beginning; we use this field to return the no of DWORDS written.

It is to be noted that this batch does not contain MI_BATCH_BUFFER_END so it adds NOOPs as padding to make it cacheline aligned. MI_BATCH_BUFFER_END will be added to perctx
batch and both of them together makes a complete batch buffer.


Return
======

non-zero if we exceed the PAGE_SIZE limit.
