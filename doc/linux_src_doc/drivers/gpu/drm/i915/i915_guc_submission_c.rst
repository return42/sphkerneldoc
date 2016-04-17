.. -*- coding: utf-8; mode: rst -*-

=====================
i915_guc_submission.c
=====================


.. _`guc-based-command-submission`:

GuC-based command submission
============================

i915_guc_client:
We use the term client to avoid confusion with contexts. A i915_guc_client is
equivalent to GuC object guc_context_desc. This context descriptor is
allocated from a pool of 1024 entries. Kernel driver will allocate doorbell
and workqueue for it. Also the process descriptor (guc_process_desc), which
is mapped to client space. So the client can write Work Item then ring the
doorbell.

To simplify the implementation, we allocate one gem object that contains all
pages for doorbell, process descriptor and workqueue.

The Scratch registers:
There are 16 MMIO-based registers start from 0xC180. The kernel driver writes
a value to the action register (SOFT_SCRATCH_0) along with any data. It then
triggers an interrupt on the GuC via another register write (0xC4C8).
Firmware writes a success/fail code back to the action register after
processes the request. The kernel driver polls waiting for this update and
then proceeds.
See :c:func:`host2guc_action`

Doorbells:
Doorbells are interrupts to uKernel. A doorbell is a single cache line (QW)
mapped into process space.

Work Items:
There are several types of work items that the host may place into a
workqueue, each with its own requirements and limitations. Currently only
WQ_TYPE_INORDER is needed to support legacy submission via GuC, which
represents in-order queue. The kernel driver packs ring tail pointer and an
ELSP context descriptor dword into Work Item.
See :c:func:`guc_add_workqueue_item`



.. _`i915_guc_submit`:

i915_guc_submit
===============

.. c:function:: int i915_guc_submit (struct i915_guc_client *client, struct drm_i915_gem_request *rq)

    Submit commands through GuC

    :param struct i915_guc_client \*client:
        the guc client where commands will go through

    :param struct drm_i915_gem_request \*rq:
        request associated with the commands



.. _`i915_guc_submit.return`:

Return
------

0 if succeed



.. _`gem_allocate_guc_obj`:

gem_allocate_guc_obj
====================

.. c:function:: struct drm_i915_gem_object *gem_allocate_guc_obj (struct drm_device *dev, u32 size)

    Allocate gem object for GuC usage

    :param struct drm_device \*dev:
        drm device

    :param u32 size:
        size of object



.. _`gem_allocate_guc_obj.description`:

Description
-----------

This is a wrapper to create a gem obj. In order to use it inside GuC, the
object needs to be pinned lifetime. Also we must pin it to gtt space other
than [0, GUC_WOPCM_TOP) because this range is reserved inside GuC.



.. _`gem_allocate_guc_obj.return`:

Return
------

A drm_i915_gem_object if successful, otherwise NULL.



.. _`gem_release_guc_obj`:

gem_release_guc_obj
===================

.. c:function:: void gem_release_guc_obj (struct drm_i915_gem_object *obj)

    Release gem object allocated for GuC usage

    :param struct drm_i915_gem_object \*obj:
        gem obj to be released



.. _`guc_client_alloc`:

guc_client_alloc
================

.. c:function:: struct i915_guc_client *guc_client_alloc (struct drm_device *dev, uint32_t priority, struct intel_context *ctx)

    Allocate an i915_guc_client

    :param struct drm_device \*dev:
        drm device

    :param uint32_t priority:
        four levels priority _CRITICAL, _HIGH, _NORMAL and _LOW
        The kernel client to replace ExecList submission is created with
        NORMAL priority. Priority of a client for scheduler can be HIGH,
        while a preemption context can use CRITICAL.

    :param struct intel_context \*ctx:
        the context that owns the client (we use the default render
        context)



.. _`guc_client_alloc.return`:

Return
------

An i915_guc_client object if success.



.. _`intel_guc_suspend`:

intel_guc_suspend
=================

.. c:function:: int intel_guc_suspend (struct drm_device *dev)

    notify GuC entering suspend state

    :param struct drm_device \*dev:
        drm device



.. _`intel_guc_resume`:

intel_guc_resume
================

.. c:function:: int intel_guc_resume (struct drm_device *dev)

    notify GuC resuming from suspend state

    :param struct drm_device \*dev:
        drm device

