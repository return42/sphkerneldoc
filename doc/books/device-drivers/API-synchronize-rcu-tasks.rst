
.. _API-synchronize-rcu-tasks:

=====================
synchronize_rcu_tasks
=====================

*man synchronize_rcu_tasks(9)*

*4.6.0-rc1*

wait until an rcu-tasks grace period has elapsed.


Synopsis
========

.. c:function:: void synchronize_rcu_tasks( void )

Arguments
=========

``void``
    no arguments


Description
===========

Control will return to the caller some time after a full rcu-tasks grace period has elapsed, in other words after all currently executing rcu-tasks read-side critical sections have
elapsed. These read-side critical sections are delimited by calls to ``schedule``, ``cond_resched_rcu_qs``, idle execution, userspace execution, calls to ``synchronize_rcu_tasks``,
and (in theory, anyway) ``cond_resched``.

This is a very specialized primitive, intended only for a few uses in tracing and other situations requiring manipulation of function preambles and profiling hooks. The
``synchronize_rcu_tasks`` function is not (yet) intended for heavy use from multiple CPUs.

Note that this guarantee implies further memory-ordering guarantees. On systems with more than one CPU, when ``synchronize_rcu_tasks`` returns, each CPU is guaranteed to have
executed a full memory barrier since the end of its last RCU-tasks read-side critical section whose beginning preceded the call to ``synchronize_rcu_tasks``. In addition, each CPU
having an RCU-tasks read-side critical section that extends beyond the return from ``synchronize_rcu_tasks`` is guaranteed to have executed a full memory barrier after the
beginning of ``synchronize_rcu_tasks`` and before the beginning of that RCU-tasks read-side critical section. Note that these guarantees include CPUs that are offline, idle, or
executing in user mode, as well as CPUs that are executing in the kernel.

Furthermore, if CPU A invoked ``synchronize_rcu_tasks``, which returned to its caller on CPU B, then both CPU A and CPU B are guaranteed to have executed a full memory barrier
during the execution of ``synchronize_rcu_tasks`` -- even if CPU A and CPU B are the same CPU (but again only if the system has more than one CPU).
