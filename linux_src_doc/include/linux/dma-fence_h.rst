.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/dma-fence.h

.. _`dma_fence`:

struct dma_fence
================

.. c:type:: struct dma_fence

    software synchronization primitive

.. _`dma_fence.definition`:

Definition
----------

.. code-block:: c

    struct dma_fence {
        struct kref refcount;
        const struct dma_fence_ops *ops;
        struct rcu_head rcu;
        struct list_head cb_list;
        spinlock_t *lock;
        u64 context;
        unsigned seqno;
        unsigned long flags;
        ktime_t timestamp;
        int error;
    }

.. _`dma_fence.members`:

Members
-------

refcount
    refcount for this fence

ops
    dma_fence_ops associated with this fence

rcu
    used for releasing fence with kfree_rcu

cb_list
    list of all callbacks to call

lock
    spin_lock_irqsave used for locking

context
    execution context this fence belongs to, returned by
    \ :c:func:`dma_fence_context_alloc`\ 

seqno
    the sequence number of this fence inside the execution context,
    can be compared to decide which fence would be signaled later.

flags
    A mask of DMA_FENCE_FLAG_* defined below

timestamp
    Timestamp when the fence was signaled.

error
    Optional, only valid if < 0, must be set before calling
    dma_fence_signal, indicates that the fence has completed with an error.

.. _`dma_fence.description`:

Description
-----------

the flags member must be manipulated and read using the appropriate
atomic ops (bit_*), so taking the spinlock will not be needed most
of the time.

DMA_FENCE_FLAG_SIGNALED_BIT - fence is already signaled
DMA_FENCE_FLAG_TIMESTAMP_BIT - timestamp recorded for fence signaling
DMA_FENCE_FLAG_ENABLE_SIGNAL_BIT - enable_signaling might have been called
DMA_FENCE_FLAG_USER_BITS - start of the unused bits, can be used by the
implementer of the fence for its own purposes. Can be used in different
ways by different fence implementers, so do not rely on this.

Since atomic bitops are used, this is not guaranteed to be the case.
Particularly, if the bit was set, but dma_fence_signal was called right
before this bit was set, it would have been able to set the
DMA_FENCE_FLAG_SIGNALED_BIT, before enable_signaling was called.
Adding a check for DMA_FENCE_FLAG_SIGNALED_BIT after setting
DMA_FENCE_FLAG_ENABLE_SIGNAL_BIT closes this race, and makes sure that
after dma_fence_signal was called, any enable_signaling call will have either
been completed, or never called at all.

.. _`dma_fence_cb`:

struct dma_fence_cb
===================

.. c:type:: struct dma_fence_cb

    callback for \ :c:func:`dma_fence_add_callback`\ 

.. _`dma_fence_cb.definition`:

Definition
----------

.. code-block:: c

    struct dma_fence_cb {
        struct list_head node;
        dma_fence_func_t func;
    }

.. _`dma_fence_cb.members`:

Members
-------

node
    used by \ :c:func:`dma_fence_add_callback`\  to append this struct to fence::cb_list

func
    dma_fence_func_t to call

.. _`dma_fence_cb.description`:

Description
-----------

This struct will be initialized by \ :c:func:`dma_fence_add_callback`\ , additional
data can be passed along by embedding dma_fence_cb in another struct.

.. _`dma_fence_ops`:

struct dma_fence_ops
====================

.. c:type:: struct dma_fence_ops

    operations implemented for fence

.. _`dma_fence_ops.definition`:

Definition
----------

.. code-block:: c

    struct dma_fence_ops {
        const char * (*get_driver_name)(struct dma_fence *fence);
        const char * (*get_timeline_name)(struct dma_fence *fence);
        bool (*enable_signaling)(struct dma_fence *fence);
        bool (*signaled)(struct dma_fence *fence);
        signed long (*wait)(struct dma_fence *fence, bool intr, signed long timeout);
        void (*release)(struct dma_fence *fence);
        int (*fill_driver_data)(struct dma_fence *fence, void *data, int size);
        void (*fence_value_str)(struct dma_fence *fence, char *str, int size);
        void (*timeline_value_str)(struct dma_fence *fence, char *str, int size);
    }

.. _`dma_fence_ops.members`:

Members
-------

get_driver_name

    Returns the driver name. This is a callback to allow drivers to
    compute the name at runtime, without having it to store permanently
    for each fence, or build a cache of some sort.

    This callback is mandatory.

get_timeline_name

    Return the name of the context this fence belongs to. This is a
    callback to allow drivers to compute the name at runtime, without
    having it to store permanently for each fence, or build a cache of
    some sort.

    This callback is mandatory.

