.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/rcu/tree_plugin.h

.. _`synchronize_rcu`:

synchronize_rcu
===============

.. c:function:: void synchronize_rcu( void)

    wait until a grace period has elapsed.

    :param void:
        no arguments
    :type void: 

.. _`synchronize_rcu.description`:

Description
-----------

Control will return to the caller some time after a full grace
period has elapsed, in other words after all currently executing RCU
read-side critical sections have completed.  Note, however, that
upon return from \ :c:func:`synchronize_rcu`\ , the caller might well be executing
concurrently with new RCU read-side critical sections that began while
\ :c:func:`synchronize_rcu`\  was waiting.  RCU read-side critical sections are
delimited by \ :c:func:`rcu_read_lock`\  and \ :c:func:`rcu_read_unlock`\ , and may be nested.
In addition, regions of code across which interrupts, preemption, or
softirqs have been disabled also serve as RCU read-side critical
sections.  This includes hardware interrupt handlers, softirq handlers,
and NMI handlers.

Note that this guarantee implies further memory-ordering guarantees.
On systems with more than one CPU, when \ :c:func:`synchronize_rcu`\  returns,
each CPU is guaranteed to have executed a full memory barrier since
the end of its last RCU read-side critical section whose beginning
preceded the call to \ :c:func:`synchronize_rcu`\ .  In addition, each CPU having
an RCU read-side critical section that extends beyond the return from
\ :c:func:`synchronize_rcu`\  is guaranteed to have executed a full memory barrier
after the beginning of \ :c:func:`synchronize_rcu`\  and before the beginning of
that RCU read-side critical section.  Note that these guarantees include
CPUs that are offline, idle, or executing in user mode, as well as CPUs
that are executing in the kernel.

Furthermore, if CPU A invoked \ :c:func:`synchronize_rcu`\ , which returned
to its caller on CPU B, then both CPU A and CPU B are guaranteed
to have executed a full memory barrier during the execution of
\ :c:func:`synchronize_rcu`\  -- even if CPU A and CPU B are the same CPU (but
again only if the system has more than one CPU).

.. This file was automatic generated / don't edit.

