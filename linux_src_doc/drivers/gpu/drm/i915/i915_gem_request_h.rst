.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_gem_request.h

.. _`i915_gem_request_global_seqno`:

i915_gem_request_global_seqno
=============================

.. c:function:: u32 i915_gem_request_global_seqno(const struct drm_i915_gem_request *request)

    report the current global seqno \ ``request``\  - the request

    :param const struct drm_i915_gem_request \*request:
        *undescribed*

.. _`i915_gem_request_global_seqno.description`:

Description
-----------

A request is assigned a global seqno only when it is on the hardware
execution queue. The global seqno can be used to maintain a list of
requests on the same engine in retirement order, for example for
constructing a priority queue for waiting. Prior to its execution, or
if it is subsequently removed in the event of preemption, its global
seqno is zero. As both insertion and removal from the execution queue
may operate in IRQ context, it is not guarded by the usual struct_mutex
BKL. Instead those relying on the global seqno must be prepared for its
value to change between reads. Only when the request is complete can
the global seqno be stable (due to the memory barriers on submitting
the commands to the hardware to write the breadcrumb, if the HWS shows
that it has passed the global seqno and the global seqno is unchanged
after the read, it is indeed complete).

.. _`i915_seqno_passed`:

i915_seqno_passed
=================

.. c:function:: bool i915_seqno_passed(u32 seq1, u32 seq2)

    :param u32 seq1:
        *undescribed*

    :param u32 seq2:
        *undescribed*

.. _`init_request_active`:

init_request_active
===================

.. c:function:: void init_request_active(struct i915_gem_active *active, i915_gem_retire_fn retire)

    prepares the activity tracker for use \ ``active``\  - the active tracker \ ``func``\  - a callback when then the tracker is retired (becomes idle), can be NULL

    :param struct i915_gem_active \*active:
        *undescribed*

    :param i915_gem_retire_fn retire:
        *undescribed*

.. _`init_request_active.description`:

Description
-----------

init_request_active() prepares the embedded \ ``active``\  struct for use as
an activity tracker, that is for tracking the last known active request
associated with it. When the last request becomes idle, when it is retired
after completion, the optional callback \ ``func``\  is invoked.

.. _`i915_gem_active_set`:

i915_gem_active_set
===================

.. c:function:: void i915_gem_active_set(struct i915_gem_active *active, struct drm_i915_gem_request *request)

    updates the tracker to watch the current request \ ``active``\  - the active tracker \ ``request``\  - the request to watch

    :param struct i915_gem_active \*active:
        *undescribed*

    :param struct drm_i915_gem_request \*request:
        *undescribed*

.. _`i915_gem_active_set.description`:

Description
-----------

i915_gem_active_set() watches the given \ ``request``\  for completion. Whilst
that \ ``request``\  is busy, the \ ``active``\  reports busy. When that \ ``request``\  is
retired, the \ ``active``\  tracker is updated to report idle.

.. _`i915_gem_active_set_retire_fn`:

i915_gem_active_set_retire_fn
=============================

.. c:function:: void i915_gem_active_set_retire_fn(struct i915_gem_active *active, i915_gem_retire_fn fn, struct mutex *mutex)

    updates the retirement callback \ ``active``\  - the active tracker \ ``fn``\  - the routine called when the request is retired \ ``mutex``\  - struct_mutex used to guard retirements

    :param struct i915_gem_active \*active:
        *undescribed*

    :param i915_gem_retire_fn fn:
        *undescribed*

    :param struct mutex \*mutex:
        *undescribed*

.. _`i915_gem_active_set_retire_fn.description`:

Description
-----------

i915_gem_active_set_retire_fn() updates the function pointer that
is called when the final request associated with the \ ``active``\  tracker
is retired.

.. _`i915_gem_active_raw`:

i915_gem_active_raw
===================

.. c:function:: struct drm_i915_gem_request *i915_gem_active_raw(const struct i915_gem_active *active, struct mutex *mutex)

    return the active request \ ``active``\  - the active tracker

    :param const struct i915_gem_active \*active:
        *undescribed*

    :param struct mutex \*mutex:
        *undescribed*

.. _`i915_gem_active_raw.description`:

Description
-----------

i915_gem_active_raw() returns the current request being tracked, or NULL.
It does not obtain a reference on the request for the caller, so the caller
must hold struct_mutex.

.. _`i915_gem_active_peek`:

i915_gem_active_peek
====================

