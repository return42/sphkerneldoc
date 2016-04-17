.. -*- coding: utf-8; mode: rst -*-

=======
fence.h
=======


.. _`fence`:

struct fence
============

.. c:type:: fence

    software synchronization primitive


.. _`fence.definition`:

Definition
----------

.. code-block:: c

  struct fence {
    struct kref refcount;
    const struct fence_ops * ops;
    struct rcu_head rcu;
    struct list_head cb_list;
    spinlock_t * lock;
    unsigned context;
    unsigned seqno;
    unsigned long flags;
    ktime_t timestamp;
    int status;
  };


.. _`fence.members`:

Members
-------

:``refcount``:
    refcount for this fence

:``ops``:
    fence_ops associated with this fence

:``rcu``:
    used for releasing fence with kfree_rcu

:``cb_list``:
    list of all callbacks to call

:``lock``:
    spin_lock_irqsave used for locking

:``context``:
    execution context this fence belongs to, returned by
    :c:func:`fence_context_alloc`

:``seqno``:
    the sequence number of this fence inside the execution context,
    can be compared to decide which fence would be signaled later.

:``flags``:
    A mask of FENCE_FLAG\_\* defined below

:``timestamp``:
    Timestamp when the fence was signaled.

:``status``:
    Optional, only valid if < 0, must be set before calling
    fence_signal, indicates that the fence has completed with an error.




.. _`fence.description`:

Description
-----------

the flags member must be manipulated and read using the appropriate
atomic ops (bit\_\*), so taking the spinlock will not be needed most
of the time.

FENCE_FLAG_SIGNALED_BIT - fence is already signaled
FENCE_FLAG_ENABLE_SIGNAL_BIT - enable_signaling might have been called*
FENCE_FLAG_USER_BITS - start of the unused bits, can be used by the
implementer of the fence for its own purposes. Can be used in different
ways by different fence implementers, so do not rely on this.

*) Since atomic bitops are used, this is not guaranteed to be the case.
Particularly, if the bit was set, but fence_signal was called right
before this bit was set, it would have been able to set the
FENCE_FLAG_SIGNALED_BIT, before enable_signaling was called.
Adding a check for FENCE_FLAG_SIGNALED_BIT after setting
FENCE_FLAG_ENABLE_SIGNAL_BIT closes this race, and makes sure that
after fence_signal was called, any enable_signaling call will have either
been completed, or never called at all.



.. _`fence_cb`:

struct fence_cb
===============

.. c:type:: fence_cb

    callback for fence_add_callback


.. _`fence_cb.definition`:

Definition
----------

.. code-block:: c

  struct fence_cb {
    struct list_head node;
    fence_func_t func;
  };


.. _`fence_cb.members`:

Members
-------

:``node``:
    used by fence_add_callback to append this struct to fence::cb_list

:``func``:
    fence_func_t to call




.. _`fence_cb.description`:

Description
-----------

This struct will be initialized by fence_add_callback, additional
data can be passed along by embedding fence_cb in another struct.



.. _`fence_ops`:

struct fence_ops
================

.. c:type:: fence_ops

    operations implemented for fence


.. _`fence_ops.definition`:

Definition
----------

.. code-block:: c

  struct fence_ops {
    const char * (* get_driver_name) (struct fence *fence);
    const char * (* get_timeline_name) (struct fence *fence);
    bool (* enable_signaling) (struct fence *fence);
    bool (* signaled) (struct fence *fence);
    signed long (* wait) (struct fence *fence, bool intr, signed long timeout);
    void (* release) (struct fence *fence);
    int (* fill_driver_data) (struct fence *fence, void *data, int size);
    void (* fence_value_str) (struct fence *fence, char *str, int size);
    void (* timeline_value_str) (struct fence *fence, char *str, int size);
  };


.. _`fence_ops.members`:

Members
-------

:``get_driver_name``:
    returns the driver name.

:``get_timeline_name``:
    return the name of the context this fence belongs to.

:``enable_signaling``:
    enable software signaling of fence.

:``signaled``:
    [optional] peek whether the fence is signaled, can be null.

:``wait``:
    custom wait implementation, or fence_default_wait.

:``release``:
    [optional] called on destruction of fence, can be null

:``fill_driver_data``:
    [optional] callback to fill in free-form debug info
    Returns amount of bytes filled, or -errno.

:``fence_value_str``:
    [optional] fills in the value of the fence as a string

:``timeline_value_str``:
    [optional] fills in the current value of the timeline
    as a string




.. _`fence_ops.notes-on-enable_signaling`:

Notes on enable_signaling
-------------------------

For fence implementations that have the capability for hw->hw
signaling, they can implement this op to enable the necessary
irqs, or insert commands into cmdstream, etc.  This is called
in the first :c:func:`wait` or :c:func:`add_callback` path to let the fence
implementation know that there is another driver waiting on
the signal (ie. hw->sw case).

This function can be called called from atomic context, but not
from irq context, so normal spinlocks can be used.

A return value of false indicates the fence already passed,
or some failure occurred that made it impossible to enable
signaling. True indicates successful enabling.

