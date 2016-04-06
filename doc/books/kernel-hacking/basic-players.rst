
.. _basic-players:

===========
The Players
===========

At any time each of the CPUs in a system can be:

-  not associated with any process, serving a hardware interrupt;

-  not associated with any process, serving a softirq or tasklet;

-  running in kernel space, associated with a process (user context);

-  running a process in user space.

There is an ordering between these. The bottom two can preempt each other, but above that is a strict hierarchy: each can only be preempted by the ones above it. For example, while
a softirq is running on a CPU, no other softirq will preempt it, but a hardware interrupt can. However, any other CPUs in the system execute independently.

We'll see a number of ways that the user context can block interrupts, to become truly non-preemptable.


.. _basics-usercontext:

User Context
============

User context is when you are coming in from a system call or other trap: like userspace, you can be preempted by more important tasks and by interrupts. You can sleep, by calling
``schedule()``.

    **Note**

    You are always in user context on module load and unload, and on operations on the block device layer.

In user context, the ``current`` pointer (indicating the task we are currently executing) is valid, and ``in_interrupt()`` (``include/linux/interrupt.h``) is false.

    **Caution**

    Beware that if you have preemption or softirqs disabled (see below), ``in_interrupt()`` will return a false positive.


.. _basics-hardirqs:

Hardware Interrupts (Hard IRQs)
===============================

Timer ticks, network cards and keyboard are examples of real hardware which produce interrupts at any time. The kernel runs interrupt handlers, which services the hardware. The
kernel guarantees that this handler is never re-entered: if the same interrupt arrives, it is queued (or dropped). Because it disables interrupts, this handler has to be fast:
frequently it simply acknowledges the interrupt, marks a 'software interrupt' for execution and exits.

You can tell you are in a hardware interrupt, because ``in_irq()`` returns true.

    **Caution**

    Beware that this will return a false positive if interrupts are disabled (see below).


.. _basics-softirqs:

Software Interrupt Context: Softirqs and Tasklets
=================================================

Whenever a system call is about to return to userspace, or a hardware interrupt handler exits, any 'software interrupts' which are marked pending (usually by hardware interrupts)
are run (``kernel/softirq.c``).

Much of the real interrupt handling work is done here. Early in the transition to SMP, there were only 'bottom halves' (BHs), which didn't take advantage of multiple CPUs. Shortly
after we switched from wind-up computers made of match-sticks and snot, we abandoned this limitation and switched to 'softirqs'.

``include/linux/interrupt.h`` lists the different softirqs. A very important softirq is the timer softirq (``include/linux/timer.h``): you can register to have it call functions
for you in a given length of time.

Softirqs are often a pain to deal with, since the same softirq will run simultaneously on more than one CPU. For this reason, tasklets (``include/linux/interrupt.h``) are more
often used: they are dynamically-registrable (meaning you can have as many as you want), and they also guarantee that any tasklet will only run on one CPU at any time, although
different tasklets can run simultaneously.

    **Caution**

    The name 'tasklet' is misleading: they have nothing to do with 'tasks', and probably more to do with some bad vodka Alexey Kuznetsov had at the time.

You can tell you are in a softirq (or tasklet) using the ``in_softirq()`` macro (``include/linux/interrupt.h``).

    **Caution**

    Beware that this will return a false positive if a bh lock (see below) is held.
