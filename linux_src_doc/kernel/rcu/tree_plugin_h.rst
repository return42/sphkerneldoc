.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/rcu/tree_plugin.h

.. _`call_rcu`:

call_rcu
========

.. c:function:: void call_rcu(struct rcu_head *head, rcu_callback_t func)

    Queue an RCU callback for invocation after a grace period.

    :param struct rcu_head \*head:
        structure to be used for queueing the RCU updates.

    :param rcu_callback_t func:
        actual callback function to be invoked after the grace period

.. _`call_rcu.description`:

Description
-----------

The callback function will be invoked some time after a full grace
period elapses, in other words after all pre-existing RCU read-side
critical sections have completed.  However, the callback function
might well execute concurrently with RCU read-side critical sections
that started after \ :c:func:`call_rcu`\  was invoked.  RCU read-side critical
sections are delimited by \ :c:func:`rcu_read_lock`\  and \ :c:func:`rcu_read_unlock`\ ,
and may be nested.

Note that all CPUs must agree that the grace period extended beyond
all pre-existing RCU read-side critical section.  On systems with more
than one CPU, this means that when "func()" is invoked, each CPU is
guaranteed to have executed a full memory barrier since the end of its
last RCU read-side critical section whose beginning preceded the call
to \ :c:func:`call_rcu`\ .  It also means that each CPU executing an RCU read-side
critical section that continues beyond the start of "func()" must have
executed a memory barrier after the \ :c:func:`call_rcu`\  but before the beginning
of that RCU read-side critical section.  Note that these guarantees
include CPUs that are offline, idle, or executing in user mode, as
well as CPUs that are executing in the kernel.

Furthermore, if CPU A invoked \ :c:func:`call_rcu`\  and CPU B invoked the
resulting RCU callback function "func()", then both CPU A and CPU B are
guaranteed to execute a full memory barrier during the time interval
between the call to \ :c:func:`call_rcu`\  and the invocation of "func()" -- even
if CPU A and CPU B are the same CPU (but again only if the system has
more than one CPU).

.. _`synchronize_rcu`:

synchronize_rcu
===============

.. c:function:: void synchronize_rcu( void)

    wait until a grace period has elapsed.

    :param  void:
        no arguments

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

See the description of \ :c:func:`synchronize_sched`\  for more detailed
information on memory-ordering guarantees.  However, please note
that -only- the memory-ordering guarantees apply.  For example,
\ :c:func:`synchronize_rcu`\  is -not- guaranteed to wait on things like code
protected by \ :c:func:`preempt_disable`\ , instead, \ :c:func:`synchronize_rcu`\  is -only-
guaranteed to wait on RCU read-side critical sections, that is, sections
of code protected by \ :c:func:`rcu_read_lock`\ .

.. _`rcu_barrier`:

rcu_barrier
===========

.. c:function:: void rcu_barrier( void)

    Wait until all in-flight \ :c:func:`call_rcu`\  callbacks complete.

    :param  void:
        no arguments

.. _`rcu_barrier.description`:

Description
-----------

Note that this primitive does not necessarily wait for an RCU grace period
to complete.  For example, if there are no RCU callbacks queued anywhere
in the system, then \ :c:func:`rcu_barrier`\  is within its rights to return
immediately, without waiting for anything, much less an RCU grace period.

.. This file was automatic generated / don't edit.

