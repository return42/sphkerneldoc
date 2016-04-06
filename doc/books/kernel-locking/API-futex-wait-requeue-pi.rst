
.. _API-futex-wait-requeue-pi:

=====================
futex_wait_requeue_pi
=====================

*man futex_wait_requeue_pi(9)*

*4.6.0-rc1*

Wait on uaddr and take uaddr2


Synopsis
========

.. c:function:: int futex_wait_requeue_pi( u32 __user * uaddr, unsigned int flags, u32 val, ktime_t * abs_time, u32 bitset, u32 __user * uaddr2 )

Arguments
=========

``uaddr``
    the futex we initially wait on (non-pi)

``flags``
    futex flags (FLAGS_SHARED, FLAGS_CLOCKRT, etc.), they must be the same type, no requeueing from private to shared, etc.

``val``
    the expected value of uaddr

``abs_time``
    absolute timeout

``bitset``
    32 bit wakeup bitset set by userspace, defaults to all

``uaddr2``
    the pi futex we will take prior to returning to user-space


Description
===========

The caller will wait on uaddr and will be requeued by ``futex_requeue`` to uaddr2 which must be PI aware and unique from uaddr. Normal wakeup will wake on uaddr2 and complete the
acquisition of the rt_mutex prior to returning to userspace. This ensures the rt_mutex maintains an owner when it has waiters; without one, the pi logic would not know which task
to boost/deboost, if there was a need to.

We call schedule in ``futex_wait_queue_me`` when we enqueue and return there via the following-- 1) wakeup on uaddr2 after an atomic lock acquisition by ``futex_requeue`` 2) wakeup
on uaddr2 after a requeue 3) signal 4) timeout

If 3, cleanup and return -ERESTARTNOINTR.

If 2, we may then block on trying to take the rt_mutex and return via: 5) successful lock 6) signal 7) timeout 8) other lock acquisition failure

If 6, return -EWOULDBLOCK (restarting the syscall would do the same).

If 4 or 7, we cleanup and return with -ETIMEDOUT.


Return
======

0 - On success; <0 - On error
