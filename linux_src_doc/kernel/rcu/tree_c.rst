.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/rcu/tree.c

.. _`rcu_is_cpu_rrupt_from_idle`:

rcu_is_cpu_rrupt_from_idle
==========================

.. c:function:: int rcu_is_cpu_rrupt_from_idle( void)

    see if idle or immediately interrupted from idle

    :param void:
        no arguments
    :type void: 

.. _`rcu_is_cpu_rrupt_from_idle.description`:

Description
-----------

If the current CPU is idle or running at a first-level (not nested)
interrupt from idle, return true.  The caller must have at least
disabled preemption.

.. _`rcu_idle_enter`:

rcu_idle_enter
==============

.. c:function:: void rcu_idle_enter( void)

    inform RCU that current CPU is entering idle

    :param void:
        no arguments
    :type void: 

.. _`rcu_idle_enter.description`:

Description
-----------

Enter idle mode, in other words, -leave- the mode in which RCU
read-side critical sections can occur.  (Though RCU read-side
critical sections can occur in irq handlers in idle, a possibility
handled by \ :c:func:`irq_enter`\  and \ :c:func:`irq_exit`\ .)

If you add or remove a call to \ :c:func:`rcu_idle_enter`\ , be sure to test with
CONFIG_RCU_EQS_DEBUG=y.

.. _`rcu_user_enter`:

rcu_user_enter
==============

.. c:function:: void rcu_user_enter( void)

    inform RCU that we are resuming userspace.

    :param void:
        no arguments
    :type void: 

.. _`rcu_user_enter.description`:

Description
-----------

Enter RCU idle mode right before resuming userspace.  No use of RCU
is permitted between this call and \ :c:func:`rcu_user_exit`\ . This way the
CPU doesn't need to maintain the tick for RCU maintenance purposes
when the CPU runs in userspace.

If you add or remove a call to \ :c:func:`rcu_user_enter`\ , be sure to test with
CONFIG_RCU_EQS_DEBUG=y.

.. _`rcu_nmi_exit`:

rcu_nmi_exit
============

.. c:function:: void rcu_nmi_exit( void)

    inform RCU of exit from NMI context

    :param void:
        no arguments
    :type void: 

.. _`rcu_nmi_exit.description`:

Description
-----------

If you add or remove a call to \ :c:func:`rcu_nmi_exit`\ , be sure to test
with CONFIG_RCU_EQS_DEBUG=y.

.. _`rcu_irq_exit`:

rcu_irq_exit
============

.. c:function:: void rcu_irq_exit( void)

    inform RCU that current CPU is exiting irq towards idle

    :param void:
        no arguments
    :type void: 

.. _`rcu_irq_exit.description`:

Description
-----------

Exit from an interrupt handler, which might possibly result in entering
idle mode, in other words, leaving the mode in which read-side critical
sections can occur.  The caller must have disabled interrupts.

This code assumes that the idle loop never does anything that might
result in unbalanced calls to \ :c:func:`irq_enter`\  and \ :c:func:`irq_exit`\ .  If your
architecture's idle loop violates this assumption, RCU will give you what
you deserve, good and hard.  But very infrequently and irreproducibly.

Use things like work queues to work around this limitation.

You have been warned.

If you add or remove a call to \ :c:func:`rcu_irq_exit`\ , be sure to test with
CONFIG_RCU_EQS_DEBUG=y.

.. _`rcu_idle_exit`:

rcu_idle_exit
=============

.. c:function:: void rcu_idle_exit( void)

    inform RCU that current CPU is leaving idle

    :param void:
        no arguments
    :type void: 

.. _`rcu_idle_exit.description`:

Description
-----------

Exit idle mode, in other words, -enter- the mode in which RCU
read-side critical sections can occur.

If you add or remove a call to \ :c:func:`rcu_idle_exit`\ , be sure to test with
CONFIG_RCU_EQS_DEBUG=y.

.. _`rcu_user_exit`:

rcu_user_exit
=============

.. c:function:: void rcu_user_exit( void)

    inform RCU that we are exiting userspace.

    :param void:
        no arguments
    :type void: 

.. _`rcu_user_exit.description`:

Description
-----------

Exit RCU idle mode while entering the kernel because it can
run a RCU read side critical section anytime.

If you add or remove a call to \ :c:func:`rcu_user_exit`\ , be sure to test with
CONFIG_RCU_EQS_DEBUG=y.

.. _`rcu_nmi_enter_common`:

rcu_nmi_enter_common
====================

.. c:function:: void rcu_nmi_enter_common(bool irq)

    inform RCU of entry to NMI context

    :param irq:
        Is this call from rcu_irq_enter?
    :type irq: bool

.. _`rcu_nmi_enter_common.description`:

Description
-----------

