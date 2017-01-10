.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma-buf/dma-fence.c

.. _`dma_fence_context_alloc`:

dma_fence_context_alloc
=======================

.. c:function:: u64 dma_fence_context_alloc(unsigned num)

    allocate an array of fence contexts

    :param unsigned num:
        [in]    amount of contexts to allocate

.. _`dma_fence_context_alloc.description`:

Description
-----------

This function will return the first index of the number of fences allocated.
The fence context is used for setting fence->context to a unique number.

.. _`dma_fence_signal_locked`:

dma_fence_signal_locked
=======================

.. c:function:: int dma_fence_signal_locked(struct dma_fence *fence)

    signal completion of a fence

    :param struct dma_fence \*fence:
        the fence to signal

.. _`dma_fence_signal_locked.description`:

Description
-----------

Signal completion for software callbacks on a fence, this will unblock
\ :c:func:`dma_fence_wait`\  calls and run all the callbacks added with
\ :c:func:`dma_fence_add_callback`\ . Can be called multiple times, but since a fence
can only go from unsignaled to signaled state, it will only be effective
the first time.

Unlike dma_fence_signal, this function must be called with fence->lock held.

.. _`dma_fence_signal`:

dma_fence_signal
================

.. c:function:: int dma_fence_signal(struct dma_fence *fence)

    signal completion of a fence

    :param struct dma_fence \*fence:
        the fence to signal

.. _`dma_fence_signal.description`:

Description
-----------

Signal completion for software callbacks on a fence, this will unblock
\ :c:func:`dma_fence_wait`\  calls and run all the callbacks added with
\ :c:func:`dma_fence_add_callback`\ . Can be called multiple times, but since a fence
can only go from unsignaled to signaled state, it will only be effective
the first time.

.. _`dma_fence_wait_timeout`:

dma_fence_wait_timeout
======================

.. c:function:: signed long dma_fence_wait_timeout(struct dma_fence *fence, bool intr, signed long timeout)

    sleep until the fence gets signaled or until timeout elapses

    :param struct dma_fence \*fence:
        [in]    the fence to wait on

    :param bool intr:
        [in]    if true, do an interruptible wait

    :param signed long timeout:
        [in]    timeout value in jiffies, or MAX_SCHEDULE_TIMEOUT

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

.. _`dma_fence_enable_sw_signaling`:

dma_fence_enable_sw_signaling
=============================

.. c:function:: void dma_fence_enable_sw_signaling(struct dma_fence *fence)

    enable signaling on fence

    :param struct dma_fence \*fence:
        [in]    the fence to enable

.. _`dma_fence_enable_sw_signaling.description`:

Description
-----------

this will request for sw signaling to be enabled, to make the fence
complete as soon as possible

.. _`dma_fence_add_callback`:

dma_fence_add_callback
======================

.. c:function:: int dma_fence_add_callback(struct dma_fence *fence, struct dma_fence_cb *cb, dma_fence_func_t func)

    add a callback to be called when the fence is signaled

    :param struct dma_fence \*fence:
        [in]    the fence to wait on

    :param struct dma_fence_cb \*cb:
        [in]    the callback to register

    :param dma_fence_func_t func:
        [in]    the function to call

.. _`dma_fence_add_callback.description`:

Description
-----------

cb will be initialized by dma_fence_add_callback, no initialization
by the caller is required. Any number of callbacks can be registered
to a fence, but a callback can only be registered to one fence at a time.

Note that the callback can be called from an atomic context.  If
fence is already signaled, this function will return -ENOENT (and
*not* call the callback)

Add a software callback to the fence. Same restrictions apply to
refcount as it does to dma_fence_wait, however the caller doesn't need to
keep a refcount to fence afterwards: when software access is enabled,
the creator of the fence is required to keep the fence alive until
after it signals with dma_fence_signal. The callback itself can be called
from irq context.

.. _`dma_fence_remove_callback`:

dma_fence_remove_callback
=========================

.. c:function:: bool dma_fence_remove_callback(struct dma_fence *fence, struct dma_fence_cb *cb)

    remove a callback from the signaling list

    :param struct dma_fence \*fence:
        [in]    the fence to wait on

    :param struct dma_fence_cb \*cb:
        [in]    the callback to remove

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

.. _`dma_fence_default_wait`:

dma_fence_default_wait
======================

.. c:function:: signed long dma_fence_default_wait(struct dma_fence *fence, bool intr, signed long timeout)

    default sleep until the fence gets signaled or until timeout elapses

    :param struct dma_fence \*fence:
        [in]    the fence to wait on

    :param bool intr:
        [in]    if true, do an interruptible wait

    :param signed long timeout:
        [in]    timeout value in jiffies, or MAX_SCHEDULE_TIMEOUT

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

    :param struct dma_fence \*\*fences:
        [in]    array of fences to wait on

    :param uint32_t count:
        [in]    number of fences to wait on

    :param bool intr:
        [in]    if true, do an interruptible wait

    :param signed long timeout:
        [in]    timeout value in jiffies, or MAX_SCHEDULE_TIMEOUT

    :param uint32_t \*idx:
        [out]    the first signaled fence index, meaningful only on
        positive return

.. _`dma_fence_wait_any_timeout.description`:

Description
-----------

Returns -EINVAL on custom fence wait implementation, -ERESTARTSYS if
interrupted, 0 if the wait timed out, or the remaining timeout in jiffies
on success.

Synchronous waits for the first fence in the array to be signaled. The
caller needs to hold a reference to all fences in the array, otherwise a
fence might be freed before return, resulting in undefined behavior.

.. _`dma_fence_init`:

dma_fence_init
==============

.. c:function:: void dma_fence_init(struct dma_fence *fence, const struct dma_fence_ops *ops, spinlock_t *lock, u64 context, unsigned seqno)

    Initialize a custom fence.

    :param struct dma_fence \*fence:
        [in]    the fence to initialize

    :param const struct dma_fence_ops \*ops:
        [in]    the dma_fence_ops for operations on this fence

    :param spinlock_t \*lock:
        [in]    the irqsafe spinlock to use for locking this fence

    :param u64 context:
        [in]    the execution context this fence is run on

    :param unsigned seqno:
        [in]    a linear increasing sequence number for this context

.. _`dma_fence_init.description`:

Description
-----------

Initializes an allocated fence, the caller doesn't have to keep its
refcount after committing with this fence, but it will need to hold a
refcount again if dma_fence_ops.enable_signaling gets called. This can
be used for other implementing other types of fence.

context and seqno are used for easy comparison between fences, allowing
to check which fence is later by simply using dma_fence_later.

.. This file was automatic generated / don't edit.