enable_signaling

    Enable software signaling of fence.

    For fence implementations that have the capability for hw->hw
    signaling, they can implement this op to enable the necessary
    interrupts, or insert commands into cmdstream, etc, to avoid these
    costly operations for the common case where only hw->hw
    synchronization is required.  This is called in the first
    \ :c:func:`dma_fence_wait`\  or \ :c:func:`dma_fence_add_callback`\  path to let the fence
    implementation know that there is another driver waiting on the
    signal (ie. hw->sw case).

    This function can be called from atomic context, but not
    from irq context, so normal spinlocks can be used.

    A return value of false indicates the fence already passed,
    or some failure occurred that made it impossible to enable
    signaling. True indicates successful enabling.

    \ :c:type:`dma_fence.error <dma_fence>`\  may be set in enable_signaling, but only when false
    is returned.

    Since many implementations can call \ :c:func:`dma_fence_signal`\  even when before
    \ ``enable_signaling``\  has been called there's a race window, where the
    \ :c:func:`dma_fence_signal`\  might result in the final fence reference being
    released and its memory freed. To avoid this, implementations of this
    callback should grab their own reference using \ :c:func:`dma_fence_get`\ , to be
    released when the fence is signalled (through e.g. the interrupt
    handler).

    This callback is mandatory.

signaled

    Peek whether the fence is signaled, as a fastpath optimization for
    e.g. \ :c:func:`dma_fence_wait`\  or \ :c:func:`dma_fence_add_callback`\ . Note that this
    callback does not need to make any guarantees beyond that a fence
    once indicates as signalled must always return true from this
    callback. This callback may return false even if the fence has
    completed already, in this case information hasn't propogated throug
    the system yet. See also \ :c:func:`dma_fence_is_signaled`\ .

    May set \ :c:type:`dma_fence.error <dma_fence>`\  if returning true.

    This callback is optional.

wait

    Custom wait implementation, or dma_fence_default_wait.

    Must not be NULL, set to dma_fence_default_wait for default implementation.
    the dma_fence_default_wait implementation should work for any fence, as long
    as enable_signaling works correctly.

    Must return -ERESTARTSYS if the wait is intr = true and the wait was
    interrupted, and remaining jiffies if fence has signaled, or 0 if wait
    timed out. Can also return other error values on custom implementations,
    which should be treated as if the fence is signaled. For example a hardware
    lockup could be reported like that.

    This callback is mandatory.

release

    Called on destruction of fence to release additional resources.
    Can be called from irq context.  This callback is optional. If it is
    NULL, then \ :c:func:`dma_fence_free`\  is instead called as the default
    implementation.

fill_driver_data

    Callback to fill in free-form debug info.

    Returns amount of bytes filled, or negative error on failure.

    This callback is optional.

fence_value_str

    Callback to fill in free-form debug info specific to this fence, like
    the sequence number.

    This callback is optional.

timeline_value_str

    Fills in the current value of the timeline as a string, like the
    sequence number. This should match what \ ``fill_driver_data``\  prints for
    the most recently signalled fence (assuming no delayed signalling).

.. _`dma_fence_put`:

dma_fence_put
=============

.. c:function:: void dma_fence_put(struct dma_fence *fence)

    decreases refcount of the fence

    :param struct dma_fence \*fence:
        fence to reduce refcount of

.. _`dma_fence_get`:

dma_fence_get
=============

.. c:function:: struct dma_fence *dma_fence_get(struct dma_fence *fence)

    increases refcount of the fence

    :param struct dma_fence \*fence:
        fence to increase refcount of

.. _`dma_fence_get.description`:

Description
-----------

Returns the same fence, with refcount increased by 1.

.. _`dma_fence_get_rcu`:

dma_fence_get_rcu
=================

.. c:function:: struct dma_fence *dma_fence_get_rcu(struct dma_fence *fence)

    get a fence from a reservation_object_list with rcu read lock

    :param struct dma_fence \*fence:
        fence to increase refcount of

.. _`dma_fence_get_rcu.description`:

Description
-----------

Function returns NULL if no refcount could be obtained, or the fence.

.. _`dma_fence_get_rcu_safe`:

dma_fence_get_rcu_safe
======================

.. c:function:: struct dma_fence *dma_fence_get_rcu_safe(struct dma_fence __rcu **fencep)

    acquire a reference to an RCU tracked fence

    :param struct dma_fence __rcu \*\*fencep:
        pointer to fence to increase refcount of

.. _`dma_fence_get_rcu_safe.description`:

Description
-----------

Function returns NULL if no refcount could be obtained, or the fence.
This function handles acquiring a reference to a fence that may be
reallocated within the RCU grace period (such as with SLAB_TYPESAFE_BY_RCU),
so long as the caller is using RCU on the pointer to the fence.

An alternative mechanism is to employ a seqlock to protect a bunch of
fences, such as used by struct reservation_object. When using a seqlock,
the seqlock must be taken before and checked after a reference to the
fence is acquired (as shown here).

The caller is required to hold the RCU read lock.

.. _`dma_fence_is_signaled_locked`:

dma_fence_is_signaled_locked
============================

.. c:function:: bool dma_fence_is_signaled_locked(struct dma_fence *fence)

    Return an indication if the fence is signaled yet.

    :param struct dma_fence \*fence:
        the fence to check

.. _`dma_fence_is_signaled_locked.description`:

Description
-----------

