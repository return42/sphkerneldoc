.. -*- coding: utf-8; mode: rst -*-

======
core.c
======

.. _`task_curr`:

task_curr
=========

.. c:function:: int task_curr (const struct task_struct *p)

    is this task currently executing on a CPU?

    :param const struct task_struct \*p:
        the task in question.


.. _`task_curr.description`:

Description
-----------

Return: 1 if the task is currently executing. 0 otherwise.


.. _`try_to_wake_up`:

try_to_wake_up
==============

.. c:function:: int try_to_wake_up (struct task_struct *p, unsigned int state, int wake_flags)

    wake up a thread

    :param struct task_struct \*p:
        the thread to be awakened

    :param unsigned int state:
        the mask of task states that can be woken

    :param int wake_flags:
        wake modifier flags (WF_\*)


.. _`try_to_wake_up.description`:

Description
-----------

Put it on the run-queue if it's not already there. The "current"
thread is always on the run-queue (except when the actual
re-schedule is in progress), and as such you're allowed to do
the simpler "current->state = TASK_RUNNING" to mark yourself
runnable without the overhead of this.

Return: ``true`` if ``p`` was woken up, ``false`` if it was already running.
or ``state`` didn't match ``p``\ 's state.


.. _`try_to_wake_up_local`:

try_to_wake_up_local
====================

.. c:function:: void try_to_wake_up_local (struct task_struct *p)

    try to wake up a local task with rq lock held

    :param struct task_struct \*p:
        the thread to be awakened


.. _`try_to_wake_up_local.description`:

Description
-----------

Put ``p`` on the run-queue if it's not already there. The caller must
ensure that :c:func:`this_rq` is locked, ``p`` is bound to :c:func:`this_rq` and not
the current task.


.. _`wake_up_process`:

wake_up_process
===============

.. c:function:: int wake_up_process (struct task_struct *p)

    Wake up a specific process

    :param struct task_struct \*p:
        The process to be woken up.


.. _`wake_up_process.description`:

Description
-----------

Attempt to wake up the nominated process and move it to the set of runnable
processes.

Return: 1 if the process was woken up, 0 if it was already running.

It may be assumed that this function implies a write memory barrier before
changing the task state if and only if any tasks are woken up.


.. _`preempt_notifier_register`:

preempt_notifier_register
=========================

.. c:function:: void preempt_notifier_register (struct preempt_notifier *notifier)

    tell me when current is being preempted & rescheduled

    :param struct preempt_notifier \*notifier:
        notifier struct to register


.. _`preempt_notifier_unregister`:

preempt_notifier_unregister
===========================

.. c:function:: void preempt_notifier_unregister (struct preempt_notifier *notifier)

    no longer interested in preemption notifications

    :param struct preempt_notifier \*notifier:
        notifier struct to unregister


.. _`preempt_notifier_unregister.description`:

Description
-----------

This is \*not\* safe to call from within a preemption notifier.


.. _`prepare_task_switch`:

prepare_task_switch
===================

.. c:function:: void prepare_task_switch (struct rq *rq, struct task_struct *prev, struct task_struct *next)

    prepare to switch tasks

    :param struct rq \*rq:
        the runqueue preparing to switch

    :param struct task_struct \*prev:
        the current task that is being switched out

    :param struct task_struct \*next:
        the task we are going to switch to.


.. _`prepare_task_switch.description`:

Description
-----------

This is called with the rq lock held and interrupts off. It must
be paired with a subsequent finish_task_switch after the context
switch.

prepare_task_switch sets up locking and calls architecture specific
hooks.


.. _`finish_task_switch`:

finish_task_switch
==================

.. c:function:: struct rq *finish_task_switch (struct task_struct *prev)

    clean up after a task-switch

    :param struct task_struct \*prev:
        the thread we just switched away from.


.. _`finish_task_switch.description`:

Description
-----------

finish_task_switch must be called after the context switch, paired
with a prepare_task_switch call before the context switch.
finish_task_switch will reconcile locking set up by prepare_task_switch,
and do any other architecture-specific cleanup actions.

Note that we may have delayed dropping an mm in :c:func:`context_switch`. If
so, we finish that here outside of the runqueue lock. (Doing it
with the lock held can cause deadlocks; see :c:func:`schedule` for
details.)

The context switch have flipped the stack from under us and restored the
local variables which were saved when this task called :c:func:`schedule` in the
past. prev == current is still correct but we need to recalculate this_rq
because prev may have moved to another CPU.


