.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma-buf/dma-fence.c

.. _`dma-fences-overview`:

DMA fences overview
===================

DMA fences, represented by \ :c:type:`struct dma_fence <dma_fence>`\ , are the kernel internal
synchronization primitive for DMA operations like GPU rendering, video
encoding/decoding, or displaying buffers on a screen.

A fence is initialized using \ :c:func:`dma_fence_init`\  and completed using
\ :c:func:`dma_fence_signal`\ . Fences are associated with a context, allocated through
\ :c:func:`dma_fence_context_alloc`\ , and all fences on the same context are
fully ordered.

Since the purposes of fences is to facilitate cross-device and
cross-application synchronization, there's multiple ways to use one:

- Individual fences can be exposed as a \ :c:type:`struct sync_file <sync_file>`\ , accessed as a file
  descriptor from userspace, created by calling \ :c:func:`sync_file_create`\ . This is
  called explicit fencing, since userspace passes around explicit
  synchronization points.

- Some subsystems also have their own explicit fencing primitives, like
  \ :c:type:`struct drm_syncobj <drm_syncobj>`\ . Compared to \ :c:type:`struct sync_file <sync_file>`\ , a \ :c:type:`struct drm_syncobj <drm_syncobj>`\  allows the underlying
  fence to be updated.

- Then there's also implicit fencing, where the synchronization points are
  implicitly passed around as part of shared \ :c:type:`struct dma_buf <dma_buf>`\  instances. Such
  implicit fences are stored in \ :c:type:`struct reservation_object <reservation_object>`\  through the
  \ :c:type:`dma_buf.resv <dma_buf>`\  pointer.

.. _`dma_fence_context_alloc`:

dma_fence_context_alloc
=======================

.. c:function:: u64 dma_fence_context_alloc(unsigned num)

    allocate an array of fence contexts

    :param num:
        amount of contexts to allocate
    :type num: unsigned

.. _`dma_fence_context_alloc.description`:

Description
-----------

This function will return the first index of the number of fence contexts
allocated.  The fence context is used for setting \ :c:type:`dma_fence.context <dma_fence>`\  to a
unique number by passing the context to \ :c:func:`dma_fence_init`\ .

.. _`dma_fence_signal_locked`:

dma_fence_signal_locked
=======================

.. c:function:: int dma_fence_signal_locked(struct dma_fence *fence)

    signal completion of a fence

    :param fence:
        the fence to signal
    :type fence: struct dma_fence \*

.. _`dma_fence_signal_locked.description`:

Description
-----------

Signal completion for software callbacks on a fence, this will unblock
\ :c:func:`dma_fence_wait`\  calls and run all the callbacks added with
\ :c:func:`dma_fence_add_callback`\ . Can be called multiple times, but since a fence
can only go from the unsignaled to the signaled state and not back, it will
only be effective the first time.

Unlike \ :c:func:`dma_fence_signal`\ , this function must be called with \ :c:type:`dma_fence.lock <dma_fence>`\ 
held.

Returns 0 on success and a negative error value when \ ``fence``\  has been
signalled already.

.. _`dma_fence_signal`:

dma_fence_signal
================

.. c:function:: int dma_fence_signal(struct dma_fence *fence)

    signal completion of a fence

    :param fence:
        the fence to signal
    :type fence: struct dma_fence \*

.. _`dma_fence_signal.description`:

Description
-----------

Signal completion for software callbacks on a fence, this will unblock
\ :c:func:`dma_fence_wait`\  calls and run all the callbacks added with
\ :c:func:`dma_fence_add_callback`\ . Can be called multiple times, but since a fence
can only go from the unsignaled to the signaled state and not back, it will
only be effective the first time.

Returns 0 on success and a negative error value when \ ``fence``\  has been
signalled already.

.. _`dma_fence_wait_timeout`:

dma_fence_wait_timeout
======================

.. c:function:: signed long dma_fence_wait_timeout(struct dma_fence *fence, bool intr, signed long timeout)

    sleep until the fence gets signaled or until timeout elapses

    :param fence:
        the fence to wait on
    :type fence: struct dma_fence \*

    :param intr:
        if true, do an interruptible wait
    :type intr: bool

    :param timeout:
        timeout value in jiffies, or MAX_SCHEDULE_TIMEOUT
    :type timeout: signed long

