.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_trace.h

.. _`i915_ppgtt_create-and-i915_ppgtt_release-tracepoints`:

i915_ppgtt_create and i915_ppgtt_release tracepoints
====================================================

With full ppgtt enabled each process using drm will allocate at least one
translation table. With these traces it is possible to keep track of the
allocation and of the lifetime of the tables; this can be used during
testing/debug to verify that we are not leaking ppgtts.
These traces identify the ppgtt through the vm pointer, which is also printed
by the i915_vma_bind and i915_vma_unbind tracepoints.

.. _`i915_context_create-and-i915_context_free-tracepoints`:

i915_context_create and i915_context_free tracepoints
=====================================================

These tracepoints are used to track creation and deletion of contexts.
If full ppgtt is enabled, they also print the address of the vm assigned to
the context.

.. _`switch_mm-tracepoint`:

switch_mm tracepoint
====================

This tracepoint allows tracking of the mm switch, which is an important point
in the lifetime of the vm in the legacy submission path. This tracepoint is
called only if full ppgtt is enabled.

.. This file was automatic generated / don't edit.

