.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/rcu/tree.c

.. _`rcu_idle_enter`:

rcu_idle_enter
==============

.. c:function:: void rcu_idle_enter( void)

    inform RCU that current CPU is entering idle

    :param  void:
        no arguments

.. _`rcu_idle_enter.description`:

Description
-----------

Enter idle mode, in other words, -leave- the mode in which RCU
read-side critical sections can occur.  (Though RCU read-side
critical sections can occur in irq handlers in idle, a possibility
handled by \ :c:func:`irq_enter`\  and \ :c:func:`irq_exit`\ .)

We crowbar the ->dynticks_nesting field to zero to allow for
the possibility of usermode upcalls having messed up our count
of interrupt nesting level during the prior busy period.

.. _`rcu_user_enter`:

rcu_user_enter
==============

.. c:function:: void rcu_user_enter( void)

    inform RCU that we are resuming userspace.

    :param  void:
        no arguments

.. _`rcu_user_enter.description`:

Description
-----------

Enter RCU idle mode right before resuming userspace.  No use of RCU
is permitted between this call and \ :c:func:`rcu_user_exit`\ . This way the
CPU doesn't need to maintain the tick for RCU maintenance purposes
when the CPU runs in userspace.

.. _`rcu_irq_exit`:

rcu_irq_exit
============

.. c:function:: void rcu_irq_exit( void)

    inform RCU that current CPU is exiting irq towards idle

    :param  void:
        no arguments

.. _`rcu_irq_exit.description`:

Description
-----------

Exit from an interrupt handler, which might possibly result in entering
idle mode, in other words, leaving the mode in which read-side critical
sections can occur.  The caller must have disabled interrupts.

This code assumes that the idle loop never does anything that might
result in unbalanced calls to \ :c:func:`irq_enter`\  and \ :c:func:`irq_exit`\ .  If your
architecture violates this assumption, RCU will give you what you
deserve, good and hard.  But very infrequently and irreproducibly.

Use things like work queues to work around this limitation.

You have been warned.

.. _`rcu_idle_exit`:

rcu_idle_exit
=============

.. c:function:: void rcu_idle_exit( void)

    inform RCU that current CPU is leaving idle

    :param  void:
        no arguments

.. _`rcu_idle_exit.description`:

Description
-----------

Exit idle mode, in other words, -enter- the mode in which RCU
read-side critical sections can occur.

We crowbar the ->dynticks_nesting field to DYNTICK_TASK_NEST to
allow for the possibility of usermode upcalls messing up our count
of interrupt nesting level during the busy period that is just
now starting.

.. _`rcu_user_exit`:

rcu_user_exit
=============

.. c:function:: void rcu_user_exit( void)

    inform RCU that we are exiting userspace.

    :param  void:
        no arguments

.. _`rcu_user_exit.description`:

Description
-----------

Exit RCU idle mode while entering the kernel because it can
run a RCU read side critical section anytime.

.. _`rcu_irq_enter`:

rcu_irq_enter
=============

.. c:function:: void rcu_irq_enter( void)

    inform RCU that current CPU is entering irq away from idle

    :param  void:
        no arguments

.. _`rcu_irq_enter.description`:

Description
-----------

Enter an interrupt handler, which might possibly result in exiting
idle mode, in other words, entering the mode in which read-side critical
sections can occur.  The caller must have disabled interrupts.

Note that the Linux kernel is fully capable of entering an interrupt
handler that it never exits, for example when doing upcalls to
user mode!  This code assumes that the idle loop never does upcalls to
user mode.  If your architecture does do upcalls from the idle loop (or
does anything else that results in unbalanced calls to the \ :c:func:`irq_enter`\ 
and \ :c:func:`irq_exit`\  functions), RCU will give you what you deserve, good
and hard.  But very infrequently and irreproducibly.

Use things like work queues to work around this limitation.

You have been warned.

.. _`rcu_nmi_enter`:

rcu_nmi_enter
=============

.. c:function:: void rcu_nmi_enter( void)

    inform RCU of entry to NMI context

    :param  void:
        no arguments

.. _`rcu_nmi_enter.description`:

Description
-----------

If the CPU was idle from RCU's viewpoint, update rdtp->dynticks and
rdtp->dynticks_nmi_nesting to let the RCU grace-period handling know
that the CPU is active.  This implementation permits nested NMIs, as
long as the nesting level does not overflow an int.  (You will probably
run out of stack space first.)

.. _`rcu_nmi_exit`:

rcu_nmi_exit
============

.. c:function:: void rcu_nmi_exit( void)

    inform RCU of exit from NMI context

    :param  void:
        no arguments

