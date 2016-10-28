.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ww_mutex.h

.. _`ww_mutex_init`:

ww_mutex_init
=============

.. c:function:: void ww_mutex_init(struct ww_mutex *lock, struct ww_class *ww_class)

    initialize the w/w mutex

    :param struct ww_mutex \*lock:
        the mutex to be initialized

    :param struct ww_class \*ww_class:
        the w/w class the mutex should belong to

.. _`ww_mutex_init.description`:

Description
-----------

Initialize the w/w mutex to unlocked state and associate it with the given
class.

It is not allowed to initialize an already locked mutex.

.. _`ww_acquire_init`:

ww_acquire_init
===============

.. c:function:: void ww_acquire_init(struct ww_acquire_ctx *ctx, struct ww_class *ww_class)

    initialize a w/w acquire context

    :param struct ww_acquire_ctx \*ctx:
        w/w acquire context to initialize

    :param struct ww_class \*ww_class:
        w/w class of the context

.. _`ww_acquire_init.description`:

Description
-----------

Initializes an context to acquire multiple mutexes of the given w/w class.

Context-based w/w mutex acquiring can be done in any order whatsoever within
a given lock class. Deadlocks will be detected and handled with the
wait/wound logic.

Mixing of context-based w/w mutex acquiring and single w/w mutex locking can
result in undetected deadlocks and is so forbidden. Mixing different contexts
for the same w/w class when acquiring mutexes can also result in undetected
deadlocks, and is hence also forbidden. Both types of abuse will be caught by
enabling CONFIG_PROVE_LOCKING.

Nesting of acquire contexts for \_different\_ w/w classes is possible, subject
to the usual locking rules between different lock classes.

An acquire context must be released with ww_acquire_fini by the same task
before the memory is freed. It is recommended to allocate the context itself
on the stack.

.. _`ww_acquire_done`:

ww_acquire_done
===============

.. c:function:: void ww_acquire_done(struct ww_acquire_ctx *ctx)

    marks the end of the acquire phase

    :param struct ww_acquire_ctx \*ctx:
        the acquire context

.. _`ww_acquire_done.description`:

Description
-----------

Marks the end of the acquire phase, any further w/w mutex lock calls using
this context are forbidden.

Calling this function is optional, it is just useful to document w/w mutex
code and clearly designated the acquire phase from actually using the locked
data structures.

.. _`ww_acquire_fini`:

ww_acquire_fini
===============

.. c:function:: void ww_acquire_fini(struct ww_acquire_ctx *ctx)

    releases a w/w acquire context

    :param struct ww_acquire_ctx \*ctx:
        the acquire context to free

.. _`ww_acquire_fini.description`:

Description
-----------

Releases a w/w acquire context. This must be called \_after\_ all acquired w/w
mutexes have been released with ww_mutex_unlock.

.. _`ww_mutex_lock`:

ww_mutex_lock
=============

.. c:function:: int ww_mutex_lock(struct ww_mutex *lock, struct ww_acquire_ctx *ctx)

    acquire the w/w mutex

    :param struct ww_mutex \*lock:
        the mutex to be acquired

    :param struct ww_acquire_ctx \*ctx:
        w/w acquire context, or NULL to acquire only a single lock.

.. _`ww_mutex_lock.description`:

Description
-----------

Lock the w/w mutex exclusively for this task.

Deadlocks within a given w/w class of locks are detected and handled with the
wait/wound algorithm. If the lock isn't immediately avaiable this function
will either sleep until it is (wait case). Or it selects the current context
for backing off by returning -EDEADLK (wound case). Trying to acquire the
same lock with the same context twice is also detected and signalled by
returning -EALREADY. Returns 0 if the mutex was successfully acquired.

In the wound case the caller must release all currently held w/w mutexes for
the given context and then wait for this contending lock to be available by
calling ww_mutex_lock_slow. Alternatively callers can opt to not acquire this
lock and proceed with trying to acquire further w/w mutexes (e.g. when
scanning through lru lists trying to free resources).

The mutex must later on be released by the same task that
acquired it. The task may not exit without first unlocking the mutex. Also,
kernel memory where the mutex resides must not be freed with the mutex still
locked. The mutex must first be initialized (or statically defined) before it
can be locked. \ :c:func:`memset`\ -ing the mutex to 0 is not allowed. The mutex must be
of the same w/w lock class as was used to initialize the acquire context.

A mutex acquired with this function must be released with ww_mutex_unlock.

.. _`ww_mutex_lock_interruptible`:

ww_mutex_lock_interruptible
===========================

.. c:function:: int ww_mutex_lock_interruptible(struct ww_mutex *lock, struct ww_acquire_ctx *ctx)

    acquire the w/w mutex, interruptible

    :param struct ww_mutex \*lock:
        the mutex to be acquired

    :param struct ww_acquire_ctx \*ctx:
        w/w acquire context

