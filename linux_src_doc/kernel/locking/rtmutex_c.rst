.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/locking/rtmutex.c

.. _`__rt_mutex_slowlock`:

\__rt_mutex_slowlock
====================

.. c:function:: int __sched __rt_mutex_slowlock(struct rt_mutex *lock, int state, struct hrtimer_sleeper *timeout, struct rt_mutex_waiter *waiter)

    Perform the wait-wake-try-to-take loop

    :param lock:
        the rt_mutex to take
    :type lock: struct rt_mutex \*

    :param state:
        the state the task should block in (TASK_INTERRUPTIBLE
        or TASK_UNINTERRUPTIBLE)
    :type state: int

    :param timeout:
        the pre-initialized and started timer, or NULL for none
    :type timeout: struct hrtimer_sleeper \*

    :param waiter:
        the pre-initialized rt_mutex_waiter
    :type waiter: struct rt_mutex_waiter \*

.. _`__rt_mutex_slowlock.description`:

Description
-----------

Must be called with lock->wait_lock held and interrupts disabled

.. _`rt_mutex_lock_nested`:

rt_mutex_lock_nested
====================

.. c:function:: void __sched rt_mutex_lock_nested(struct rt_mutex *lock, unsigned int subclass)

    lock a rt_mutex

    :param lock:
        the rt_mutex to be locked
    :type lock: struct rt_mutex \*

    :param subclass:
        the lockdep subclass
    :type subclass: unsigned int

.. _`rt_mutex_lock`:

rt_mutex_lock
=============

.. c:function:: void __sched rt_mutex_lock(struct rt_mutex *lock)

    lock a rt_mutex

    :param lock:
        the rt_mutex to be locked
    :type lock: struct rt_mutex \*

.. _`rt_mutex_lock_interruptible`:

rt_mutex_lock_interruptible
===========================

.. c:function:: int __sched rt_mutex_lock_interruptible(struct rt_mutex *lock)

    lock a rt_mutex interruptible

    :param lock:
        the rt_mutex to be locked
    :type lock: struct rt_mutex \*

.. _`rt_mutex_lock_interruptible.return`:

Return
------

0           on success
-EINTR       when interrupted by a signal

.. _`rt_mutex_timed_lock`:

rt_mutex_timed_lock
===================

.. c:function:: int rt_mutex_timed_lock(struct rt_mutex *lock, struct hrtimer_sleeper *timeout)

    lock a rt_mutex interruptible the timeout structure is provided by the caller

    :param lock:
        the rt_mutex to be locked
    :type lock: struct rt_mutex \*

    :param timeout:
        timeout structure or NULL (no timeout)
    :type timeout: struct hrtimer_sleeper \*

.. _`rt_mutex_timed_lock.return`:

Return
------

0           on success
-EINTR       when interrupted by a signal
-ETIMEDOUT   when the timeout expired

.. _`rt_mutex_trylock`:

rt_mutex_trylock
================

.. c:function:: int __sched rt_mutex_trylock(struct rt_mutex *lock)

    try to lock a rt_mutex

    :param lock:
        the rt_mutex to be locked
    :type lock: struct rt_mutex \*

.. _`rt_mutex_trylock.description`:

Description
-----------

This function can only be called in thread context. It's safe to
call it from atomic regions, but not from hard interrupt or soft
interrupt context.

Returns 1 on success and 0 on contention

.. _`rt_mutex_unlock`:

rt_mutex_unlock
===============

.. c:function:: void __sched rt_mutex_unlock(struct rt_mutex *lock)

    unlock a rt_mutex

    :param lock:
        the rt_mutex to be unlocked
    :type lock: struct rt_mutex \*

.. _`__rt_mutex_futex_unlock`:

\__rt_mutex_futex_unlock
========================

.. c:function:: bool __sched __rt_mutex_futex_unlock(struct rt_mutex *lock, struct wake_q_head *wake_q)

    path, can be simple and will not need to retry.

    :param lock:
        *undescribed*
    :type lock: struct rt_mutex \*

    :param wake_q:
        *undescribed*
    :type wake_q: struct wake_q_head \*

.. _`rt_mutex_destroy`:

rt_mutex_destroy
================

.. c:function:: void rt_mutex_destroy(struct rt_mutex *lock)

    mark a mutex unusable

    :param lock:
        the mutex to be destroyed
    :type lock: struct rt_mutex \*

.. _`rt_mutex_destroy.description`:

Description
-----------

This function marks the mutex uninitialized, and any subsequent
use of the mutex is forbidden. The mutex must not be locked when
this function is called.

.. _`__rt_mutex_init`:

\__rt_mutex_init
================

.. c:function:: void __rt_mutex_init(struct rt_mutex *lock, const char *name, struct lock_class_key *key)

    initialize the rt lock

    :param lock:
        the rt lock to be initialized
    :type lock: struct rt_mutex \*

    :param name:
        *undescribed*
    :type name: const char \*

    :param key:
        *undescribed*
    :type key: struct lock_class_key \*

.. _`__rt_mutex_init.description`:

Description
-----------

Initialize the rt lock to unlocked state.

Initializing of a locked rt lock is not allowed

.. _`rt_mutex_init_proxy_locked`:

rt_mutex_init_proxy_locked
==========================