.. _`rcu_nmi_exit.description`:

Description
-----------

If we are returning from the outermost NMI handler that interrupted an
RCU-idle period, update rdtp->dynticks and rdtp->dynticks_nmi_nesting
to let the RCU grace-period handling know that the CPU is back to
being RCU-idle.

.. _`__rcu_is_watching`:

__rcu_is_watching
=================

.. c:function:: bool notrace __rcu_is_watching( void)

    are RCU read-side critical sections safe?

    :param  void:
        no arguments

.. _`__rcu_is_watching.description`:

Description
-----------

Return true if RCU is watching the running CPU, which means that
this CPU can safely enter RCU read-side critical sections.  Unlike
\ :c:func:`rcu_is_watching`\ , the caller of \\ :c:func:`__rcu_is_watching`\  must have at
least disabled preemption.

.. _`rcu_is_watching`:

rcu_is_watching
===============

.. c:function:: bool notrace rcu_is_watching( void)

    see if RCU thinks that the current CPU is idle

    :param  void:
        no arguments

.. _`rcu_is_watching.description`:

Description
-----------

If the current CPU is in its idle loop and is neither in an interrupt
or NMI handler, return true.

.. _`rcu_is_cpu_rrupt_from_idle`:

rcu_is_cpu_rrupt_from_idle
==========================

.. c:function:: int rcu_is_cpu_rrupt_from_idle( void)

    see if idle or immediately interrupted from idle

    :param  void:
        no arguments

.. _`rcu_is_cpu_rrupt_from_idle.description`:

Description
-----------

If the current CPU is idle or running at a first-level (not nested)
interrupt from idle, return true.  The caller must have at least
disabled preemption.

.. _`rcu_cpu_stall_reset`:

rcu_cpu_stall_reset
===================

.. c:function:: void rcu_cpu_stall_reset( void)

    prevent further stall warnings in current grace period

    :param  void:
        no arguments

.. _`rcu_cpu_stall_reset.description`:

Description
-----------

Set the stall-warning timeout way off into the future, thus preventing
any RCU CPU stall-warning messages from appearing in the current set of
RCU grace periods.

The caller must disable hard irqs.

.. _`synchronize_sched`:

synchronize_sched
=================

.. c:function:: void synchronize_sched( void)

    wait until an rcu-sched grace period has elapsed.

    :param  void:
        no arguments

.. _`synchronize_sched.description`:

Description
-----------

Control will return to the caller some time after a full rcu-sched
grace period has elapsed, in other words after all currently executing
rcu-sched read-side critical sections have completed.   These read-side
critical sections are delimited by \ :c:func:`rcu_read_lock_sched`\  and
\ :c:func:`rcu_read_unlock_sched`\ , and may be nested.  Note that \ :c:func:`preempt_disable`\ ,
\ :c:func:`local_irq_disable`\ , and so on may be used in place of
\ :c:func:`rcu_read_lock_sched`\ .

This means that all preempt_disable code sequences, including NMI and
non-threaded hardware-interrupt handlers, in progress on entry will
have completed before this primitive returns.  However, this does not
guarantee that softirq handlers will have completed, since in some
kernels, these handlers can run in process context, and can block.

Note that this guarantee implies further memory-ordering guarantees.
On systems with more than one CPU, when \ :c:func:`synchronize_sched`\  returns,
each CPU is guaranteed to have executed a full memory barrier since the
end of its last RCU-sched read-side critical section whose beginning
preceded the call to \ :c:func:`synchronize_sched`\ .  In addition, each CPU having
an RCU read-side critical section that extends beyond the return from
\ :c:func:`synchronize_sched`\  is guaranteed to have executed a full memory barrier
after the beginning of \ :c:func:`synchronize_sched`\  and before the beginning of
that RCU read-side critical section.  Note that these guarantees include
CPUs that are offline, idle, or executing in user mode, as well as CPUs
that are executing in the kernel.

Furthermore, if CPU A invoked \ :c:func:`synchronize_sched`\ , which returned
to its caller on CPU B, then both CPU A and CPU B are guaranteed
to have executed a full memory barrier during the execution of
\ :c:func:`synchronize_sched`\  -- even if CPU A and CPU B are the same CPU (but
again only if the system has more than one CPU).

This primitive provides the guarantees made by the (now removed)
\ :c:func:`synchronize_kernel`\  API.  In contrast, \ :c:func:`synchronize_rcu`\  only
guarantees that \ :c:func:`rcu_read_lock`\  sections will have completed.
In "classic RCU", these two guarantees happen to be one and
the same, but can differ in realtime RCU implementations.

.. _`synchronize_rcu_bh`:

