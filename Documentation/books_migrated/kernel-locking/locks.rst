.. -*- coding: utf-8; mode: rst -*-

.. _locks:

***************************
Locking in the Linux Kernel
***************************

If I could give you one piece of advice: never sleep with anyone crazier
than yourself. But if I had to give you advice on locking: *keep it
simple*.

Be reluctant to introduce new locks.

Strangely enough, this last one is the exact reverse of my advice when
you *have* slept with someone crazier than yourself. And you should
think about getting a big dog.


.. _lock-intro:

Two Main Types of Kernel Locks: Spinlocks and Mutexes
=====================================================

There are two main types of kernel locks. The fundamental type is the
spinlock (``include/asm/spinlock.h``), which is a very simple
single-holder lock: if you can't get the spinlock, you keep trying
(spinning) until you can. Spinlocks are very small and fast, and can be
used anywhere.

The second type is a mutex (``include/linux/mutex.h``): it is like a
spinlock, but you may block holding a mutex. If you can't lock a mutex,
your task will suspend itself, and be woken up when the mutex is
released. This means the CPU can do something else while you are
waiting. There are many cases when you simply can't sleep (see
:ref:`sleeping-things`), and so have to use a spinlock instead.

Neither type of lock is recursive: see :ref:`deadlock`.


.. _uniprocessor:

Locks and Uniprocessor Kernels
==============================

For kernels compiled without ``CONFIG_SMP``, and without
``CONFIG_PREEMPT`` spinlocks do not exist at all. This is an excellent
design decision: when no-one else can run at the same time, there is no
reason to have a lock.

If the kernel is compiled without ``CONFIG_SMP``, but ``CONFIG_PREEMPT``
is set, then spinlocks simply disable preemption, which is sufficient to
prevent any races. For most purposes, we can think of preemption as
equivalent to SMP, and not worry about it separately.

You should always test your locking code with ``CONFIG_SMP`` and
``CONFIG_PREEMPT`` enabled, even if you don't have an SMP test box,
because it will still catch some kinds of locking bugs.

Mutexes still exist, because they are required for synchronization
between user contexts, as we will see below.


.. _usercontextlocking:

Locking Only In User Context
============================

If you have a data structure which is only ever accessed from user
context, then you can use a simple mutex (``include/linux/mutex.h``) to
protect it. This is the most trivial case: you initialize the mutex.
Then you can call :c:func:`mutex_lock_interruptible()` to grab the
mutex, and :c:func:`mutex_unlock()` to release it. There is also a
:c:func:`mutex_lock()`, which should be avoided, because it will not
return if a signal is received.

Example: ``net/netfilter/nf_sockopt.c`` allows registration of new
:c:func:`setsockopt()` and :c:func:`getsockopt()` calls, with
:c:func:`nf_register_sockopt()`. Registration and de-registration
are only done on module load and unload (and boot time, where there is
no concurrency), and the list of registrations is only consulted for an
unknown :c:func:`setsockopt()` or :c:func:`getsockopt()` system
call. The ``nf_sockopt_mutex`` is perfect to protect this, especially
since the setsockopt and getsockopt calls may well sleep.


.. _lock-user-bh:

Locking Between User Context and Softirqs
=========================================

If a softirq shares data with user context, you have two problems.
Firstly, the current user context can be interrupted by a softirq, and
secondly, the critical region could be entered from another CPU. This is
where :c:func:`spin_lock_bh()` (``include/linux/spinlock.h``) is
used. It disables softirqs on that CPU, then grabs the lock.
:c:func:`spin_unlock_bh()` does the reverse. (The '_bh' suffix is a
historical reference to "Bottom Halves", the old name for software
interrupts. It should really be called spin_lock_softirq()' in a
perfect world).

Note that you can also use :c:func:`spin_lock_irq()` or
:c:func:`spin_lock_irqsave()` here, which stop hardware interrupts
as well: see :ref:`hardirq-context`.

This works perfectly for UP as well: the spin lock vanishes, and this
macro simply becomes :c:func:`local_bh_disable()`
(``include/linux/interrupt.h``), which protects you from the softirq
being run.


.. _lock-user-tasklet:

Locking Between User Context and Tasklets
=========================================

This is exactly the same as above, because tasklets are actually run
from a softirq.


.. _lock-user-timers:

Locking Between User Context and Timers
=======================================

This, too, is exactly the same as above, because timers are actually run
from a softirq. From a locking point of view, tasklets and timers are
identical.


.. _lock-tasklets:

Locking Between Tasklets/Timers
===============================

Sometimes a tasklet or timer might want to share data with another
tasklet or timer.


.. _lock-tasklets-same:

The Same Tasklet/Timer
----------------------

Since a tasklet is never run on two CPUs at once, you don't need to
worry about your tasklet being reentrant (running twice at once), even
on SMP.


.. _lock-tasklets-different:

Different Tasklets/Timers
-------------------------

If another tasklet/timer wants to share data with your tasklet or timer
, you will both need to use :c:func:`spin_lock()` and
:c:func:`spin_unlock()` calls. :c:func:`spin_lock_bh()` is
unnecessary here, as you are already in a tasklet, and none will be run
on the same CPU.


.. _lock-softirqs:

Locking Between Softirqs
========================

Often a softirq might want to share data with itself or a tasklet/timer.


.. _lock-softirqs-same:

The Same Softirq
----------------

The same softirq can run on the other CPUs: you can use a per-CPU array
(see :ref:`per-cpu`) for better performance. If you're going so far as
to use a softirq, you probably care about scalable performance enough to
justify the extra complexity.

You'll need to use :c:func:`spin_lock()` and
:c:func:`spin_unlock()` for shared data.


.. _lock-softirqs-different:

Different Softirqs
------------------

You'll need to use :c:func:`spin_lock()` and
:c:func:`spin_unlock()` for shared data, whether it be a timer,
tasklet, different softirq or the same or another softirq: any of them
could be running on a different CPU.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