Returns true if the fence was already signaled, false if not. Since this
function doesn't enable signaling, it is not guaranteed to ever return
true if \ :c:func:`dma_fence_add_callback`\ , \ :c:func:`dma_fence_wait`\  or
\ :c:func:`dma_fence_enable_sw_signaling`\  haven't been called before.

This function requires \ :c:type:`dma_fence.lock <dma_fence>`\  to be held.

See also \ :c:func:`dma_fence_is_signaled`\ .

.. _`dma_fence_is_signaled`:

dma_fence_is_signaled
=====================

.. c:function:: bool dma_fence_is_signaled(struct dma_fence *fence)

    Return an indication if the fence is signaled yet.

    :param struct dma_fence \*fence:
        the fence to check

.. _`dma_fence_is_signaled.description`:

Description
-----------

Returns true if the fence was already signaled, false if not. Since this
function doesn't enable signaling, it is not guaranteed to ever return
true if \ :c:func:`dma_fence_add_callback`\ , \ :c:func:`dma_fence_wait`\  or
\ :c:func:`dma_fence_enable_sw_signaling`\  haven't been called before.

It's recommended for seqno fences to call dma_fence_signal when the
operation is complete, it makes it possible to prevent issues from
wraparound between time of issue and time of use by checking the return
value of this function before calling hardware-specific wait instructions.

See also \ :c:func:`dma_fence_is_signaled_locked`\ .

.. _`__dma_fence_is_later`:

__dma_fence_is_later
====================

.. c:function:: bool __dma_fence_is_later(u32 f1, u32 f2)

    return if f1 is chronologically later than f2

    :param u32 f1:
        the first fence's seqno

    :param u32 f2:
        the second fence's seqno from the same context

.. _`__dma_fence_is_later.description`:

Description
-----------

Returns true if f1 is chronologically later than f2. Both fences must be
from the same context, since a seqno is not common across contexts.

.. _`dma_fence_is_later`:

dma_fence_is_later
==================

.. c:function:: bool dma_fence_is_later(struct dma_fence *f1, struct dma_fence *f2)

    return if f1 is chronologically later than f2

    :param struct dma_fence \*f1:
        the first fence from the same context

    :param struct dma_fence \*f2:
        the second fence from the same context

.. _`dma_fence_is_later.description`:

Description
-----------

Returns true if f1 is chronologically later than f2. Both fences must be
from the same context, since a seqno is not re-used across contexts.

.. _`dma_fence_later`:

dma_fence_later
===============

.. c:function:: struct dma_fence *dma_fence_later(struct dma_fence *f1, struct dma_fence *f2)

    return the chronologically later fence

    :param struct dma_fence \*f1:
        the first fence from the same context

    :param struct dma_fence \*f2:
        the second fence from the same context

.. _`dma_fence_later.description`:

Description
-----------

Returns NULL if both fences are signaled, otherwise the fence that would be
signaled last. Both fences must be from the same context, since a seqno is
not re-used across contexts.

.. _`dma_fence_get_status_locked`:

dma_fence_get_status_locked
===========================

.. c:function:: int dma_fence_get_status_locked(struct dma_fence *fence)

    returns the status upon completion

    :param struct dma_fence \*fence:
        the dma_fence to query

.. _`dma_fence_get_status_locked.description`:

Description
-----------

Drivers can supply an optional error status condition before they signal
the fence (to indicate whether the fence was completed due to an error
rather than success). The value of the status condition is only valid
if the fence has been signaled, \ :c:func:`dma_fence_get_status_locked`\  first checks
the signal state before reporting the error status.

Returns 0 if the fence has not yet been signaled, 1 if the fence has
been signaled without an error condition, or a negative error code
if the fence has been completed in err.

.. _`dma_fence_set_error`:

dma_fence_set_error
===================

.. c:function:: void dma_fence_set_error(struct dma_fence *fence, int error)

    flag an error condition on the fence

    :param struct dma_fence \*fence:
        the dma_fence

    :param int error:
        the error to store

.. _`dma_fence_set_error.description`:

Description
-----------

Drivers can supply an optional error status condition before they signal
the fence, to indicate that the fence was completed due to an error
rather than success. This must be set before signaling (so that the value
is visible before any waiters on the signal callback are woken). This
helper exists to help catching erroneous setting of #dma_fence.error.

.. _`dma_fence_wait`:

dma_fence_wait
==============

.. c:function:: signed long dma_fence_wait(struct dma_fence *fence, bool intr)

    sleep until the fence gets signaled

    :param struct dma_fence \*fence:
        the fence to wait on

    :param bool intr:
        if true, do an interruptible wait

.. _`dma_fence_wait.description`:

Description
-----------

This function will return -ERESTARTSYS if interrupted by a signal,
or 0 if the fence was signaled. Other error values may be
returned on custom implementations.

Performs a synchronous wait on this fence. It is assumed the caller
directly or indirectly holds a reference to the fence, otherwise the
fence might be freed before return, resulting in undefined behavior.

See also \ :c:func:`dma_fence_wait_timeout`\  and \ :c:func:`dma_fence_wait_any_timeout`\ .

.. This file was automatic generated / don't edit.