.. _`dma_fence_wait_timeout.description`:

Description
-----------

Returns -ERESTARTSYS if interrupted, 0 if the wait timed out, or the
remaining timeout in jiffies on success. Other error values may be
returned on custom implementations.

Performs a synchronous wait on this fence. It is assumed the caller
directly or indirectly (buf-mgr between reservation and committing)
holds a reference to the fence, otherwise the fence might be
freed before return, resulting in undefined behavior.

See also \ :c:func:`dma_fence_wait`\  and \ :c:func:`dma_fence_wait_any_timeout`\ .

.. _`dma_fence_release`:

dma_fence_release
=================

.. c:function:: void dma_fence_release(struct kref *kref)

    default relese function for fences

    :param kref:
        \ :c:type:`dma_fence.recfount <dma_fence>`\ 
    :type kref: struct kref \*

.. _`dma_fence_release.description`:

Description
-----------

This is the default release functions for \ :c:type:`struct dma_fence <dma_fence>`\ . Drivers shouldn't call
this directly, but instead call \ :c:func:`dma_fence_put`\ .

.. _`dma_fence_free`:

dma_fence_free
==============

.. c:function:: void dma_fence_free(struct dma_fence *fence)

    default release function for \ :c:type:`struct dma_fence <dma_fence>`\ .

    :param fence:
        fence to release
    :type fence: struct dma_fence \*

.. _`dma_fence_free.description`:

Description
-----------

This is the default implementation for \ :c:type:`dma_fence_ops.release <dma_fence_ops>`\ . It calls
\ :c:func:`kfree_rcu`\  on \ ``fence``\ .

.. _`dma_fence_enable_sw_signaling`:

dma_fence_enable_sw_signaling
=============================

.. c:function:: void dma_fence_enable_sw_signaling(struct dma_fence *fence)

    enable signaling on fence

    :param fence:
        the fence to enable
    :type fence: struct dma_fence \*

.. _`dma_fence_enable_sw_signaling.description`:

Description
-----------

This will request for sw signaling to be enabled, to make the fence
complete as soon as possible. This calls \ :c:type:`dma_fence_ops.enable_signaling <dma_fence_ops>`\ 
internally.

.. _`dma_fence_add_callback`:

dma_fence_add_callback
======================

.. c:function:: int dma_fence_add_callback(struct dma_fence *fence, struct dma_fence_cb *cb, dma_fence_func_t func)

    add a callback to be called when the fence is signaled

    :param fence:
        the fence to wait on
    :type fence: struct dma_fence \*

    :param cb:
        the callback to register
    :type cb: struct dma_fence_cb \*

    :param func:
        the function to call
    :type func: dma_fence_func_t

.. _`dma_fence_add_callback.description`:

Description
-----------

\ ``cb``\  will be initialized by \ :c:func:`dma_fence_add_callback`\ , no initialization
by the caller is required. Any number of callbacks can be registered
to a fence, but a callback can only be registered to one fence at a time.

Note that the callback can be called from an atomic context.  If
fence is already signaled, this function will return -ENOENT (and
*not* call the callback).

Add a software callback to the fence. Same restrictions apply to
refcount as it does to \ :c:func:`dma_fence_wait`\ , however the caller doesn't need to
keep a refcount to fence afterward \ :c:func:`dma_fence_add_callback`\  has returned:
when software access is enabled, the creator of the fence is required to keep
the fence alive until after it signals with \ :c:func:`dma_fence_signal`\ . The callback
itself can be called from irq context.

Returns 0 in case of success, -ENOENT if the fence is already signaled
and -EINVAL in case of error.

.. _`dma_fence_get_status`:

dma_fence_get_status
====================

.. c:function:: int dma_fence_get_status(struct dma_fence *fence)

    returns the status upon completion

    :param fence:
        the dma_fence to query
    :type fence: struct dma_fence \*

.. _`dma_fence_get_status.description`:

Description
-----------

This wraps \ :c:func:`dma_fence_get_status_locked`\  to return the error status
condition on a signaled fence. See \ :c:func:`dma_fence_get_status_locked`\  for more
details.

Returns 0 if the fence has not yet been signaled, 1 if the fence has
been signaled without an error condition, or a negative error code
if the fence has been completed in err.