.. _`schedule_tail`:

schedule_tail
=============

.. c:function:: __visible void schedule_tail (struct task_struct *prev)

    first thing a freshly forked thread must call.

    :param struct task_struct \*prev:
        the thread we just switched away from.


.. _`scheduler_tick_max_deferment`:

scheduler_tick_max_deferment
============================

.. c:function:: u64 scheduler_tick_max_deferment ( void)

    :param void:
        no arguments


.. _`scheduler_tick_max_deferment.description`:

Description
-----------


Keep at least one tick per second when a single
active task is running because the scheduler doesn't
yet completely support full dynticks environment.

This makes sure that uptime, CFS vruntime, load
balancing, etc... continue to move forward, even
with a very low granularity.

Return: Maximum deferment in nanoseconds.


.. _`schedule_preempt_disabled`:

schedule_preempt_disabled
=========================

.. c:function:: void __sched schedule_preempt_disabled ( void)

    called with preemption disabled

    :param void:
        no arguments


.. _`schedule_preempt_disabled.description`:

Description
-----------


Returns with preemption disabled. Note: preempt_count must be 1


.. _`preempt_schedule_notrace`:

preempt_schedule_notrace
========================

.. c:function:: __visible void __sched notrace preempt_schedule_notrace ( void)

    preempt_schedule called by tracing

    :param void:
        no arguments


.. _`preempt_schedule_notrace.description`:

Description
-----------


The tracing infrastructure uses preempt_enable_notrace to prevent
recursion and tracing preempt enabling caused by the tracing
infrastructure itself. But as tracing can happen in areas coming
from userspace or just about to enter userspace, a preempt enable
can occur before :c:func:`user_exit` is called. This will cause the scheduler
to be called when the system is still in usermode.

To prevent this, the preempt_enable_notrace will use this function
instead of :c:func:`preempt_schedule` to exit user context if needed before
calling the scheduler.


.. _`task_prio`:

task_prio
=========

.. c:function:: int task_prio (const struct task_struct *p)

    return the priority value of a given task.

    :param const struct task_struct \*p:
        the task in question.


.. _`task_prio.description`:

Description
-----------

Return: The priority value as seen by users in /proc.
RT tasks are offset by -200. Normal tasks are centered
around 0, value goes from -16 to +15.


.. _`idle_cpu`:

idle_cpu
========

.. c:function:: int idle_cpu (int cpu)

    is a given cpu idle currently?

    :param int cpu:
        the processor in question.


.. _`idle_cpu.description`:

Description
-----------

Return: 1 if the CPU is currently idle. 0 otherwise.


.. _`idle_task`:

idle_task
=========

.. c:function:: struct task_struct *idle_task (int cpu)

    return the idle task for a given cpu.

    :param int cpu:
        the processor in question.


.. _`idle_task.description`:

Description
-----------

Return: The idle task for the cpu ``cpu``\ .


.. _`find_process_by_pid`:

find_process_by_pid
===================

.. c:function:: struct task_struct *find_process_by_pid (pid_t pid)

    find a process with a matching PID value.

    :param pid_t pid:
        the pid in question.


.. _`find_process_by_pid.description`:

Description
-----------

The task of ``pid``\ , if found. ``NULL`` otherwise.


.. _`sched_setscheduler`:

sched_setscheduler
==================

.. c:function:: int sched_setscheduler (struct task_struct *p, int policy, const struct sched_param *param)

    change the scheduling policy and/or RT priority of a thread.

    :param struct task_struct \*p:
        the task in question.

    :param int policy:
        new policy.

    :param const struct sched_param \*param:
        structure containing the new RT priority.


.. _`sched_setscheduler.description`:

Description
-----------

Return: 0 on success. An error code otherwise.

NOTE that the task may be already dead.


.. _`sched_setscheduler_nocheck`:

sched_setscheduler_nocheck
==========================

.. c:function:: int sched_setscheduler_nocheck (struct task_struct *p, int policy, const struct sched_param *param)

    change the scheduling policy and/or RT priority of a thread from kernelspace.

    :param struct task_struct \*p:
        the task in question.

    :param int policy:
        new policy.

    :param const struct sched_param \*param:
        structure containing the new RT priority.


.. _`sched_setscheduler_nocheck.description`:

Description
-----------

Just like sched_setscheduler, only don't bother checking if the
current context has permission.  For example, this is needed in
:c:func:`stop_machine`: we create temporary high priority worker threads,
but our caller might not have that capability.