synchronize_rcu_bh
==================

.. c:function:: void synchronize_rcu_bh( void)

    wait until an rcu_bh grace period has elapsed.

    :param  void:
        no arguments

.. _`synchronize_rcu_bh.description`:

Description
-----------

Control will return to the caller some time after a full rcu_bh grace
period has elapsed, in other words after all currently executing rcu_bh
read-side critical sections have completed.  RCU read-side critical
sections are delimited by \ :c:func:`rcu_read_lock_bh`\  and \ :c:func:`rcu_read_unlock_bh`\ ,
and may be nested.

See the description of \ :c:func:`synchronize_sched`\  for more detailed information
on memory ordering guarantees.

.. _`get_state_synchronize_rcu`:

get_state_synchronize_rcu
=========================

.. c:function:: unsigned long get_state_synchronize_rcu( void)

    Snapshot current RCU state

    :param  void:
        no arguments

.. _`get_state_synchronize_rcu.description`:

Description
-----------

Returns a cookie that is used by a later call to \ :c:func:`cond_synchronize_rcu`\ 
to determine whether or not a full grace period has elapsed in the
meantime.

.. _`cond_synchronize_rcu`:

cond_synchronize_rcu
====================

.. c:function:: void cond_synchronize_rcu(unsigned long oldstate)

    Conditionally wait for an RCU grace period

    :param unsigned long oldstate:
        return value from earlier call to \ :c:func:`get_state_synchronize_rcu`\ 

.. _`cond_synchronize_rcu.description`:

Description
-----------

If a full RCU grace period has elapsed since the earlier call to
\ :c:func:`get_state_synchronize_rcu`\ , just return.  Otherwise, invoke
\ :c:func:`synchronize_rcu`\  to wait for a full grace period.

Yes, this function does not take counter wrap into account.  But
counter wrap is harmless.  If the counter wraps, we have waited for
more than 2 billion grace periods (and way more on a 64-bit system!),
so waiting for one additional grace period should be just fine.

.. _`get_state_synchronize_sched`:

get_state_synchronize_sched
===========================

.. c:function:: unsigned long get_state_synchronize_sched( void)

    Snapshot current RCU-sched state

    :param  void:
        no arguments

.. _`get_state_synchronize_sched.description`:

Description
-----------

Returns a cookie that is used by a later call to \ :c:func:`cond_synchronize_sched`\ 
to determine whether or not a full grace period has elapsed in the
meantime.

.. _`cond_synchronize_sched`:

cond_synchronize_sched
======================

.. c:function:: void cond_synchronize_sched(unsigned long oldstate)

    Conditionally wait for an RCU-sched grace period

    :param unsigned long oldstate:
        return value from earlier call to \ :c:func:`get_state_synchronize_sched`\ 

.. _`cond_synchronize_sched.description`:

Description
-----------

If a full RCU-sched grace period has elapsed since the earlier call to
\ :c:func:`get_state_synchronize_sched`\ , just return.  Otherwise, invoke
\ :c:func:`synchronize_sched`\  to wait for a full grace period.

Yes, this function does not take counter wrap into account.  But
counter wrap is harmless.  If the counter wraps, we have waited for
more than 2 billion grace periods (and way more on a 64-bit system!),
so waiting for one additional grace period should be just fine.

.. _`synchronize_sched_expedited`:

synchronize_sched_expedited
===========================

.. c:function:: void synchronize_sched_expedited( void)

    Brute-force RCU-sched grace period

    :param  void:
        no arguments

.. _`synchronize_sched_expedited.description`:

Description
-----------

Wait for an RCU-sched grace period to elapse, but use a "big hammer"
approach to force the grace period to end quickly.  This consumes
significant time on all CPUs and is unfriendly to real-time workloads,
so is thus not recommended for any sort of common-case code.  In fact,
if you are using \ :c:func:`synchronize_sched_expedited`\  in a loop, please
restructure your code to batch your updates, and then use a single
\ :c:func:`synchronize_sched`\  instead.

This implementation can be thought of as an application of sequence
locking to expedited grace periods, but using the sequence counter to
determine when someone else has already done the work instead of for
retrying readers.

.. _`rcu_barrier_bh`:

rcu_barrier_bh
==============

.. c:function:: void rcu_barrier_bh( void)

    Wait until all in-flight \ :c:func:`call_rcu_bh`\  callbacks complete.

    :param  void:
        no arguments

.. _`rcu_barrier_sched`:

rcu_barrier_sched
=================

.. c:function:: void rcu_barrier_sched( void)

    Wait for in-flight \ :c:func:`call_rcu_sched`\  callbacks.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.
