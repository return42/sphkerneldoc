
.. _API-synchronize-sched:

=================
synchronize_sched
=================

*man synchronize_sched(9)*

*4.6.0-rc1*

wait until an rcu-sched grace period has elapsed.


Synopsis
========

.. c:function:: void synchronize_sched( void )

Arguments
=========

``void``
    no arguments


Description
===========

Control will return to the caller some time after a full rcu-sched grace period has elapsed, in other words after all currently executing rcu-sched read-side critical sections have
completed. These read-side critical sections are delimited by ``rcu_read_lock_sched`` and ``rcu_read_unlock_sched``, and may be nested. Note that ``preempt_disable``,
``local_irq_disable``, and so on may be used in place of ``rcu_read_lock_sched``.

This means that all preempt_disable code sequences, including NMI and non-threaded hardware-interrupt handlers, in progress on entry will have completed before this primitive
returns. However, this does not guarantee that softirq handlers will have completed, since in some kernels, these handlers can run in process context, and can block.

Note that this guarantee implies further memory-ordering guarantees. On systems with more than one CPU, when ``synchronize_sched`` returns, each CPU is guaranteed to have executed
a full memory barrier since the end of its last RCU-sched read-side critical section whose beginning preceded the call to ``synchronize_sched``. In addition, each CPU having an RCU
read-side critical section that extends beyond the return from ``synchronize_sched`` is guaranteed to have executed a full memory barrier after the beginning of
``synchronize_sched`` and before the beginning of that RCU read-side critical section. Note that these guarantees include CPUs that are offline, idle, or executing in user mode, as
well as CPUs that are executing in the kernel.

Furthermore, if CPU A invoked ``synchronize_sched``, which returned to its caller on CPU B, then both CPU A and CPU B are guaranteed to have executed a full memory barrier during
the execution of ``synchronize_sched`` -- even if CPU A and CPU B are the same CPU (but again only if the system has more than one CPU).

This primitive provides the guarantees made by the (now removed) ``synchronize_kernel`` API. In contrast, ``synchronize_rcu`` only guarantees that ``rcu_read_lock`` sections will
have completed. In “classic RCU”, these two guarantees happen to be one and the same, but can differ in realtime RCU implementations.