.. _`ww_mutex_lock_interruptible.description`:

Description
-----------

Lock the w/w mutex exclusively for this task.

Deadlocks within a given w/w class of locks are detected and handled with the
wait/wound algorithm. If the lock isn't immediately avaiable this function
will either sleep until it is (wait case). Or it selects the current context
for backing off by returning -EDEADLK (wound case). Trying to acquire the
same lock with the same context twice is also detected and signalled by
returning -EALREADY. Returns 0 if the mutex was successfully acquired. If a
signal arrives while waiting for the lock then this function returns -EINTR.

In the wound case the caller must release all currently held w/w mutexes for
the given context and then wait for this contending lock to be available by
calling ww_mutex_lock_slow_interruptible. Alternatively callers can opt to
not acquire this lock and proceed with trying to acquire further w/w mutexes
(e.g. when scanning through lru lists trying to free resources).

The mutex must later on be released by the same task that
acquired it. The task may not exit without first unlocking the mutex. Also,
kernel memory where the mutex resides must not be freed with the mutex still
locked. The mutex must first be initialized (or statically defined) before it
can be locked. \ :c:func:`memset`\ -ing the mutex to 0 is not allowed. The mutex must be
of the same w/w lock class as was used to initialize the acquire context.

A mutex acquired with this function must be released with ww_mutex_unlock.

.. _`ww_mutex_lock_slow`:

ww_mutex_lock_slow
==================

.. c:function:: void ww_mutex_lock_slow(struct ww_mutex *lock, struct ww_acquire_ctx *ctx)

    slowpath acquiring of the w/w mutex

    :param struct ww_mutex \*lock:
        the mutex to be acquired

    :param struct ww_acquire_ctx \*ctx:
        w/w acquire context

.. _`ww_mutex_lock_slow.description`:

Description
-----------

Acquires a w/w mutex with the given context after a wound case. This function
will sleep until the lock becomes available.

The caller must have released all w/w mutexes already acquired with the
context and then call this function on the contended lock.

Afterwards the caller may continue to (re)acquire the other w/w mutexes it
needs with ww_mutex_lock. Note that the -EALREADY return code from
ww_mutex_lock can be used to avoid locking this contended mutex twice.

It is forbidden to call this function with any other w/w mutexes associated
with the context held. It is forbidden to call this on anything else than the
contending mutex.

Note that the slowpath lock acquiring can also be done by calling
ww_mutex_lock directly. This function here is simply to help w/w mutex
locking code readability by clearly denoting the slowpath.

.. _`ww_mutex_lock_slow_interruptible`:

ww_mutex_lock_slow_interruptible
================================

.. c:function:: int ww_mutex_lock_slow_interruptible(struct ww_mutex *lock, struct ww_acquire_ctx *ctx)

    slowpath acquiring of the w/w mutex, interruptible

    :param struct ww_mutex \*lock:
        the mutex to be acquired

    :param struct ww_acquire_ctx \*ctx:
        w/w acquire context

.. _`ww_mutex_lock_slow_interruptible.description`:

Description
-----------

Acquires a w/w mutex with the given context after a wound case. This function
will sleep until the lock becomes available and returns 0 when the lock has
been acquired. If a signal arrives while waiting for the lock then this
function returns -EINTR.

The caller must have released all w/w mutexes already acquired with the
context and then call this function on the contended lock.

Afterwards the caller may continue to (re)acquire the other w/w mutexes it
needs with ww_mutex_lock. Note that the -EALREADY return code from
ww_mutex_lock can be used to avoid locking this contended mutex twice.

It is forbidden to call this function with any other w/w mutexes associated
with the given context held. It is forbidden to call this on anything else
than the contending mutex.

Note that the slowpath lock acquiring can also be done by calling
ww_mutex_lock_interruptible directly. This function here is simply to help
w/w mutex locking code readability by clearly denoting the slowpath.

.. _`ww_mutex_trylock`:

ww_mutex_trylock
================

.. c:function:: int ww_mutex_trylock(struct ww_mutex *lock)

    tries to acquire the w/w mutex without acquire context

    :param struct ww_mutex \*lock:
        mutex to lock

.. _`ww_mutex_trylock.description`:

Description
-----------

Trylocks a mutex without acquire context, so no deadlock detection is
possible. Returns 1 if the mutex has been acquired successfully, 0 otherwise.

.. _`ww_mutex_is_locked`:

ww_mutex_is_locked
==================

.. c:function:: bool ww_mutex_is_locked(struct ww_mutex *lock)

    is the w/w mutex locked

    :param struct ww_mutex \*lock:
        the mutex to be queried

.. _`ww_mutex_is_locked.description`:

Description
-----------

Returns 1 if the mutex is locked, 0 if unlocked.

.. This file was automatic generated / don't edit.

