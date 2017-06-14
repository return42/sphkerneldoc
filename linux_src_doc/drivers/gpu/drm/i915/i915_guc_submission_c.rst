.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_guc_submission.c

.. _`guc-based-command-submission`:

GuC-based command submission
============================

GuC client:
A i915_guc_client refers to a submission path through GuC. Currently, there
is only one of these (the execbuf_client) and this one is charged with all
submissions to the GuC. This struct is the owner of a doorbell, a process
descriptor and a workqueue (all of them inside a single gem object that
contains all required pages for these elements).

GuC stage descriptor:
During initialization, the driver allocates a static pool of 1024 such
descriptors, and shares them with the GuC.
Currently, there exists a 1:1 mapping between a i915_guc_client and a
guc_stage_desc (via the client's stage_id), so effectively only one
gets used. This stage descriptor lets the GuC know about the doorbell,
workqueue and process descriptor. Theoretically, it also lets the GuC
know about our HW contexts (context ID, etc...), but we actually
employ a kind of submission where the GuC uses the LRCA sent via the work
item instead (the single guc_stage_desc associated to execbuf client
contains information about the default kernel context only, but this is
essentially unused). This is called a "proxy" submission.

The Scratch registers:
There are 16 MMIO-based registers start from 0xC180. The kernel driver writes
a value to the action register (SOFT_SCRATCH_0) along with any data. It then
triggers an interrupt on the GuC via another register write (0xC4C8).
Firmware writes a success/fail code back to the action register after
processes the request. The kernel driver polls waiting for this update and
then proceeds.
See \ :c:func:`intel_guc_send`\ 

Doorbells:
Doorbells are interrupts to uKernel. A doorbell is a single cache line (QW)
mapped into process space.

Work Items:
There are several types of work items that the host may place into a
workqueue, each with its own requirements and limitations. Currently only
WQ_TYPE_INORDER is needed to support legacy submission via GuC, which
represents in-order queue. The kernel driver packs ring tail pointer and an
ELSP context descriptor dword into Work Item.
See \ :c:func:`guc_wq_item_append`\ 

ADS:
The Additional Data Struct (ADS) has pointers for different buffers used by
the GuC. One single gem object contains the ADS struct itself (guc_ads), the
scheduling policies (guc_policies), a structure describing a collection of
register sets (guc_mmio_reg_state) and some extra pages for the GuC to save
its internal state for sleep.

.. _`i915_guc_wq_reserve`:

i915_guc_wq_reserve
===================

.. c:function:: int i915_guc_wq_reserve(struct drm_i915_gem_request *request)

    reserve space in the GuC's workqueue

    :param struct drm_i915_gem_request \*request:
        request associated with the commands

.. _`i915_guc_wq_reserve.return`:

Return
------

0 if space is available
             -EAGAIN if space is not currently available

This function must be called (and must return 0) before a request
is submitted to the GuC via \ :c:func:`i915_guc_submit`\  below. Once a result
of 0 has been returned, it must be balanced by a corresponding
call to \ :c:func:`submit`\ .

Reservation allows the caller to determine in advance that space
will be available for the next submission before committing resources
to it, and helps avoid late failures with complicated recovery paths.

.. _`__i915_guc_submit`:

__i915_guc_submit
=================

.. c:function:: void __i915_guc_submit(struct drm_i915_gem_request *rq)

    Submit commands through GuC

    :param struct drm_i915_gem_request \*rq:
        request associated with the commands

.. _`__i915_guc_submit.description`:

Description
-----------

The caller must have already called \ :c:func:`i915_guc_wq_reserve`\  above with
a result of 0 (success), guaranteeing that there is space in the work
queue for the new request, so enqueuing the item cannot fail.

Bad Things Will Happen if the caller violates this protocol e.g. calls
\ :c:func:`submit`\  when \ :c:func:`_reserve`\  says there's no space, or calls \ :c:func:`_submit`\ 
a different number of times from (successful) calls to \ :c:func:`_reserve`\ .

The only error here arises if the doorbell hardware isn't functioning
as expected, which really shouln't happen.

.. _`intel_guc_allocate_vma`:

intel_guc_allocate_vma
======================

.. c:function:: struct i915_vma *intel_guc_allocate_vma(struct intel_guc *guc, u32 size)

    Allocate a GGTT VMA for GuC usage

    :param struct intel_guc \*guc:
        the guc

    :param u32 size:
        size of area to allocate (both virtual space and memory)

.. _`intel_guc_allocate_vma.description`:

Description
-----------

This is a wrapper to create an object for use with the GuC. In order to
use it inside the GuC, an object needs to be pinned lifetime, so we allocate
both some backing storage and a range inside the Global GTT. We must pin
it in the GGTT somewhere other than than [0, GUC_WOPCM_TOP) because that
range is reserved inside GuC.

.. _`intel_guc_allocate_vma.return`:

Return
------

A i915_vma if successful, otherwise an ERR_PTR.

.. _`guc_client_alloc`:

guc_client_alloc
================

.. c:function:: struct i915_guc_client *guc_client_alloc(struct drm_i915_private *dev_priv, uint32_t engines, uint32_t priority, struct i915_gem_context *ctx)

    Allocate an i915_guc_client

    :param struct drm_i915_private \*dev_priv:
        driver private data structure

    :param uint32_t engines:
        The set of engines to enable for this client

    :param uint32_t priority:
        four levels priority _CRITICAL, _HIGH, _NORMAL and _LOW
        The kernel client to replace ExecList submission is created with
        NORMAL priority. Priority of a client for scheduler can be HIGH,
        while a preemption context can use CRITICAL.

    :param struct i915_gem_context \*ctx:
        the context that owns the client (we use the default render
        context)

.. _`guc_client_alloc.return`:

Return
------

An i915_guc_client object if success, else NULL.

.. _`intel_guc_suspend`:

intel_guc_suspend
=================

.. c:function:: int intel_guc_suspend(struct drm_i915_private *dev_priv)

    notify GuC entering suspend state

    :param struct drm_i915_private \*dev_priv:
        i915 device private

.. _`intel_guc_resume`:

intel_guc_resume
================

.. c:function:: int intel_guc_resume(struct drm_i915_private *dev_priv)

    notify GuC resuming from suspend state

    :param struct drm_i915_private \*dev_priv:
        i915 device private

.. This file was automatic generated / don't edit.