fence->status may be set in enable_signaling, but only when false is
returned.

Calling fence_signal before enable_signaling is called allows
for a tiny race window in which enable_signaling is called during,
before, or after fence_signal. To fight this, it is recommended
that before enable_signaling returns true an extra reference is
taken on the fence, to be released when the fence is signaled.
This will mean fence_signal will still be called twice, but
the second time will be a noop since it was already signaled.



.. _`fence_ops.notes-on-signaled`:

Notes on signaled
-----------------

May set fence->status if returning true.



.. _`fence_ops.notes-on-wait`:

Notes on wait
-------------

Must not be NULL, set to fence_default_wait for default implementation.
the fence_default_wait implementation should work for any fence, as long
as enable_signaling works correctly.

Must return -ERESTARTSYS if the wait is intr = true and the wait was
interrupted, and remaining jiffies if fence has signaled, or 0 if wait
timed out. Can also return other error values on custom implementations,
which should be treated as if the fence is signaled. For example a hardware
lockup could be reported like that.



.. _`fence_ops.notes-on-release`:

Notes on release
----------------

Can be NULL, this function allows additional commands to run on
destruction of the fence. Can be called from irq context.
If pointer is set to NULL, kfree will get called instead.



.. _`fence_get`:

fence_get
=========

.. c:function:: struct fence *fence_get (struct fence *fence)

    increases refcount of the fence

    :param struct fence \*fence:
        [in]        fence to increase refcount of



.. _`fence_get.description`:

Description
-----------

Returns the same fence, with refcount increased by 1.



.. _`fence_get_rcu`:

fence_get_rcu
=============

.. c:function:: struct fence *fence_get_rcu (struct fence *fence)

    get a fence from a reservation_object_list with rcu read lock

    :param struct fence \*fence:
        [in]        fence to increase refcount of



.. _`fence_get_rcu.description`:

Description
-----------

Function returns NULL if no refcount could be obtained, or the fence.



.. _`fence_put`:

fence_put
=========

.. c:function:: void fence_put (struct fence *fence)

    decreases refcount of the fence

    :param struct fence \*fence:
        [in]        fence to reduce refcount of



.. _`fence_is_signaled_locked`:

fence_is_signaled_locked
========================

.. c:function:: bool fence_is_signaled_locked (struct fence *fence)

    Return an indication if the fence is signaled yet.

    :param struct fence \*fence:
        [in]        the fence to check



.. _`fence_is_signaled_locked.description`:

Description
-----------

Returns true if the fence was already signaled, false if not. Since this
function doesn't enable signaling, it is not guaranteed to ever return
true if fence_add_callback, fence_wait or fence_enable_sw_signaling
haven't been called before.

This function requires fence->lock to be held.



.. _`fence_is_signaled`:

fence_is_signaled
=================

.. c:function:: bool fence_is_signaled (struct fence *fence)

    Return an indication if the fence is signaled yet.

    :param struct fence \*fence:
        [in]        the fence to check



.. _`fence_is_signaled.description`:

Description
-----------

Returns true if the fence was already signaled, false if not. Since this
function doesn't enable signaling, it is not guaranteed to ever return
true if fence_add_callback, fence_wait or fence_enable_sw_signaling
haven't been called before.

It's recommended for seqno fences to call fence_signal when the
operation is complete, it makes it possible to prevent issues from
wraparound between time of issue and time of use by checking the return
value of this function before calling hardware-specific wait instructions.



.. _`fence_is_later`:

fence_is_later
==============

.. c:function:: bool fence_is_later (struct fence *f1, struct fence *f2)

    return if f1 is chronologically later than f2

    :param struct fence \*f1:
        [in]        the first fence from the same context

    :param struct fence \*f2:
        [in]        the second fence from the same context



.. _`fence_is_later.description`:

Description
-----------

Returns true if f1 is chronologically later than f2. Both fences must be
from the same context, since a seqno is not re-used across contexts.



.. _`fence_later`:

fence_later
===========

.. c:function:: struct fence *fence_later (struct fence *f1, struct fence *f2)

    return the chronologically later fence

    :param struct fence \*f1:
        [in]        the first fence from the same context

    :param struct fence \*f2:
        [in]        the second fence from the same context



.. _`fence_later.description`:

Description
-----------

Returns NULL if both fences are signaled, otherwise the fence that would be
signaled last. Both fences must be from the same context, since a seqno is
not re-used across contexts.



.. _`fence_wait`:

fence_wait
==========

.. c:function:: signed long fence_wait (struct fence *fence, bool intr)

    sleep until the fence gets signaled

    :param struct fence \*fence:
        [in]        the fence to wait on

    :param bool intr:
        [in]        if true, do an interruptible wait



.. _`fence_wait.description`:

Description
-----------

This function will return -ERESTARTSYS if interrupted by a signal,
or 0 if the fence was signaled. Other error values may be
returned on custom implementations.

Performs a synchronous wait on this fence. It is assumed the caller
directly or indirectly holds a reference to the fence, otherwise the
fence might be freed before return, resulting in undefined behavior.