If the CPU was idle from RCU's viewpoint, update rdp->dynticks and
rdp->dynticks_nmi_nesting to let the RCU grace-period handling know
that the CPU is active.  This implementation permits nested NMIs, as
long as the nesting level does not overflow an int.  (You will probably
run out of stack space first.)

If you add or remove a call to \ :c:func:`rcu_nmi_enter_common`\ , be sure to test
with CONFIG_RCU_EQS_DEBUG=y.

.. _`rcu_nmi_enter`:

rcu_nmi_enter
=============

.. c:function:: void rcu_nmi_enter( void)

    inform RCU of entry to NMI context

    :param void:
        no arguments
    :type void: 

.. _`rcu_irq_enter`:

rcu_irq_enter
=============

.. c:function:: void rcu_irq_enter( void)

    inform RCU that current CPU is entering irq away from idle

    :param void:
        no arguments
    :type void: 

.. _`rcu_irq_enter.description`:

Description
-----------

Enter an interrupt handler, which might possibly result in exiting
idle mode, in other words, entering the mode in which read-side critical
sections can occur.  The caller must have disabled interrupts.

Note that the Linux kernel is fully capable of entering an interrupt
handler that it never exits, for example when doing upcalls to user mode!
This code assumes that the idle loop never does upcalls to user mode.
If your architecture's idle loop does do upcalls to user mode (or does
anything else that results in unbalanced calls to the \ :c:func:`irq_enter`\  and
\ :c:func:`irq_exit`\  functions), RCU will give you what you deserve, good and hard.
But very infrequently and irreproducibly.

Use things like work queues to work around this limitation.

You have been warned.

If you add or remove a call to \ :c:func:`rcu_irq_enter`\ , be sure to test with
CONFIG_RCU_EQS_DEBUG=y.

.. _`rcu_is_watching`:

rcu_is_watching
===============

.. c:function:: bool notrace rcu_is_watching( void)

    see if RCU thinks that the current CPU is idle

    :param void:
        no arguments
    :type void: 

.. _`rcu_is_watching.description`:

Description
-----------

Return true if RCU is watching the running CPU, which means that this
CPU can safely enter RCU read-side critical sections.  In other words,
if the current CPU is in its idle loop and is neither in an interrupt
or NMI handler, return true.

.. _`rcu_cpu_stall_reset`:

rcu_cpu_stall_reset
===================

.. c:function:: void rcu_cpu_stall_reset( void)

    prevent further stall warnings in current grace period

    :param void:
        no arguments
    :type void: 

.. _`rcu_cpu_stall_reset.description`:

Description
-----------

Set the stall-warning timeout way off into the future, thus preventing
any RCU CPU stall-warning messages from appearing in the current set of
RCU grace periods.

The caller must disable hard irqs.

.. _`call_rcu`:

call_rcu
========

.. c:function:: void call_rcu(struct rcu_head *head, rcu_callback_t func)

    Queue an RCU callback for invocation after a grace period.

    :param head:
        structure to be used for queueing the RCU updates.
    :type head: struct rcu_head \*

    :param func:
        actual callback function to be invoked after the grace period
    :type func: rcu_callback_t

.. _`call_rcu.description`:

Description
-----------

The callback function will be invoked some time after a full grace
period elapses, in other words after all pre-existing RCU read-side
critical sections have completed.  However, the callback function
might well execute concurrently with RCU read-side critical sections
that started after \ :c:func:`call_rcu`\  was invoked.  RCU read-side critical
sections are delimited by \ :c:func:`rcu_read_lock`\  and \ :c:func:`rcu_read_unlock`\ , and
may be nested.  In addition, regions of code across which interrupts,
preemption, or softirqs have been disabled also serve as RCU read-side
critical sections.  This includes hardware interrupt handlers, softirq
handlers, and NMI handlers.

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

.. _`get_state_synchronize_rcu`:

get_state_synchronize_rcu
=========================

.. c:function:: unsigned long get_state_synchronize_rcu( void)

    Snapshot current RCU state

    :param void:
        no arguments
    :type void: 

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

    :param oldstate:
        return value from earlier call to \ :c:func:`get_state_synchronize_rcu`\ 
    :type oldstate: unsigned long

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

.. _`rcu_barrier`:

rcu_barrier
===========

.. c:function:: void rcu_barrier( void)

    Wait until all in-flight \ :c:func:`call_rcu`\  callbacks complete.

    :param void:
        no arguments
    :type void: 

.. _`rcu_barrier.description`:

Description
-----------

Note that this primitive does not necessarily wait for an RCU grace period
to complete.  For example, if there are no RCU callbacks queued anywhere
in the system, then \ :c:func:`rcu_barrier`\  is within its rights to return
immediately, without waiting for anything, much less an RCU grace period.

.. This file was automatic generated / don't edit.

