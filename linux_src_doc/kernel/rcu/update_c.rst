.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/rcu/update.c

.. _`rcu_read_lock_sched_held`:

rcu_read_lock_sched_held
========================

.. c:function:: int rcu_read_lock_sched_held( void)

    might we be in RCU-sched read-side critical section?

    :param  void:
        no arguments

.. _`rcu_read_lock_sched_held.description`:

Description
-----------

If CONFIG_DEBUG_LOCK_ALLOC is selected, returns nonzero iff in an
RCU-sched read-side critical section.  In absence of
CONFIG_DEBUG_LOCK_ALLOC, this assumes we are in an RCU-sched read-side
critical section unless it can prove otherwise.  Note that disabling
of preemption (including disabling irqs) counts as an RCU-sched
read-side critical section.  This is useful for debug checks in functions
that required that they be called within an RCU-sched read-side
critical section.

Check \ :c:func:`debug_lockdep_rcu_enabled`\  to prevent false positives during boot
and while lockdep is disabled.

Note that if the CPU is in the idle loop from an RCU point of
view (ie: that we are in the section between \ :c:func:`rcu_idle_enter`\  and
\ :c:func:`rcu_idle_exit`\ ) then \ :c:func:`rcu_read_lock_held`\  returns false even if the CPU
did an \ :c:func:`rcu_read_lock`\ .  The reason for this is that RCU ignores CPUs
that are in such a section, considering these as in extended quiescent
state, so such a CPU is effectively never in an RCU read-side critical
section regardless of what RCU primitives it invokes.  This state of
affairs is required --- we need to keep an RCU-free window in idle
where the CPU may possibly enter into low power mode. This way we can
notice an extended quiescent state to other CPUs that started a grace
period. Otherwise we would delay any grace period as long as we run in
the idle task.

Similarly, we avoid claiming an SRCU read lock held if the current
CPU is offline.

.. _`rcu_expedite_gp`:

rcu_expedite_gp
===============

.. c:function:: void rcu_expedite_gp( void)

    Expedite future RCU grace periods

    :param  void:
        no arguments

.. _`rcu_expedite_gp.description`:

Description
-----------

After a call to this function, future calls to \ :c:func:`synchronize_rcu`\  and
friends act as the corresponding \ :c:func:`synchronize_rcu_expedited`\  function
had instead been called.

.. _`rcu_unexpedite_gp`:

rcu_unexpedite_gp
=================

.. c:function:: void rcu_unexpedite_gp( void)

    Cancel prior \ :c:func:`rcu_expedite_gp`\  invocation

    :param  void:
        no arguments

.. _`rcu_unexpedite_gp.description`:

Description
-----------

Undo a prior call to \ :c:func:`rcu_expedite_gp`\ .  If all prior calls to
\ :c:func:`rcu_expedite_gp`\  are undone by a subsequent call to \ :c:func:`rcu_unexpedite_gp`\ ,
and if the rcu_expedited sysfs/boot parameter is not set, then all
subsequent calls to \ :c:func:`synchronize_rcu`\  and friends will return to
their normal non-expedited behavior.

.. _`rcu_read_lock_held`:

rcu_read_lock_held
==================

.. c:function:: int rcu_read_lock_held( void)

    might we be in RCU read-side critical section?

    :param  void:
        no arguments

.. _`rcu_read_lock_held.description`:

Description
-----------

If CONFIG_DEBUG_LOCK_ALLOC is selected, returns nonzero iff in an RCU
read-side critical section.  In absence of CONFIG_DEBUG_LOCK_ALLOC,
this assumes we are in an RCU read-side critical section unless it can
prove otherwise.  This is useful for debug checks in functions that
require that they be called within an RCU read-side critical section.

Checks \ :c:func:`debug_lockdep_rcu_enabled`\  to prevent false positives during boot
and while lockdep is disabled.

Note that \ :c:func:`rcu_read_lock`\  and the matching \ :c:func:`rcu_read_unlock`\  must
occur in the same context, for example, it is illegal to invoke
\ :c:func:`rcu_read_unlock`\  in process context if the matching \ :c:func:`rcu_read_lock`\ 
was invoked from within an irq handler.

Note that \ :c:func:`rcu_read_lock`\  is disallowed if the CPU is either idle or
offline from an RCU perspective, so check for those as well.

.. _`rcu_read_lock_bh_held`:

rcu_read_lock_bh_held
=====================

.. c:function:: int rcu_read_lock_bh_held( void)

    might we be in RCU-bh read-side critical section?

    :param  void:
        no arguments

.. _`rcu_read_lock_bh_held.description`:

Description
-----------

Check for bottom half being disabled, which covers both the
CONFIG_PROVE_RCU and not cases.  Note that if someone uses
\ :c:func:`rcu_read_lock_bh`\ , but then later enables BH, lockdep (if enabled)
will show the situation.  This is useful for debug checks in functions
that require that they be called within an RCU read-side critical
section.

Check \ :c:func:`debug_lockdep_rcu_enabled`\  to prevent false positives during boot.

Note that \ :c:func:`rcu_read_lock`\  is disallowed if the CPU is either idle or
offline from an RCU perspective, so check for those as well.

.. _`wakeme_after_rcu`:

wakeme_after_rcu
================

.. c:function:: void wakeme_after_rcu(struct rcu_head *head)

    Callback function to awaken a task after grace period

    :param struct rcu_head \*head:
        Pointer to rcu_head member within rcu_synchronize structure

