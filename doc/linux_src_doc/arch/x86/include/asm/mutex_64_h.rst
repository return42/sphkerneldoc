.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/mutex_64.h

.. _`__mutex_fastpath_lock`:

__mutex_fastpath_lock
=====================

.. c:function:: void __mutex_fastpath_lock(atomic_t *v, void (*) fail_fn (atomic_t *)

    decrement and call function if negative

    :param atomic_t \*v:
        pointer of type atomic_t

    :param (void (\*) fail_fn (atomic_t \*):
        function to call if the result is negative

.. _`__mutex_fastpath_lock.description`:

Description
-----------

Atomically decrements \ ``v``\  and calls <fail_fn> if the result is negative.

.. _`__mutex_fastpath_lock_retval`:

__mutex_fastpath_lock_retval
============================

.. c:function:: int __mutex_fastpath_lock_retval(atomic_t *count)

    try to take the lock by moving the count from 1 to a 0 value

    :param atomic_t \*count:
        pointer of type atomic_t

.. _`__mutex_fastpath_lock_retval.description`:

Description
-----------

Change the count from 1 to a value lower than 1. This function returns 0
if the fastpath succeeds, or -1 otherwise.

.. _`__mutex_fastpath_unlock`:

__mutex_fastpath_unlock
=======================

.. c:function:: void __mutex_fastpath_unlock(atomic_t *v, void (*) fail_fn (atomic_t *)

    increment and call function if nonpositive

    :param atomic_t \*v:
        pointer of type atomic_t

    :param (void (\*) fail_fn (atomic_t \*):
        function to call if the result is nonpositive

.. _`__mutex_fastpath_unlock.description`:

Description
-----------

Atomically increments \ ``v``\  and calls <fail_fn> if the result is nonpositive.

.. _`__mutex_fastpath_trylock`:

__mutex_fastpath_trylock
========================

.. c:function:: int __mutex_fastpath_trylock(atomic_t *count, int (*) fail_fn (atomic_t *)

    try to acquire the mutex, without waiting

    :param atomic_t \*count:
        pointer of type atomic_t

    :param (int (\*) fail_fn (atomic_t \*):
        fallback function

.. _`__mutex_fastpath_trylock.description`:

Description
-----------

Change the count from 1 to 0 and return 1 (success), or return 0 (failure)
if it wasn't 1 originally. [the fallback function is never used on
x86_64, because all x86_64 CPUs have a CMPXCHG instruction.]

.. This file was automatic generated / don't edit.