.. c:function:: struct drm_i915_gem_request *i915_gem_active_peek(const struct i915_gem_active *active, struct mutex *mutex)

    report the active request being monitored \ ``active``\  - the active tracker

    :param const struct i915_gem_active \*active:
        *undescribed*

    :param struct mutex \*mutex:
        *undescribed*

.. _`i915_gem_active_peek.description`:

Description
-----------

i915_gem_active_peek() returns the current request being tracked if
still active, or NULL. It does not obtain a reference on the request
for the caller, so the caller must hold struct_mutex.

.. _`i915_gem_active_get`:

i915_gem_active_get
===================

.. c:function:: struct drm_i915_gem_request *i915_gem_active_get(const struct i915_gem_active *active, struct mutex *mutex)

    return a reference to the active request \ ``active``\  - the active tracker

    :param const struct i915_gem_active \*active:
        *undescribed*

    :param struct mutex \*mutex:
        *undescribed*

.. _`i915_gem_active_get.description`:

Description
-----------

i915_gem_active_get() returns a reference to the active request, or NULL
if the active tracker is idle. The caller must hold struct_mutex.

.. _`__i915_gem_active_get_rcu`:

__i915_gem_active_get_rcu
=========================

.. c:function:: struct drm_i915_gem_request *__i915_gem_active_get_rcu(const struct i915_gem_active *active)

    return a reference to the active request \ ``active``\  - the active tracker

    :param const struct i915_gem_active \*active:
        *undescribed*

.. _`__i915_gem_active_get_rcu.description`:

Description
-----------

__i915_gem_active_get() returns a reference to the active request, or NULL
if the active tracker is idle. The caller must hold the RCU read lock, but
the returned pointer is safe to use outside of RCU.

.. _`i915_gem_active_get_unlocked`:

i915_gem_active_get_unlocked
============================

.. c:function:: struct drm_i915_gem_request *i915_gem_active_get_unlocked(const struct i915_gem_active *active)

    return a reference to the active request \ ``active``\  - the active tracker

    :param const struct i915_gem_active \*active:
        *undescribed*

.. _`i915_gem_active_get_unlocked.description`:

Description
-----------

i915_gem_active_get_unlocked() returns a reference to the active request,
or NULL if the active tracker is idle. The reference is obtained under RCU,
so no locking is required by the caller.

The reference should be freed with \ :c:func:`i915_gem_request_put`\ .

.. _`i915_gem_active_isset`:

i915_gem_active_isset
=====================

.. c:function:: bool i915_gem_active_isset(const struct i915_gem_active *active)

    report whether the active tracker is assigned \ ``active``\  - the active tracker

    :param const struct i915_gem_active \*active:
        *undescribed*

.. _`i915_gem_active_isset.description`:

Description
-----------

i915_gem_active_isset() returns true if the active tracker is currently
assigned to a request. Due to the lazy retiring, that request may be idle
and this may report stale information.

.. _`i915_gem_active_wait`:

i915_gem_active_wait
====================

.. c:function:: int i915_gem_active_wait(const struct i915_gem_active *active, unsigned int flags)

    waits until the request is completed \ ``active``\  - the active request on which to wait \ ``flags``\  - how to wait \ ``timeout``\  - how long to wait at most \ ``rps``\  - userspace client to charge for a waitboost

    :param const struct i915_gem_active \*active:
        *undescribed*

    :param unsigned int flags:
        *undescribed*

.. _`i915_gem_active_wait.description`:

Description
-----------

i915_gem_active_wait() waits until the request is completed before
returning, without requiring any locks to be held. Note that it does not
retire any requests before returning.

This function relies on RCU in order to acquire the reference to the active
request without holding any locks. See \__i915_gem_active_get_rcu() for the
glory details on how that is managed. Once the reference is acquired, we
can then wait upon the request, and afterwards release our reference,
free of any locking.

This function wraps \ :c:func:`i915_wait_request`\ , see it for the full details on
the arguments.

Returns 0 if successful, or a negative error code.

.. _`i915_gem_active_retire`:

i915_gem_active_retire
======================

.. c:function:: int i915_gem_active_retire(struct i915_gem_active *active, struct mutex *mutex)

    waits until the request is retired \ ``active``\  - the active request on which to wait

    :param struct i915_gem_active \*active:
        *undescribed*

    :param struct mutex \*mutex:
        *undescribed*

.. _`i915_gem_active_retire.description`:

Description
-----------

i915_gem_active_retire() waits until the request is completed,
and then ensures that at least the retirement handler for this
\ ``active``\  tracker is called before returning. If the \ ``active``\ 
tracker is idle, the function returns immediately.

.. This file was automatic generated / don't edit.

