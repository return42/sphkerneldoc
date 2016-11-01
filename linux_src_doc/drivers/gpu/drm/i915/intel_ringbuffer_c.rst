.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_ringbuffer.c

.. _`intel_emit_post_sync_nonzero_flush`:

intel_emit_post_sync_nonzero_flush
==================================

.. c:function:: int intel_emit_post_sync_nonzero_flush(struct drm_i915_gem_request *req)

    zero post-sync operation, for implementing two workarounds on gen6.  From section 1.4.7.1 "PIPE_CONTROL" of the Sandy Bridge PRM volume 2 part 1:

    :param struct drm_i915_gem_request \*req:
        *undescribed*

.. _`intel_emit_post_sync_nonzero_flush.description`:

Description
-----------

[DevSNB-C+{W/A}] Before any depth stall flush (including those
produced by non-pipelined state commands), software needs to first
send a PIPE_CONTROL with no bits set except Post-Sync Operation !=
0.

[Dev-SNB{W/A}]: Before a PIPE_CONTROL with Write Cache Flush Enable
=1, a PIPE_CONTROL with any non-zero post-sync-op is required.

.. _`intel_emit_post_sync_nonzero_flush.and-the-workaround-for-these-two-requires-this-workaround-first`:

And the workaround for these two requires this workaround first
---------------------------------------------------------------


[Dev-SNB{W/A}]: Pipe-control with CS-stall bit set must be sent
BEFORE the pipe-control with a post-sync op and no write-cache
flushes.

And this last workaround is tricky because of the requirements on
that bit.  From section 1.4.7.2.3 "Stall" of the Sandy Bridge PRM

.. _`intel_emit_post_sync_nonzero_flush.volume-2-part-1`:

volume 2 part 1
---------------


"1 of the following must also be set:
- Render Target Cache Flush Enable ([12] of DW1)
- Depth Cache Flush Enable ([0] of DW1)
- Stall at Pixel Scoreboard ([1] of DW1)
- Depth Stall ([13] of DW1)
- Post-Sync Operation ([13] of DW1)
- Notify Enable ([8] of DW1)"

The cache flushes require the workaround flush that triggered this
one, so we can't use it.  Depth stall would trigger the same.
Post-sync nonzero is what triggered this second workaround, so we
can't use that one either.  Notify enable is IRQs, which aren't
really our business.  That leaves only stall at scoreboard.

.. _`gen6_sema_emit_request`:

gen6_sema_emit_request
======================

.. c:function:: int gen6_sema_emit_request(struct drm_i915_gem_request *req)

    Update the semaphore mailbox registers

    :param struct drm_i915_gem_request \*req:
        *undescribed*

.. _`gen6_sema_emit_request.description`:

Description
-----------

@request - request to write to the ring

Update the mailbox registers in the \*other\* rings with the current seqno.
This acts like a signal in the canonical semaphore.

.. _`gen8_ring_sync_to`:

gen8_ring_sync_to
=================

.. c:function:: int gen8_ring_sync_to(struct drm_i915_gem_request *req, struct drm_i915_gem_request *signal)

    sync the waiter to the signaller on seqno

    :param struct drm_i915_gem_request \*req:
        *undescribed*

    :param struct drm_i915_gem_request \*signal:
        *undescribed*

.. _`gen8_ring_sync_to.description`:

Description
-----------

@waiter - ring that is waiting
\ ``signaller``\  - ring which has, or will signal
\ ``seqno``\  - seqno which the waiter will block on

.. _`intel_init_bsd2_ring_buffer`:

intel_init_bsd2_ring_buffer
===========================

.. c:function:: int intel_init_bsd2_ring_buffer(struct intel_engine_cs *engine)

    :param struct intel_engine_cs \*engine:
        *undescribed*

.. This file was automatic generated / don't edit.

