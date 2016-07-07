.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/locking/rtmutex.c

.. _`__rt_mutex_slowlock`:

__rt_mutex_slowlock
===================

.. c:function:: int __sched __rt_mutex_slowlock(struct rt_mutex *lock, int state, struct hrtimer_sleeper *timeout, struct rt_mutex_waiter *waiter)

    Perform the wait-wake-try-to-take loop

    :param struct rt_mutex \*lock:
        the rt_mutex to take

    :param int state:
        the state the task should block in (TASK_INTERRUPTIBLE
        or TASK_UNINTERRUPTIBLE)

    :param struct hrtimer_sleeper \*timeout:
        the pre-initialized and started timer, or NULL for none

    :param struct rt_mutex_waiter \*waiter:
        the pre-initialized rt_mutex_waiter

.. _`__rt_mutex_slowlock.description`:

Description
-----------

Must be called with lock->wait_lock held and interrupts disabled

.. _`rt_mutex_lock`:

rt_mutex_lock
=============

.. c:function:: void __sched rt_mutex_lock(struct rt_mutex *lock)

    lock a rt_mutex

    :param struct rt_mutex \*lock:
        the rt_mutex to be locked

.. _`rt_mutex_lock_interruptible`:

rt_mutex_lock_interruptible
===========================

.. c:function:: int __sched rt_mutex_lock_interruptible(struct rt_mutex *lock)

    lock a rt_mutex interruptible

    :param struct rt_mutex \*lock:
        the rt_mutex to be locked

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

    :param struct rt_mutex \*lock:
        the rt_mutex to be locked

    :param struct hrtimer_sleeper \*timeout:
        timeout structure or NULL (no timeout)

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

    :param struct rt_mutex \*lock:
        the rt_mutex to be locked

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

    :param struct rt_mutex \*lock:
        the rt_mutex to be unlocked

.. _`rt_mutex_futex_unlock`:

rt_mutex_futex_unlock
=====================

.. c:function:: bool __sched rt_mutex_futex_unlock(struct rt_mutex *lock, struct wake_q_head *wqh)

    Futex variant of rt_mutex_unlock

    :param struct rt_mutex \*lock:
        the rt_mutex to be unlocked

    :param struct wake_q_head \*wqh:
        *undescribed*

.. _`rt_mutex_futex_unlock.return`:

Return
------

true/false indicating whether priority adjustment is
required or not.

.. _`rt_mutex_destroy`:

rt_mutex_destroy
================

.. c:function:: void rt_mutex_destroy(struct rt_mutex *lock)

    mark a mutex unusable

    :param struct rt_mutex \*lock:
        the mutex to be destroyed

.. _`rt_mutex_destroy.description`:

Description
-----------

This function marks the mutex uninitialized, and any subsequent
use of the mutex is forbidden. The mutex must not be locked when
this function is called.

.. _`__rt_mutex_init`:

__rt_mutex_init
===============

.. c:function:: void __rt_mutex_init(struct rt_mutex *lock, const char *name)

    initialize the rt lock

    :param struct rt_mutex \*lock:
        the rt lock to be initialized

    :param const char \*name:
        *undescribed*

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

    :param struct rt_mutex \*lock:
        the rt_mutex to be locked

    :param struct task_struct \*proxy_owner:
        the task to set as owner

.. _`rt_mutex_init_proxy_locked.description`:

Description
-----------

No locking. Caller has to do serializing itself
Special API call for PI-futex support

.. _`rt_mutex_proxy_unlock`:

rt_mutex_proxy_unlock
=====================

.. c:function:: void rt_mutex_proxy_unlock(struct rt_mutex *lock, struct task_struct *proxy_owner)

    release a lock on behalf of owner

    :param struct rt_mutex \*lock:
        the rt_mutex to be locked

    :param struct task_struct \*proxy_owner:
        *undescribed*

.. _`rt_mutex_proxy_unlock.description`:

Description
-----------

No locking. Caller has to do serializing itself
Special API call for PI-futex support

.. _`rt_mutex_start_proxy_lock`:

rt_mutex_start_proxy_lock
=========================

.. c:function:: int rt_mutex_start_proxy_lock(struct rt_mutex *lock, struct rt_mutex_waiter *waiter, struct task_struct *task)

    Start lock acquisition for another task

    :param struct rt_mutex \*lock:
        the rt_mutex to take

    :param struct rt_mutex_waiter \*waiter:
        the pre-initialized rt_mutex_waiter

    :param struct task_struct \*task:
        the task to prepare

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

    :param struct rt_mutex \*lock:
        the rt lock query

.. _`rt_mutex_next_owner.description`:

Description
-----------

Returns the next owner of the lock or NULL

Caller has to serialize against other accessors to the lock
itself.

Special API call for PI-futex support

.. _`rt_mutex_finish_proxy_lock`:

rt_mutex_finish_proxy_lock
==========================

.. c:function:: int rt_mutex_finish_proxy_lock(struct rt_mutex *lock, struct hrtimer_sleeper *to, struct rt_mutex_waiter *waiter)

    Complete lock acquisition

    :param struct rt_mutex \*lock:
        the rt_mutex we were woken on

    :param struct hrtimer_sleeper \*to:
        the timeout, null if none. hrtimer should already have
        been started.

    :param struct rt_mutex_waiter \*waiter:
        the pre-initialized rt_mutex_waiter

.. _`rt_mutex_finish_proxy_lock.description`:

Description
-----------

Complete the lock acquisition started our behalf by another thread.

.. _`rt_mutex_finish_proxy_lock.return`:

Return
------

0 - success
<0 - error, one of -EINTR, -ETIMEDOUT

Special API call for PI-futex requeue support

.. This file was automatic generated / don't edit.

