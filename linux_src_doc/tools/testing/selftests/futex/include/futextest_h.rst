.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/testing/selftests/futex/include/futextest.h

.. _`futex`:

futex
=====

.. c:function::  futex( uaddr,  op,  val,  timeout,  uaddr2,  val3,  opflags)

    SYS_futex syscall wrapper

    :param uaddr:
        address of first futex
    :type uaddr: 

    :param op:
        futex op code
    :type op: 

    :param val:
        typically expected value of uaddr, but varies by op
    :type val: 

    :param timeout:
        typically an absolute struct timespec (except where noted
        otherwise). Overloaded by some ops
    :type timeout: 

    :param uaddr2:
        address of second futex for some ops\
    :type uaddr2: 

    :param val3:
        varies by op
    :type val3: 

    :param opflags:
        flags to be bitwise OR'd with op, such as FUTEX_PRIVATE_FLAG
    :type opflags: 

.. _`futex.description`:

Description
-----------

\ :c:func:`futex`\  is used by all the following futex op wrappers. It can also be
used for misuse and abuse testing. Generally, the specific op wrappers
should be used instead. It is a macro instead of an static inline function as
some of the types over overloaded (timeout is used for nr_requeue for
example).

These argument descriptions are the defaults for all
like-named arguments in the following wrappers except where noted below.

.. _`futex_wait`:

futex_wait
==========

.. c:function:: int futex_wait(futex_t *uaddr, futex_t val, struct timespec *timeout, int opflags)

    block on uaddr with optional timeout

    :param uaddr:
        *undescribed*
    :type uaddr: futex_t \*

    :param val:
        *undescribed*
    :type val: futex_t

    :param timeout:
        relative timeout
    :type timeout: struct timespec \*

    :param opflags:
        *undescribed*
    :type opflags: int

.. _`futex_wake`:

futex_wake
==========

.. c:function:: int futex_wake(futex_t *uaddr, int nr_wake, int opflags)

    wake one or more tasks blocked on uaddr

    :param uaddr:
        *undescribed*
    :type uaddr: futex_t \*

    :param nr_wake:
        wake up to this many tasks
    :type nr_wake: int

    :param opflags:
        *undescribed*
    :type opflags: int

.. _`futex_wait_bitset`:

futex_wait_bitset
=================

.. c:function:: int futex_wait_bitset(futex_t *uaddr, futex_t val, struct timespec *timeout, u_int32_t bitset, int opflags)

    block on uaddr with bitset

    :param uaddr:
        *undescribed*
    :type uaddr: futex_t \*

    :param val:
        *undescribed*
    :type val: futex_t

    :param timeout:
        *undescribed*
    :type timeout: struct timespec \*

    :param bitset:
        bitset to be used with futex_wake_bitset
    :type bitset: u_int32_t

    :param opflags:
        *undescribed*
    :type opflags: int

.. _`futex_wake_bitset`:

futex_wake_bitset
=================

.. c:function:: int futex_wake_bitset(futex_t *uaddr, int nr_wake, u_int32_t bitset, int opflags)

    wake one or more tasks blocked on uaddr with bitset

    :param uaddr:
        *undescribed*
    :type uaddr: futex_t \*

    :param nr_wake:
        *undescribed*
    :type nr_wake: int

    :param bitset:
        bitset to compare with that used in futex_wait_bitset
    :type bitset: u_int32_t

    :param opflags:
        *undescribed*
    :type opflags: int

.. _`futex_lock_pi`:

futex_lock_pi
=============

.. c:function:: int futex_lock_pi(futex_t *uaddr, struct timespec *timeout, int detect, int opflags)

    block on uaddr as a PI mutex

    :param uaddr:
        *undescribed*
    :type uaddr: futex_t \*

    :param timeout:
        *undescribed*
    :type timeout: struct timespec \*

    :param detect:
        whether (1) or not (0) to perform deadlock detection
    :type detect: int

    :param opflags:
        *undescribed*
    :type opflags: int

.. _`futex_unlock_pi`:

futex_unlock_pi
===============

.. c:function:: int futex_unlock_pi(futex_t *uaddr, int opflags)

    release uaddr as a PI mutex, waking the top waiter

    :param uaddr:
        *undescribed*
    :type uaddr: futex_t \*

    :param opflags:
        *undescribed*
    :type opflags: int

.. _`futex_wake_op`:

futex_wake_op
=============

.. c:function:: int futex_wake_op(futex_t *uaddr, futex_t *uaddr2, int nr_wake, int nr_wake2, int wake_op, int opflags)

    FIXME: COME UP WITH A GOOD ONE LINE DESCRIPTION

    :param uaddr:
        *undescribed*
    :type uaddr: futex_t \*

    :param uaddr2:
        *undescribed*
    :type uaddr2: futex_t \*

    :param nr_wake:
        *undescribed*
    :type nr_wake: int

    :param nr_wake2:
        *undescribed*
    :type nr_wake2: int

    :param wake_op:
        *undescribed*
    :type wake_op: int

    :param opflags:
        *undescribed*
    :type opflags: int

.. _`futex_requeue`:

futex_requeue
=============

.. c:function:: int futex_requeue(futex_t *uaddr, futex_t *uaddr2, int nr_wake, int nr_requeue, int opflags)

    requeue without expected value comparison, deprecated

    :param uaddr:
        *undescribed*
    :type uaddr: futex_t \*

    :param uaddr2:
        *undescribed*
    :type uaddr2: futex_t \*

    :param nr_wake:
        wake up to this many tasks
    :type nr_wake: int

    :param nr_requeue:
        requeue up to this many tasks
    :type nr_requeue: int

    :param opflags:
        *undescribed*
    :type opflags: int

.. _`futex_requeue.description`:

Description
-----------

Due to its inherently racy implementation, \ :c:func:`futex_requeue`\  is deprecated in
favor of \ :c:func:`futex_cmp_requeue`\ .

.. _`futex_cmp_requeue`:

futex_cmp_requeue
=================

.. c:function:: int futex_cmp_requeue(futex_t *uaddr, futex_t val, futex_t *uaddr2, int nr_wake, int nr_requeue, int opflags)

    requeue tasks from uaddr to uaddr2

    :param uaddr:
        *undescribed*
    :type uaddr: futex_t \*

    :param val:
        *undescribed*
    :type val: futex_t

    :param uaddr2:
        *undescribed*
    :type uaddr2: futex_t \*

    :param nr_wake:
        wake up to this many tasks
    :type nr_wake: int

    :param nr_requeue:
        requeue up to this many tasks
    :type nr_requeue: int

    :param opflags:
        *undescribed*
    :type opflags: int

.. _`futex_wait_requeue_pi`:

futex_wait_requeue_pi
=====================

.. c:function:: int futex_wait_requeue_pi(futex_t *uaddr, futex_t val, futex_t *uaddr2, struct timespec *timeout, int opflags)

    block on uaddr and prepare to requeue to uaddr2

    :param uaddr:
        non-PI futex source
    :type uaddr: futex_t \*

    :param val:
        *undescribed*
    :type val: futex_t

    :param uaddr2:
        PI futex target
    :type uaddr2: futex_t \*

    :param timeout:
        *undescribed*
    :type timeout: struct timespec \*

    :param opflags:
        *undescribed*
    :type opflags: int

.. _`futex_wait_requeue_pi.description`:

Description
-----------

This is the first half of the requeue_pi mechanism. It shall always be
paired with \ :c:func:`futex_cmp_requeue_pi`\ .

.. _`futex_cmp_requeue_pi`:

futex_cmp_requeue_pi
====================

.. c:function:: int futex_cmp_requeue_pi(futex_t *uaddr, futex_t val, futex_t *uaddr2, int nr_wake, int nr_requeue, int opflags)

    requeue tasks from uaddr to uaddr2 (PI aware)

    :param uaddr:
        non-PI futex source
    :type uaddr: futex_t \*

    :param val:
        *undescribed*
    :type val: futex_t

    :param uaddr2:
        PI futex target
    :type uaddr2: futex_t \*

    :param nr_wake:
        wake up to this many tasks
    :type nr_wake: int

    :param nr_requeue:
        requeue up to this many tasks
    :type nr_requeue: int

    :param opflags:
        *undescribed*
    :type opflags: int

.. _`futex_cmpxchg`:

futex_cmpxchg
=============

.. c:function:: u_int32_t futex_cmpxchg(futex_t *uaddr, u_int32_t oldval, u_int32_t newval)

    atomic compare and exchange

    :param uaddr:
        The address of the futex to be modified
    :type uaddr: futex_t \*

    :param oldval:
        The expected value of the futex
    :type oldval: u_int32_t

    :param newval:
        The new value to try and assign the futex
    :type newval: u_int32_t

.. _`futex_cmpxchg.description`:

Description
-----------

Implement cmpxchg using gcc atomic builtins.
http://gcc.gnu.org/onlinedocs/gcc-4.1.0/gcc/Atomic-Builtins.html

Return the old futex value.

.. _`futex_dec`:

futex_dec
=========

.. c:function:: u_int32_t futex_dec(futex_t *uaddr)

    atomic decrement of the futex value

    :param uaddr:
        The address of the futex to be modified
    :type uaddr: futex_t \*

.. _`futex_dec.description`:

Description
-----------

Return the new futex value.

.. _`futex_inc`:

futex_inc
=========

.. c:function:: u_int32_t futex_inc(futex_t *uaddr)

    atomic increment of the futex value

    :param uaddr:
        the address of the futex to be modified
    :type uaddr: futex_t \*

.. _`futex_inc.description`:

Description
-----------

Return the new futex value.

.. _`futex_set`:

futex_set
=========

.. c:function:: u_int32_t futex_set(futex_t *uaddr, u_int32_t newval)

    atomic decrement of the futex value

    :param uaddr:
        the address of the futex to be modified
    :type uaddr: futex_t \*

    :param newval:
        New value for the atomic_t
    :type newval: u_int32_t

.. _`futex_set.description`:

Description
-----------

Return the new futex value.

.. This file was automatic generated / don't edit.