.. _`dma_fence_remove_callback`:

dma_fence_remove_callback
=========================

.. c:function:: bool dma_fence_remove_callback(struct dma_fence *fence, struct dma_fence_cb *cb)

    remove a callback from the signaling list

    :param fence:
        the fence to wait on
    :type fence: struct dma_fence \*

    :param cb:
        the callback to remove
    :type cb: struct dma_fence_cb \*

.. _`dma_fence_remove_callback.description`:

Description
-----------

Remove a previously queued callback from the fence. This function returns
true if the callback is successfully removed, or false if the fence has
already been signaled.

*WARNING*:
Cancelling a callback should only be done if you really know what you're
doing, since deadlocks and race conditions could occur all too easily. For
this reason, it should only ever be done on hardware lockup recovery,
with a reference held to the fence.

Behaviour is undefined if \ ``cb``\  has not been added to \ ``fence``\  using
\ :c:func:`dma_fence_add_callback`\  beforehand.

.. _`dma_fence_default_wait`:

dma_fence_default_wait
======================

.. c:function:: signed long dma_fence_default_wait(struct dma_fence *fence, bool intr, signed long timeout)

    default sleep until the fence gets signaled or until timeout elapses

    :param fence:
        the fence to wait on
    :type fence: struct dma_fence \*

    :param intr:
        if true, do an interruptible wait
    :type intr: bool

    :param timeout:
        timeout value in jiffies, or MAX_SCHEDULE_TIMEOUT
    :type timeout: signed long

.. _`dma_fence_default_wait.description`:

Description
-----------

Returns -ERESTARTSYS if interrupted, 0 if the wait timed out, or the
remaining timeout in jiffies on success. If timeout is zero the value one is
returned if the fence is already signaled for consistency with other
functions taking a jiffies timeout.

.. _`dma_fence_wait_any_timeout`:

dma_fence_wait_any_timeout
==========================

.. c:function:: signed long dma_fence_wait_any_timeout(struct dma_fence **fences, uint32_t count, bool intr, signed long timeout, uint32_t *idx)

    sleep until any fence gets signaled or until timeout elapses

    :param fences:
        array of fences to wait on
    :type fences: struct dma_fence \*\*

    :param count:
        number of fences to wait on
    :type count: uint32_t

    :param intr:
        if true, do an interruptible wait
    :type intr: bool

    :param timeout:
        timeout value in jiffies, or MAX_SCHEDULE_TIMEOUT
    :type timeout: signed long

    :param idx:
        used to store the first signaled fence index, meaningful only on
        positive return
    :type idx: uint32_t \*

.. _`dma_fence_wait_any_timeout.description`:

Description
-----------

Returns -EINVAL on custom fence wait implementation, -ERESTARTSYS if
interrupted, 0 if the wait timed out, or the remaining timeout in jiffies
on success.

Synchronous waits for the first fence in the array to be signaled. The
caller needs to hold a reference to all fences in the array, otherwise a
fence might be freed before return, resulting in undefined behavior.

See also \ :c:func:`dma_fence_wait`\  and \ :c:func:`dma_fence_wait_timeout`\ .

.. _`dma_fence_init`:

dma_fence_init
==============

.. c:function:: void dma_fence_init(struct dma_fence *fence, const struct dma_fence_ops *ops, spinlock_t *lock, u64 context, unsigned seqno)

    Initialize a custom fence.

    :param fence:
        the fence to initialize
    :type fence: struct dma_fence \*

    :param ops:
        the dma_fence_ops for operations on this fence
    :type ops: const struct dma_fence_ops \*

    :param lock:
        the irqsafe spinlock to use for locking this fence
    :type lock: spinlock_t \*

    :param context:
        the execution context this fence is run on
    :type context: u64

    :param seqno:
        a linear increasing sequence number for this context
    :type seqno: unsigned

.. _`dma_fence_init.description`:

Description
-----------

Initializes an allocated fence, the caller doesn't have to keep its
refcount after committing with this fence, but it will need to hold a
refcount again if \ :c:type:`dma_fence_ops.enable_signaling <dma_fence_ops>`\  gets called.

context and seqno are used for easy comparison between fences, allowing
to check which fence is later by simply using \ :c:func:`dma_fence_later`\ .

.. This file was automatic generated / don't edit.

