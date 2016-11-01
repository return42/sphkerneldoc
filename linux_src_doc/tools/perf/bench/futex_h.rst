.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/bench/futex.h

.. _`futex`:

futex
=====

.. c:function::  futex( uaddr,  op,  val,  timeout,  uaddr2,  val3,  opflags)

    SYS_futex syscall wrapper

    :param  uaddr:
        address of first futex

    :param  op:
        futex op code

    :param  val:
        typically expected value of uaddr, but varies by op

    :param  timeout:
        typically an absolute struct timespec (except where noted
        otherwise). Overloaded by some ops

    :param  uaddr2:
        address of second futex for some ops\

    :param  val3:
        varies by op

    :param  opflags:
        flags to be bitwise OR'd with op, such as FUTEX_PRIVATE_FLAG

.. _`futex.description`:

Description
-----------

futex() is used by all the following futex op wrappers. It can also be
used for misuse and abuse testing. Generally, the specific op wrappers
should be used instead. It is a macro instead of an static inline function as
some of the types over overloaded (timeout is used for nr_requeue for
example).

These argument descriptions are the defaults for all
like-named arguments in the following wrappers except where noted below.

.. _`futex_wait`:

futex_wait
==========

.. c:function:: int futex_wait(u_int32_t *uaddr, u_int32_t val, struct timespec *timeout, int opflags)

    block on uaddr with optional timeout

    :param u_int32_t \*uaddr:
        *undescribed*

    :param u_int32_t val:
        *undescribed*

    :param struct timespec \*timeout:
        relative timeout

    :param int opflags:
        *undescribed*

.. _`futex_wake`:

futex_wake
==========

.. c:function:: int futex_wake(u_int32_t *uaddr, int nr_wake, int opflags)

    wake one or more tasks blocked on uaddr

    :param u_int32_t \*uaddr:
        *undescribed*

    :param int nr_wake:
        wake up to this many tasks

    :param int opflags:
        *undescribed*

.. _`futex_lock_pi`:

futex_lock_pi
=============

.. c:function:: int futex_lock_pi(u_int32_t *uaddr, struct timespec *timeout, int opflags)

    block on uaddr as a PI mutex

    :param u_int32_t \*uaddr:
        *undescribed*

    :param struct timespec \*timeout:
        *undescribed*

    :param int opflags:
        *undescribed*

.. _`futex_unlock_pi`:

futex_unlock_pi
===============

.. c:function:: int futex_unlock_pi(u_int32_t *uaddr, int opflags)

    release uaddr as a PI mutex, waking the top waiter

    :param u_int32_t \*uaddr:
        *undescribed*

    :param int opflags:
        *undescribed*

.. _`futex_cmp_requeue`:

futex_cmp_requeue
=================

.. c:function:: int futex_cmp_requeue(u_int32_t *uaddr, u_int32_t val, u_int32_t *uaddr2, int nr_wake, int nr_requeue, int opflags)

    requeue tasks from uaddr to uaddr2

    :param u_int32_t \*uaddr:
        *undescribed*

    :param u_int32_t val:
        *undescribed*

    :param u_int32_t \*uaddr2:
        *undescribed*

    :param int nr_wake:
        wake up to this many tasks

    :param int nr_requeue:
        requeue up to this many tasks

    :param int opflags:
        *undescribed*

.. This file was automatic generated / don't edit.

