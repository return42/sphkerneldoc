.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/locking/mutex.c

.. _`mutex_lock`:

mutex_lock
==========

.. c:function:: void __sched mutex_lock(struct mutex *lock)

    acquire the mutex

    :param struct mutex \*lock:
        the mutex to be acquired

.. _`mutex_lock.description`:

Description
-----------

Lock the mutex exclusively for this task. If the mutex is not
available right now, it will sleep until it can get it.

The mutex must later on be released by the same task that
acquired it. Recursive locking is not allowed. The task
may not exit without first unlocking the mutex. Also, kernel
memory where the mutex resides must not be freed with
the mutex still locked. The mutex must first be initialized
(or statically defined) before it can be locked. \ :c:func:`memset`\ -ing
the mutex to 0 is not allowed.

(The CONFIG_DEBUG_MUTEXES .config option turns on debugging
checks that will enforce the restrictions and will also do
deadlock debugging)

This function is similar to (but not equivalent to) \ :c:func:`down`\ .

.. _`mutex_unlock`:

mutex_unlock
============

.. c:function:: void __sched mutex_unlock(struct mutex *lock)

    release the mutex

    :param struct mutex \*lock:
        the mutex to be released

.. _`mutex_unlock.description`:

Description
-----------

Unlock a mutex that has been locked by this task previously.

This function must not be used in interrupt context. Unlocking
of a not locked mutex is not allowed.

This function is similar to (but not equivalent to) \ :c:func:`up`\ .

.. _`ww_mutex_unlock`:

ww_mutex_unlock
===============

.. c:function:: void __sched ww_mutex_unlock(struct ww_mutex *lock)

    release the w/w mutex

    :param struct ww_mutex \*lock:
        the mutex to be released

.. _`ww_mutex_unlock.description`:

Description
-----------

Unlock a mutex that has been locked by this task previously with any of the
ww_mutex_lock* functions (with or without an acquire context). It is
forbidden to release the locks after releasing the acquire context.

This function must not be used in interrupt context. Unlocking
of a unlocked mutex is not allowed.

.. _`mutex_lock_interruptible`:

mutex_lock_interruptible
========================

.. c:function:: int __sched mutex_lock_interruptible(struct mutex *lock)

    Acquire the mutex, interruptible by signals.

    :param struct mutex \*lock:
        The mutex to be acquired.

.. _`mutex_lock_interruptible.description`:

Description
-----------

Lock the mutex like \ :c:func:`mutex_lock`\ .  If a signal is delivered while the
process is sleeping, this function will return without acquiring the
mutex.

.. _`mutex_lock_interruptible.context`:

Context
-------

Process context.

.. _`mutex_lock_interruptible.return`:

Return
------

0 if the lock was successfully acquired or \ ``-EINTR``\  if a
signal arrived.

.. _`mutex_lock_killable`:

mutex_lock_killable
===================

.. c:function:: int __sched mutex_lock_killable(struct mutex *lock)

    Acquire the mutex, interruptible by fatal signals.

    :param struct mutex \*lock:
        The mutex to be acquired.

.. _`mutex_lock_killable.description`:

Description
-----------

Lock the mutex like \ :c:func:`mutex_lock`\ .  If a signal which will be fatal to
the current process is delivered while the process is sleeping, this
function will return without acquiring the mutex.

.. _`mutex_lock_killable.context`:

Context
-------

Process context.

.. _`mutex_lock_killable.return`:

Return
------

0 if the lock was successfully acquired or \ ``-EINTR``\  if a
fatal signal arrived.

.. _`mutex_lock_io`:

mutex_lock_io
=============

.. c:function:: void __sched mutex_lock_io(struct mutex *lock)

    Acquire the mutex and mark the process as waiting for I/O

    :param struct mutex \*lock:
        The mutex to be acquired.

.. _`mutex_lock_io.description`:

Description
-----------

Lock the mutex like \ :c:func:`mutex_lock`\ .  While the task is waiting for this
mutex, it will be accounted as being in the IO wait state by the
scheduler.

.. _`mutex_lock_io.context`:

Context
-------

Process context.

.. _`mutex_trylock`:

mutex_trylock
=============

.. c:function:: int __sched mutex_trylock(struct mutex *lock)

    try to acquire the mutex, without waiting

    :param struct mutex \*lock:
        the mutex to be acquired

.. _`mutex_trylock.description`:

Description
-----------

Try to acquire the mutex atomically. Returns 1 if the mutex
has been acquired successfully, and 0 on contention.

.. _`mutex_trylock.note`:

NOTE
----

this function follows the \ :c:func:`spin_trylock`\  convention, so
it is negated from the \ :c:func:`down_trylock`\  return values! Be careful
about this when converting semaphore users to mutexes.

This function must not be used in interrupt context. The
mutex must be released by the same task that acquired it.

.. _`atomic_dec_and_mutex_lock`:

atomic_dec_and_mutex_lock
=========================

.. c:function:: int atomic_dec_and_mutex_lock(atomic_t *cnt, struct mutex *lock)

    return holding mutex if we dec to 0

    :param atomic_t \*cnt:
        the atomic which we are to dec

    :param struct mutex \*lock:
        the mutex to return holding if we dec to 0

.. _`atomic_dec_and_mutex_lock.description`:

Description
-----------

return true and hold lock if we dec to 0, return false otherwise

.. This file was automatic generated / don't edit.