.. _`wakeme_after_rcu.description`:

Description
-----------

Awaken the corresponding task now that a grace period has elapsed.

.. _`init_rcu_head_on_stack`:

init_rcu_head_on_stack
======================

.. c:function:: void init_rcu_head_on_stack(struct rcu_head *head)

    initialize on-stack rcu_head for debugobjects

    :param struct rcu_head \*head:
        pointer to rcu_head structure to be initialized

.. _`init_rcu_head_on_stack.description`:

Description
-----------

This function informs debugobjects of a new rcu_head structure that
has been allocated as an auto variable on the stack.  This function
is not required for rcu_head structures that are statically defined or
that are dynamically allocated on the heap.  This function has no
effect for !CONFIG_DEBUG_OBJECTS_RCU_HEAD kernel builds.

.. _`destroy_rcu_head_on_stack`:

destroy_rcu_head_on_stack
=========================

.. c:function:: void destroy_rcu_head_on_stack(struct rcu_head *head)

    destroy on-stack rcu_head for debugobjects

    :param struct rcu_head \*head:
        pointer to rcu_head structure to be initialized

.. _`destroy_rcu_head_on_stack.description`:

Description
-----------

This function informs debugobjects that an on-stack rcu_head structure
is about to go out of scope.  As with \ :c:func:`init_rcu_head_on_stack`\ , this
function is not required for rcu_head structures that are statically
defined or that are dynamically allocated on the heap.  Also as with
\ :c:func:`init_rcu_head_on_stack`\ , this function has no effect for
!CONFIG_DEBUG_OBJECTS_RCU_HEAD kernel builds.

.. _`call_rcu_tasks`:

call_rcu_tasks
==============

.. c:function:: void call_rcu_tasks(struct rcu_head *rhp, rcu_callback_t func)

    Queue an RCU for invocation task-based grace period

    :param struct rcu_head \*rhp:
        structure to be used for queueing the RCU updates.

    :param rcu_callback_t func:
        actual callback function to be invoked after the grace period

.. _`call_rcu_tasks.description`:

Description
-----------

The callback function will be invoked some time after a full grace
period elapses, in other words after all currently executing RCU
read-side critical sections have completed. \ :c:func:`call_rcu_tasks`\  assumes
that the read-side critical sections end at a voluntary context
switch (not a preemption!), entry into idle, or transition to usermode
execution.  As such, there are no read-side primitives analogous to
\ :c:func:`rcu_read_lock`\  and \ :c:func:`rcu_read_unlock`\  because this primitive is intended
to determine that all tasks have passed through a safe state, not so
much for data-strcuture synchronization.

See the description of \ :c:func:`call_rcu`\  for more detailed information on
memory ordering guarantees.

.. _`synchronize_rcu_tasks`:

synchronize_rcu_tasks
=====================

.. c:function:: void synchronize_rcu_tasks( void)

    wait until an rcu-tasks grace period has elapsed.

    :param  void:
        no arguments

.. _`synchronize_rcu_tasks.description`:

Description
-----------

Control will return to the caller some time after a full rcu-tasks
grace period has elapsed, in other words after all currently
executing rcu-tasks read-side critical sections have elapsed.  These
read-side critical sections are delimited by calls to \ :c:func:`schedule`\ ,
\ :c:func:`cond_resched_rcu_qs`\ , idle execution, userspace execution, calls
to \ :c:func:`synchronize_rcu_tasks`\ , and (in theory, anyway) \ :c:func:`cond_resched`\ .

This is a very specialized primitive, intended only for a few uses in
tracing and other situations requiring manipulation of function
preambles and profiling hooks.  The \ :c:func:`synchronize_rcu_tasks`\  function
is not (yet) intended for heavy use from multiple CPUs.

Note that this guarantee implies further memory-ordering guarantees.
On systems with more than one CPU, when \ :c:func:`synchronize_rcu_tasks`\  returns,
each CPU is guaranteed to have executed a full memory barrier since the
end of its last RCU-tasks read-side critical section whose beginning
preceded the call to \ :c:func:`synchronize_rcu_tasks`\ .  In addition, each CPU
having an RCU-tasks read-side critical section that extends beyond
the return from \ :c:func:`synchronize_rcu_tasks`\  is guaranteed to have executed
a full memory barrier after the beginning of \ :c:func:`synchronize_rcu_tasks`\ 
and before the beginning of that RCU-tasks read-side critical section.
Note that these guarantees include CPUs that are offline, idle, or
executing in user mode, as well as CPUs that are executing in the kernel.

Furthermore, if CPU A invoked \ :c:func:`synchronize_rcu_tasks`\ , which returned
to its caller on CPU B, then both CPU A and CPU B are guaranteed
to have executed a full memory barrier during the execution of
\ :c:func:`synchronize_rcu_tasks`\  -- even if CPU A and CPU B are the same CPU
(but again only if the system has more than one CPU).

.. _`rcu_barrier_tasks`:

rcu_barrier_tasks
=================

.. c:function:: void rcu_barrier_tasks( void)

    Wait for in-flight \ :c:func:`call_rcu_tasks`\  callbacks.

    :param  void:
        no arguments

.. _`rcu_barrier_tasks.description`:

Description
-----------

Although the current implementation is guaranteed to wait, it is not
obligated to, for example, if there are no pending callbacks.

.. This file was automatic generated / don't edit.

