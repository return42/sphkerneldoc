.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_request.c

.. _`i915_request_alloc`:

i915_request_alloc
==================

.. c:function:: struct i915_request *i915_request_alloc(struct intel_engine_cs *engine, struct i915_gem_context *ctx)

    allocate a request structure

    :param engine:
        engine that we wish to issue the request on.
    :type engine: struct intel_engine_cs \*

    :param ctx:
        context that the request will be associated with.
    :type ctx: struct i915_gem_context \*

.. _`i915_request_alloc.description`:

Description
-----------

Returns a pointer to the allocated request if successful,
or an error code if not.

.. _`i915_request_await_object`:

i915_request_await_object
=========================

.. c:function:: int i915_request_await_object(struct i915_request *to, struct drm_i915_gem_object *obj, bool write)

    set this request to (async) wait upon a bo

    :param to:
        request we are wishing to use
    :type to: struct i915_request \*

    :param obj:
        object which may be in use on another ring.
    :type obj: struct drm_i915_gem_object \*

    :param write:
        whether the wait is on behalf of a writer
    :type write: bool

.. _`i915_request_await_object.description`:

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

.. _`i915_request_wait`:

i915_request_wait
=================

.. c:function:: long i915_request_wait(struct i915_request *rq, unsigned int flags, long timeout)

    wait until execution of request has finished

    :param rq:
        the request to wait upon
    :type rq: struct i915_request \*

    :param flags:
        how to wait
    :type flags: unsigned int

    :param timeout:
        how long to wait in jiffies
    :type timeout: long

.. _`i915_request_wait.description`:

Description
-----------

\ :c:func:`i915_request_wait`\  waits for the request to be completed, for a
maximum of \ ``timeout``\  jiffies (with MAX_SCHEDULE_TIMEOUT implying an
unbounded wait).

If the caller holds the struct_mutex, the caller must pass I915_WAIT_LOCKED
in via the flags, and vice versa if the struct_mutex is not held, the caller
must not specify that the wait is locked.

Returns the remaining time (in jiffies) if the request completed, which may
be zero or -ETIME if the request is unfinished after the timeout expires.
May return -EINTR is called with I915_WAIT_INTERRUPTIBLE and a signal is
pending before the request completes.

.. This file was automatic generated / don't edit.

