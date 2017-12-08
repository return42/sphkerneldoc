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

.. _`i915_guc_submit`:

i915_guc_submit
===============

.. c:function:: void i915_guc_submit(struct intel_engine_cs *engine)

    Submit commands through GuC

    :param struct intel_engine_cs \*engine:
        engine associated with the commands

.. _`i915_guc_submit.description`:

Description
-----------

The only error here arises if the doorbell hardware isn't functioning
as expected, which really shouln't happen.

.. _`guc_client_alloc`:

guc_client_alloc
================

.. c:function:: struct i915_guc_client *guc_client_alloc(struct drm_i915_private *dev_priv, u32 engines, u32 priority, struct i915_gem_context *ctx)

    Allocate an i915_guc_client

    :param struct drm_i915_private \*dev_priv:
        driver private data structure

    :param u32 engines:
        The set of engines to enable for this client

    :param u32 priority:
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

.. This file was automatic generated / don't edit.