.. c:function:: void rt_mutex_init_proxy_locked(struct rt_mutex *lock, struct task_struct *proxy_owner)

    initialize and lock a rt_mutex on behalf of a proxy owner

    :param lock:
        the rt_mutex to be locked
    :type lock: struct rt_mutex \*

    :param proxy_owner:
        the task to set as owner
    :type proxy_owner: struct task_struct \*

.. _`rt_mutex_init_proxy_locked.description`:

Description
-----------

No locking. Caller has to do serializing itself

Special API call for PI-futex support. This initializes the rtmutex and
assigns it to \ ``proxy_owner``\ . Concurrent operations on the rtmutex are not
possible at this point because the pi_state which contains the rtmutex
is not yet visible to other tasks.

.. _`rt_mutex_proxy_unlock`:

rt_mutex_proxy_unlock
=====================

.. c:function:: void rt_mutex_proxy_unlock(struct rt_mutex *lock, struct task_struct *proxy_owner)

    release a lock on behalf of owner

    :param lock:
        the rt_mutex to be locked
    :type lock: struct rt_mutex \*

    :param proxy_owner:
        *undescribed*
    :type proxy_owner: struct task_struct \*

.. _`rt_mutex_proxy_unlock.description`:

Description
-----------

No locking. Caller has to do serializing itself

Special API call for PI-futex support. This merrily cleans up the rtmutex
(debugging) state. Concurrent operations on this rt_mutex are not
possible because it belongs to the pi_state which is about to be freed
and it is not longer visible to other tasks.

.. _`rt_mutex_start_proxy_lock`:

rt_mutex_start_proxy_lock
=========================

.. c:function:: int rt_mutex_start_proxy_lock(struct rt_mutex *lock, struct rt_mutex_waiter *waiter, struct task_struct *task)

    Start lock acquisition for another task

    :param lock:
        the rt_mutex to take
    :type lock: struct rt_mutex \*

    :param waiter:
        the pre-initialized rt_mutex_waiter
    :type waiter: struct rt_mutex_waiter \*

    :param task:
        the task to prepare
    :type task: struct task_struct \*

.. _`rt_mutex_start_proxy_lock.return`:

Return
------

0 - task blocked on lock
1 - acquired the lock for task, caller should wake it up
<0 - error

Special API call for FUTEX_REQUEUE_PI support.

.. _`rt_mutex_next_owner`:

rt_mutex_next_owner
===================

.. c:function:: struct task_struct *rt_mutex_next_owner(struct rt_mutex *lock)

    return the next owner of the lock

    :param lock:
        the rt lock query
    :type lock: struct rt_mutex \*

.. _`rt_mutex_next_owner.description`:

Description
-----------

Returns the next owner of the lock or NULL

Caller has to serialize against other accessors to the lock
itself.

Special API call for PI-futex support

.. _`rt_mutex_wait_proxy_lock`:

rt_mutex_wait_proxy_lock
========================

.. c:function:: int rt_mutex_wait_proxy_lock(struct rt_mutex *lock, struct hrtimer_sleeper *to, struct rt_mutex_waiter *waiter)

    Wait for lock acquisition

    :param lock:
        the rt_mutex we were woken on
    :type lock: struct rt_mutex \*

    :param to:
        the timeout, null if none. hrtimer should already have
        been started.
    :type to: struct hrtimer_sleeper \*

    :param waiter:
        the pre-initialized rt_mutex_waiter
    :type waiter: struct rt_mutex_waiter \*

.. _`rt_mutex_wait_proxy_lock.description`:

Description
-----------

Wait for the the lock acquisition started on our behalf by
\ :c:func:`rt_mutex_start_proxy_lock`\ . Upon failure, the caller must call
\ :c:func:`rt_mutex_cleanup_proxy_lock`\ .

.. _`rt_mutex_wait_proxy_lock.return`:

Return
------

0 - success
<0 - error, one of -EINTR, -ETIMEDOUT

Special API call for PI-futex support

.. _`rt_mutex_cleanup_proxy_lock`:

rt_mutex_cleanup_proxy_lock
===========================

.. c:function:: bool rt_mutex_cleanup_proxy_lock(struct rt_mutex *lock, struct rt_mutex_waiter *waiter)

    Cleanup failed lock acquisition

    :param lock:
        the rt_mutex we were woken on
    :type lock: struct rt_mutex \*

    :param waiter:
        the pre-initialized rt_mutex_waiter
    :type waiter: struct rt_mutex_waiter \*

.. _`rt_mutex_cleanup_proxy_lock.description`:

Description
-----------

Attempt to clean up after a failed \ :c:func:`rt_mutex_wait_proxy_lock`\ .

Unless we acquired the lock; we're still enqueued on the wait-list and can
in fact still be granted ownership until we're removed. Therefore we can
find we are in fact the owner and must disregard the
\ :c:func:`rt_mutex_wait_proxy_lock`\  failure.

.. _`rt_mutex_cleanup_proxy_lock.return`:

Return
------

true  - did the cleanup, we done.
false - we acquired the lock after \ :c:func:`rt_mutex_wait_proxy_lock`\  returned,
caller should disregards its return value.

Special API call for PI-futex support

.. This file was automatic generated / don't edit.

