.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/mutex_32.h

.. _`__mutex_fastpath_lock`:

__mutex_fastpath_lock
=====================

.. c:function::  __mutex_fastpath_lock( count,  fail_fn)

    try to take the lock by moving the count from 1 to a 0 value

    :param  count:
        pointer of type atomic_t

    :param  fail_fn:
        *undescribed*

.. _`__mutex_fastpath_lock.description`:

Description
-----------

Change the count from 1 to a value lower than 1, and call <fn> if it
wasn't 1 originally. This function MUST leave the value lower than 1
even when the "1" assertion wasn't true.

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

.. c:function::  __mutex_fastpath_unlock( count,  fail_fn)

    try to promote the mutex from 0 to 1

    :param  count:
        pointer of type atomic_t

    :param  fail_fn:
        function to call if the original value was not 0

.. _`__mutex_fastpath_unlock.description`:

Description
-----------

try to promote the mutex from 0 to 1. if it wasn't 0, call <fail_fn>.
In the failure case, this function is allowed to either set the value
to 1, or to set it to a value lower than 1.

If the implementation sets it to a value of lower than 1, the
\\ :c:func:`__mutex_slowpath_needs_to_unlock`\  macro needs to return 1, it needs
to return 0 otherwise.

.. _`__mutex_fastpath_trylock`:

__mutex_fastpath_trylock
========================

.. c:function:: int __mutex_fastpath_trylock(atomic_t *count, int (*fail_fn)(atomic_t *))

    try to acquire the mutex, without waiting

    :param atomic_t \*count:
        pointer of type atomic_t

    :param int (\*fail_fn)(atomic_t \*):
        fallback function

.. _`__mutex_fastpath_trylock.description`:

Description
-----------

Change the count from 1 to a value lower than 1, and return 0 (failure)
if it wasn't 1 originally, or return 1 (success) otherwise. This function
MUST leave the value lower than 1 even when the "1" assertion wasn't true.
Additionally, if the value was < 0 originally, this function must not leave
it to 0 on failure.

.. This file was automatic generated / don't edit.