Return: 0 on success. An error code otherwise.


.. _`sys_sched_setscheduler`:

sys_sched_setscheduler
======================

.. c:function:: long sys_sched_setscheduler (pid_t pid, int policy, struct sched_param __user *param)

    set/change the scheduler policy and RT priority

    :param pid_t pid:
        the pid in question.

    :param int policy:
        new policy.

    :param struct sched_param __user \*param:
        structure containing the new RT priority.


.. _`sys_sched_setscheduler.description`:

Description
-----------

Return: 0 on success. An error code otherwise.


.. _`sys_sched_setparam`:

sys_sched_setparam
==================

.. c:function:: long sys_sched_setparam (pid_t pid, struct sched_param __user *param)

    set/change the RT priority of a thread

    :param pid_t pid:
        the pid in question.

    :param struct sched_param __user \*param:
        structure containing the new RT priority.


.. _`sys_sched_setparam.description`:

Description
-----------

Return: 0 on success. An error code otherwise.


.. _`sys_sched_setattr`:

sys_sched_setattr
=================

.. c:function:: long sys_sched_setattr (pid_t pid, struct sched_attr __user *uattr, unsigned int flags)

    same as above, but with extended sched_attr

    :param pid_t pid:
        the pid in question.

    :param struct sched_attr __user \*uattr:
        structure containing the extended parameters.

    :param unsigned int flags:
        for future extension.


.. _`sys_sched_getscheduler`:

sys_sched_getscheduler
======================

.. c:function:: long sys_sched_getscheduler (pid_t pid)

    get the policy (scheduling class) of a thread

    :param pid_t pid:
        the pid in question.


.. _`sys_sched_getscheduler.description`:

Description
-----------

Return: On success, the policy of the thread. Otherwise, a negative error
code.


.. _`sys_sched_getparam`:

sys_sched_getparam
==================

.. c:function:: long sys_sched_getparam (pid_t pid, struct sched_param __user *param)

    get the RT priority of a thread

    :param pid_t pid:
        the pid in question.

    :param struct sched_param __user \*param:
        structure containing the RT priority.


.. _`sys_sched_getparam.description`:

Description
-----------

Return: On success, 0 and the RT priority is in ``param``\ . Otherwise, an error
code.


.. _`sys_sched_getattr`:

sys_sched_getattr
=================

.. c:function:: long sys_sched_getattr (pid_t pid, struct sched_attr __user *uattr, unsigned int size, unsigned int flags)

    similar to sched_getparam, but with sched_attr

    :param pid_t pid:
        the pid in question.

    :param struct sched_attr __user \*uattr:
        structure containing the extended parameters.

    :param unsigned int size:
        sizeof(attr) for fwd/bwd comp.

    :param unsigned int flags:
        for future extension.


.. _`sys_sched_setaffinity`:

sys_sched_setaffinity
=====================

.. c:function:: long sys_sched_setaffinity (pid_t pid, unsigned int len, unsigned long __user *user_mask_ptr)

    set the cpu affinity of a process

    :param pid_t pid:
        pid of the process

    :param unsigned int len:
        length in bytes of the bitmask pointed to by user_mask_ptr

    :param unsigned long __user \*user_mask_ptr:
        user-space pointer to the new cpu mask


.. _`sys_sched_setaffinity.description`:

Description
-----------

Return: 0 on success. An error code otherwise.


.. _`sys_sched_getaffinity`:

sys_sched_getaffinity
=====================

.. c:function:: long sys_sched_getaffinity (pid_t pid, unsigned int len, unsigned long __user *user_mask_ptr)

    get the cpu affinity of a process

    :param pid_t pid:
        pid of the process

    :param unsigned int len:
        length in bytes of the bitmask pointed to by user_mask_ptr

    :param unsigned long __user \*user_mask_ptr:
        user-space pointer to hold the current cpu mask


.. _`sys_sched_getaffinity.description`:

Description
-----------

Return: 0 on success. An error code otherwise.


.. _`sys_sched_yield`:

sys_sched_yield
===============

.. c:function:: long sys_sched_yield ( void)

    yield the current processor to other threads.

    :param void:
        no arguments


.. _`sys_sched_yield.description`:

Description
-----------


This function yields the current CPU to other tasks. If there are no
other threads running on this CPU then this function will return.

Return: 0.


.. _`yield`:

yield
=====

