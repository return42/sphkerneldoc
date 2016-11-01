.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_request.c

.. _`i915_gem_request_alloc`:

i915_gem_request_alloc
======================

.. c:function:: struct drm_i915_gem_request *i915_gem_request_alloc(struct intel_engine_cs *engine, struct i915_gem_context *ctx)

    allocate a request structure

    :param struct intel_engine_cs \*engine:
        engine that we wish to issue the request on.

    :param struct i915_gem_context \*ctx:
        context that the request will be associated with.
        This can be NULL if the request is not directly related to
        any specific user context, in which case this function will
        choose an appropriate context to use.

.. _`i915_gem_request_alloc.description`:

Description
-----------

Returns a pointer to the allocated request if successful,
or an error code if not.

.. _`i915_gem_request_await_object`:

i915_gem_request_await_object
=============================

.. c:function:: int i915_gem_request_await_object(struct drm_i915_gem_request *to, struct drm_i915_gem_object *obj, bool write)

    set this request to (async) wait upon a bo

    :param struct drm_i915_gem_request \*to:
        request we are wishing to use

    :param struct drm_i915_gem_object \*obj:
        object which may be in use on another ring.

    :param bool write:
        *undescribed*

.. _`i915_gem_request_await_object.description`:

Description
-----------

This code is meant to abstract object synchronization with the GPU.
Conceptually we serialise writes between engines inside the GPU.
We only allow one engine to write into a buffer at any time, but
multiple readers. To ensure each has a coherent view of memory, we must:

- If there is an outstanding write request to the object, the new
request must wait for it to complete (either CPU or in hw, requests
on the same ring will be naturally ordered).

- If we are a write request (pending_write_domain is set), the new
request must wait for outstanding read requests to complete.

Returns 0 if successful, else propagates up the lower layer error.

.. _`i915_wait_request`:

i915_wait_request
=================

.. c:function:: int i915_wait_request(struct drm_i915_gem_request *req, unsigned int flags, s64 *timeout, struct intel_rps_client *rps)

    wait until execution of request has finished

    :param struct drm_i915_gem_request \*req:
        duh!

    :param unsigned int flags:
        how to wait

    :param s64 \*timeout:
        in - how long to wait (NULL forever); out - how much time remaining

    :param struct intel_rps_client \*rps:
        client to charge for RPS boosting

.. _`i915_wait_request.note`:

Note
----

It is of utmost importance that the passed in seqno and reset_counter
values have been read by the caller in an smp safe manner. Where read-side
locks are involved, it is sufficient to read the reset_counter before
unlocking the lock that protects the seqno. For lockless tricks, the
reset_counter \_must\_ be read before, and an appropriate smp_rmb must be
inserted.

Returns 0 if the request was found within the alloted time. Else returns the
errno with remaining time filled in timeout argument.

.. This file was automatic generated / don't edit.

