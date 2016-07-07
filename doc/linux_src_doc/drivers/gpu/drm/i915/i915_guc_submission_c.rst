.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_guc_submission.c

.. _`i915_guc_wq_check_space`:

i915_guc_wq_check_space
=======================

.. c:function:: int i915_guc_wq_check_space(struct drm_i915_gem_request *request)

    check that the GuC can accept a request

    :param struct drm_i915_gem_request \*request:
        request associated with the commands

.. _`i915_guc_wq_check_space.return`:

Return
------

0 if space is available
-EAGAIN if space is not currently available

This function must be called (and must return 0) before a request
is submitted to the GuC via \ :c:func:`i915_guc_submit`\  below. Once a result
of 0 has been returned, it remains valid until (but only until)
the next call to \ :c:func:`submit`\ .

This precheck allows the caller to determine in advance that space
will be available for the next submission before committing resources
to it, and helps avoid late failures with complicated recovery paths.

.. _`i915_guc_submit`:

i915_guc_submit
===============

.. c:function:: int i915_guc_submit(struct drm_i915_gem_request *rq)

    Submit commands through GuC

    :param struct drm_i915_gem_request \*rq:
        request associated with the commands

.. _`i915_guc_submit.return`:

Return
------

0 on success, otherwise an errno.
(Note: nonzero really shouldn't happen!)

The caller must have already called \ :c:func:`i915_guc_wq_check_space`\  above
with a result of 0 (success) since the last request submission. This
guarantees that there is space in the work queue for the new request,
so enqueuing the item cannot fail.

Bad Things Will Happen if the caller violates this protocol e.g. calls
\ :c:func:`submit`\  when \ :c:func:`check`\  says there's no space, or calls \ :c:func:`submit`\  multiple
times with no intervening \ :c:func:`check`\ .

The only error here arises if the doorbell hardware isn't functioning
as expected, which really shouln't happen.

.. _`gem_allocate_guc_obj`:

gem_allocate_guc_obj
====================

.. c:function:: struct drm_i915_gem_object *gem_allocate_guc_obj(struct drm_i915_private *dev_priv, u32 size)

    Allocate gem object for GuC usage

    :param struct drm_i915_private \*dev_priv:
        driver private data structure

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

.. c:function:: void gem_release_guc_obj(struct drm_i915_gem_object *obj)

    Release gem object allocated for GuC usage

    :param struct drm_i915_gem_object \*obj:
        gem obj to be released

.. _`guc_client_alloc`:

guc_client_alloc
================

.. c:function:: struct i915_guc_client *guc_client_alloc(struct drm_i915_private *dev_priv, uint32_t priority, struct i915_gem_context *ctx)

    Allocate an i915_guc_client

    :param struct drm_i915_private \*dev_priv:
        driver private data structure

    :param uint32_t priority:
        four levels priority \_CRITICAL, \_HIGH, \_NORMAL and \_LOW
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

.. c:function:: int intel_guc_suspend(struct drm_device *dev)

    notify GuC entering suspend state

    :param struct drm_device \*dev:
        drm device

.. _`intel_guc_resume`:

intel_guc_resume
================

.. c:function:: int intel_guc_resume(struct drm_device *dev)

    notify GuC resuming from suspend state

    :param struct drm_device \*dev:
        drm device

.. This file was automatic generated / don't edit.