.. c:function:: void __sched yield ( void)

    yield the current processor to other threads.

    :param void:
        no arguments


.. _`yield.description`:

Description
-----------


Do not ever use this function, there's a 99% chance you're doing it wrong.

The scheduler is at all times free to pick the calling task as the most
eligible task to run, if removing the :c:func:`yield` call from your code breaks
it, its already broken.

Typical broken usage is:

while (!event)
:c:func:`yield`;

where one assumes that :c:func:`yield` will let 'the other' process run that will
make event true. If the current task is a SCHED_FIFO task that will never
happen. Never use :c:func:`yield` as a progress guarantee!!

If you want to use :c:func:`yield` to wait for something, use :c:func:`wait_event`.
If you want to use :c:func:`yield` to be 'nice' for others, use :c:func:`cond_resched`.
If you still want to use :c:func:`yield`, do not!


.. _`yield_to`:

yield_to
========

.. c:function:: int __sched yield_to (struct task_struct *p, bool preempt)

    yield the current processor to another thread in your thread group, or accelerate that thread toward the processor it's on.

    :param struct task_struct \*p:
        target task

    :param bool preempt:
        whether task preemption is allowed or not


.. _`yield_to.description`:

Description
-----------

It's the caller's job to ensure that the target task struct
can't go away on us before we can do any checks.

Return::

        true (>0) if we indeed boosted the target task.
        false (0) if we failed to boost the target.
        -ESRCH if there's no task to yield to.


.. _`sys_sched_get_priority_max`:

sys_sched_get_priority_max
==========================

.. c:function:: long sys_sched_get_priority_max (int policy)

    return maximum RT priority.

    :param int policy:
        scheduling class.


.. _`sys_sched_get_priority_max.description`:

Description
-----------

Return: On success, this syscall returns the maximum
rt_priority that can be used by a given scheduling class.
On failure, a negative error code is returned.


.. _`sys_sched_get_priority_min`:

sys_sched_get_priority_min
==========================

.. c:function:: long sys_sched_get_priority_min (int policy)

    return minimum RT priority.

    :param int policy:
        scheduling class.


.. _`sys_sched_get_priority_min.description`:

Description
-----------

Return: On success, this syscall returns the minimum
rt_priority that can be used by a given scheduling class.
On failure, a negative error code is returned.


.. _`sys_sched_rr_get_interval`:

sys_sched_rr_get_interval
=========================

.. c:function:: long sys_sched_rr_get_interval (pid_t pid, struct timespec __user *interval)

    return the default timeslice of a process.

    :param pid_t pid:
        pid of the process.

    :param struct timespec __user \*interval:
        userspace pointer to the timeslice value.


.. _`sys_sched_rr_get_interval.description`:

Description
-----------

this syscall writes the default timeslice value of a given process
into the user-space timespec buffer. A value of '0' means infinity.

Return: On success, 0 and the timeslice is in ``interval``\ . Otherwise,
an error code.


.. _`init_idle`:

init_idle
=========

.. c:function:: void init_idle (struct task_struct *idle, int cpu)

    set up an idle thread for a given CPU

    :param struct task_struct \*idle:
        task in question

    :param int cpu:
        cpu the idle task belongs to


.. _`init_idle.description`:

Description
-----------

NOTE: this function does not set the idle thread's NEED_RESCHED
flag, to make booting more robust.


.. _`curr_task`:

curr_task
=========

.. c:function:: struct task_struct *curr_task (int cpu)

    return the current task for a given cpu.

    :param int cpu:
        the processor in question.


.. _`curr_task.description`:

Description
-----------

ONLY VALID WHEN THE WHOLE SYSTEM IS STOPPED!

Return: The current task for ``cpu``\ .


.. _`set_curr_task`:

set_curr_task
=============

.. c:function:: void set_curr_task (int cpu, struct task_struct *p)

    set the current task for a given cpu.

    :param int cpu:
        the processor in question.

    :param struct task_struct \*p:
        the task pointer to set.


.. _`set_curr_task.description`:

Description
-----------

Description: This function must only be used when non-maskable interrupts
are serviced on a separate stack. It allows the architecture to switch the
notion of the current task on a cpu in a non-blocking manner. This function
must be called with all CPU's synchronized, and interrupts disabled, the
and caller must save the original value of the current task (see
:c:func:`curr_task` above) and restore that value before reenabling interrupts and
re-starting the system.

ONLY VALID WHEN THE WHOLE SYSTEM IS STOPPED!

