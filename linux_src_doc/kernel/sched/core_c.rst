.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/sched/core.c

.. _`task_curr`:

task_curr
=========

.. c:function:: int task_curr(const struct task_struct *p)

    is this task currently executing on a CPU?

    :param p:
        the task in question.
    :type p: const struct task_struct \*

.. _`task_curr.return`:

Return
------

1 if the task is currently executing. 0 otherwise.

.. _`try_to_wake_up`:

try_to_wake_up
==============

.. c:function:: int try_to_wake_up(struct task_struct *p, unsigned int state, int wake_flags)

    wake up a thread

    :param p:
        the thread to be awakened
    :type p: struct task_struct \*

    :param state:
        the mask of task states that can be woken
    :type state: unsigned int

    :param wake_flags:
        wake modifier flags (WF_*)
    :type wake_flags: int

.. _`try_to_wake_up.description`:

Description
-----------

If (@state & \ ``p->state``\ ) \ ``p->state``\  = TASK_RUNNING.

If the task was not queued/runnable, also place it back on a runqueue.

Atomic against \ :c:func:`schedule`\  which would dequeue a task, also see
\ :c:func:`set_current_state`\ .

This function executes a full memory barrier before accessing the task
state; see \ :c:func:`set_current_state`\ .

.. _`try_to_wake_up.return`:

Return
------

\ ``true``\  if \ ``p->state``\  changes (an actual wakeup was done),
        \ ``false``\  otherwise.

.. _`try_to_wake_up_local`:

try_to_wake_up_local
====================

.. c:function:: void try_to_wake_up_local(struct task_struct *p, struct rq_flags *rf)

    try to wake up a local task with rq lock held

    :param p:
        the thread to be awakened
    :type p: struct task_struct \*

    :param rf:
        request-queue flags for pinning
    :type rf: struct rq_flags \*

.. _`try_to_wake_up_local.description`:

Description
-----------

Put \ ``p``\  on the run-queue if it's not already there. The caller must
ensure that \ :c:func:`this_rq`\  is locked, \ ``p``\  is bound to \ :c:func:`this_rq`\  and not
the current task.

.. _`wake_up_process`:

wake_up_process
===============

.. c:function:: int wake_up_process(struct task_struct *p)

    Wake up a specific process

    :param p:
        The process to be woken up.
    :type p: struct task_struct \*

.. _`wake_up_process.description`:

Description
-----------

Attempt to wake up the nominated process and move it to the set of runnable
processes.

.. _`wake_up_process.return`:

Return
------

1 if the process was woken up, 0 if it was already running.

This function executes a full memory barrier before accessing the task state.

.. _`preempt_notifier_register`:

preempt_notifier_register
=========================

.. c:function:: void preempt_notifier_register(struct preempt_notifier *notifier)

    tell me when current is being preempted & rescheduled

    :param notifier:
        notifier struct to register
    :type notifier: struct preempt_notifier \*

.. _`preempt_notifier_unregister`:

preempt_notifier_unregister
===========================

.. c:function:: void preempt_notifier_unregister(struct preempt_notifier *notifier)

    no longer interested in preemption notifications

    :param notifier:
        notifier struct to unregister
    :type notifier: struct preempt_notifier \*

.. _`preempt_notifier_unregister.description`:

Description
-----------

This is *not* safe to call from within a preemption notifier.

.. _`prepare_task_switch`:

prepare_task_switch
===================

.. c:function:: void prepare_task_switch(struct rq *rq, struct task_struct *prev, struct task_struct *next)

    prepare to switch tasks

    :param rq:
        the runqueue preparing to switch
    :type rq: struct rq \*

    :param prev:
        the current task that is being switched out
    :type prev: struct task_struct \*

    :param next:
        the task we are going to switch to.
    :type next: struct task_struct \*

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

.. c:function:: struct rq *finish_task_switch(struct task_struct *prev)

    clean up after a task-switch

    :param prev:
        the thread we just switched away from.
    :type prev: struct task_struct \*

.. _`finish_task_switch.description`:

Description
-----------

finish_task_switch must be called after the context switch, paired
with a prepare_task_switch call before the context switch.
finish_task_switch will reconcile locking set up by prepare_task_switch,
and do any other architecture-specific cleanup actions.

Note that we may have delayed dropping an mm in \ :c:func:`context_switch`\ . If
so, we finish that here outside of the runqueue lock. (Doing it
with the lock held can cause deadlocks; see \ :c:func:`schedule`\  for
details.)

The context switch have flipped the stack from under us and restored the
local variables which were saved when this task called \ :c:func:`schedule`\  in the
past. prev == current is still correct but we need to recalculate this_rq
because prev may have moved to another CPU.

.. _`schedule_tail`:

schedule_tail
=============

.. c:function:: __visible void schedule_tail(struct task_struct *prev)

    first thing a freshly forked thread must call.

    :param prev:
        the thread we just switched away from.
    :type prev: struct task_struct \*

.. _`schedule_preempt_disabled`:

schedule_preempt_disabled
=========================

.. c:function:: void __sched schedule_preempt_disabled( void)

    called with preemption disabled

    :param void:
        no arguments
    :type void: 

.. _`schedule_preempt_disabled.description`:

Description
-----------

Returns with preemption disabled. Note: preempt_count must be 1

.. _`preempt_schedule_notrace`:

preempt_schedule_notrace
========================

.. c:function:: __visible void __sched notrace preempt_schedule_notrace( void)

    preempt_schedule called by tracing

    :param void:
        no arguments
    :type void: 

.. _`preempt_schedule_notrace.description`:

Description
-----------

The tracing infrastructure uses preempt_enable_notrace to prevent
recursion and tracing preempt enabling caused by the tracing
infrastructure itself. But as tracing can happen in areas coming
from userspace or just about to enter userspace, a preempt enable
can occur before \ :c:func:`user_exit`\  is called. This will cause the scheduler
to be called when the system is still in usermode.

To prevent this, the preempt_enable_notrace will use this function
instead of \ :c:func:`preempt_schedule`\  to exit user context if needed before
calling the scheduler.

.. _`task_prio`:

task_prio
=========

.. c:function:: int task_prio(const struct task_struct *p)

    return the priority value of a given task.

    :param p:
        the task in question.
    :type p: const struct task_struct \*

.. _`task_prio.return`:

Return
------

The priority value as seen by users in /proc.
RT tasks are offset by -200. Normal tasks are centered
around 0, value goes from -16 to +15.

.. _`idle_cpu`:

idle_cpu
========

.. c:function:: int idle_cpu(int cpu)

    is a given CPU idle currently?

    :param cpu:
        the processor in question.
    :type cpu: int

.. _`idle_cpu.return`:

Return
------

1 if the CPU is currently idle. 0 otherwise.

.. _`available_idle_cpu`:

available_idle_cpu
==================

.. c:function:: int available_idle_cpu(int cpu)

    is a given CPU idle for enqueuing work.

    :param cpu:
        the CPU in question.
    :type cpu: int

.. _`available_idle_cpu.return`:

Return
------

1 if the CPU is currently idle. 0 otherwise.

.. _`idle_task`:

idle_task
=========

.. c:function:: struct task_struct *idle_task(int cpu)

    return the idle task for a given CPU.

    :param cpu:
        the processor in question.
    :type cpu: int

.. _`idle_task.return`:

Return
------

The idle task for the CPU \ ``cpu``\ .

.. _`find_process_by_pid`:

find_process_by_pid
===================

.. c:function:: struct task_struct *find_process_by_pid(pid_t pid)

    find a process with a matching PID value.

    :param pid:
        the pid in question.
    :type pid: pid_t

.. _`find_process_by_pid.description`:

Description
-----------

The task of \ ``pid``\ , if found. \ ``NULL``\  otherwise.

.. _`sched_setscheduler`:

sched_setscheduler
==================

.. c:function:: int sched_setscheduler(struct task_struct *p, int policy, const struct sched_param *param)

    change the scheduling policy and/or RT priority of a thread.

    :param p:
        the task in question.
    :type p: struct task_struct \*

    :param policy:
        new policy.
    :type policy: int

    :param param:
        structure containing the new RT priority.
    :type param: const struct sched_param \*

.. _`sched_setscheduler.return`:

Return
------

0 on success. An error code otherwise.

NOTE that the task may be already dead.

.. _`sched_setscheduler_nocheck`:

sched_setscheduler_nocheck
==========================

.. c:function:: int sched_setscheduler_nocheck(struct task_struct *p, int policy, const struct sched_param *param)

    change the scheduling policy and/or RT priority of a thread from kernelspace.

    :param p:
        the task in question.
    :type p: struct task_struct \*

    :param policy:
        new policy.
    :type policy: int

    :param param:
        structure containing the new RT priority.
    :type param: const struct sched_param \*

.. _`sched_setscheduler_nocheck.description`:

Description
-----------

Just like sched_setscheduler, only don't bother checking if the
current context has permission.  For example, this is needed in
\ :c:func:`stop_machine`\ : we create temporary high priority worker threads,
but our caller might not have that capability.

.. _`sched_setscheduler_nocheck.return`:

Return
------

0 on success. An error code otherwise.

.. _`sys_sched_setscheduler`:

sys_sched_setscheduler
======================

.. c:function:: long sys_sched_setscheduler(pid_t pid, int policy, struct sched_param __user *param)

    set/change the scheduler policy and RT priority

    :param pid:
        the pid in question.
    :type pid: pid_t

    :param policy:
        new policy.
    :type policy: int

    :param param:
        structure containing the new RT priority.
    :type param: struct sched_param __user \*

.. _`sys_sched_setscheduler.return`:

Return
------

0 on success. An error code otherwise.

.. _`sys_sched_setparam`:

sys_sched_setparam
==================

.. c:function:: long sys_sched_setparam(pid_t pid, struct sched_param __user *param)

    set/change the RT priority of a thread

    :param pid:
        the pid in question.
    :type pid: pid_t

    :param param:
        structure containing the new RT priority.
    :type param: struct sched_param __user \*

.. _`sys_sched_setparam.return`:

Return
------

0 on success. An error code otherwise.

.. _`sys_sched_setattr`:

sys_sched_setattr
=================

.. c:function:: long sys_sched_setattr(pid_t pid, struct sched_attr __user *uattr, unsigned int flags)

    same as above, but with extended sched_attr

    :param pid:
        the pid in question.
    :type pid: pid_t

    :param uattr:
        structure containing the extended parameters.
    :type uattr: struct sched_attr __user \*

    :param flags:
        for future extension.
    :type flags: unsigned int

.. _`sys_sched_getscheduler`:

sys_sched_getscheduler
======================

.. c:function:: long sys_sched_getscheduler(pid_t pid)

    get the policy (scheduling class) of a thread

    :param pid:
        the pid in question.
    :type pid: pid_t

.. _`sys_sched_getscheduler.return`:

Return
------

On success, the policy of the thread. Otherwise, a negative error
code.

.. _`sys_sched_getparam`:

sys_sched_getparam
==================

.. c:function:: long sys_sched_getparam(pid_t pid, struct sched_param __user *param)

    get the RT priority of a thread

    :param pid:
        the pid in question.
    :type pid: pid_t

    :param param:
        structure containing the RT priority.
    :type param: struct sched_param __user \*

.. _`sys_sched_getparam.return`:

Return
------

On success, 0 and the RT priority is in \ ``param``\ . Otherwise, an error
code.

.. _`sys_sched_getattr`:

sys_sched_getattr
=================

.. c:function:: long sys_sched_getattr(pid_t pid, struct sched_attr __user *uattr, unsigned int size, unsigned int flags)

    similar to sched_getparam, but with sched_attr

    :param pid:
        the pid in question.
    :type pid: pid_t

    :param uattr:
        structure containing the extended parameters.
    :type uattr: struct sched_attr __user \*

    :param size:
        sizeof(attr) for fwd/bwd comp.
    :type size: unsigned int

    :param flags:
        for future extension.
    :type flags: unsigned int

.. _`sys_sched_setaffinity`:

sys_sched_setaffinity
=====================

.. c:function:: long sys_sched_setaffinity(pid_t pid, unsigned int len, unsigned long __user *user_mask_ptr)

    set the CPU affinity of a process

    :param pid:
        pid of the process
    :type pid: pid_t

    :param len:
        length in bytes of the bitmask pointed to by user_mask_ptr
    :type len: unsigned int

    :param user_mask_ptr:
        user-space pointer to the new CPU mask
    :type user_mask_ptr: unsigned long __user \*

.. _`sys_sched_setaffinity.return`:

Return
------

0 on success. An error code otherwise.

.. _`sys_sched_getaffinity`:

sys_sched_getaffinity
=====================

.. c:function:: long sys_sched_getaffinity(pid_t pid, unsigned int len, unsigned long __user *user_mask_ptr)

    get the CPU affinity of a process

    :param pid:
        pid of the process
    :type pid: pid_t

    :param len:
        length in bytes of the bitmask pointed to by user_mask_ptr
    :type len: unsigned int

    :param user_mask_ptr:
        user-space pointer to hold the current CPU mask
    :type user_mask_ptr: unsigned long __user \*

.. _`sys_sched_getaffinity.return`:

Return
------

size of CPU mask copied to user_mask_ptr on success. An
error code otherwise.

.. _`do_sched_yield`:

do_sched_yield
==============

.. c:function:: void do_sched_yield( void)

    yield the current processor to other threads.

    :param void:
        no arguments
    :type void: 

.. _`do_sched_yield.description`:

Description
-----------

This function yields the current CPU to other tasks. If there are no
other threads running on this CPU then this function will return.

.. _`do_sched_yield.return`:

Return
------

0.

.. _`yield`:

yield
=====

.. c:function:: void __sched yield( void)

    yield the current processor to other threads.

    :param void:
        no arguments
    :type void: 

.. _`yield.description`:

Description
-----------

Do not ever use this function, there's a 99% chance you're doing it wrong.

The scheduler is at all times free to pick the calling task as the most
eligible task to run, if removing the \ :c:func:`yield`\  call from your code breaks
it, its already broken.

.. _`yield.typical-broken-usage-is`:

Typical broken usage is
-----------------------


while (!event)
     \ :c:func:`yield`\ ;

where one assumes that \ :c:func:`yield`\  will let 'the other' process run that will
make event true. If the current task is a SCHED_FIFO task that will never
happen. Never use \ :c:func:`yield`\  as a progress guarantee!!

If you want to use \ :c:func:`yield`\  to wait for something, use \ :c:func:`wait_event`\ .
If you want to use \ :c:func:`yield`\  to be 'nice' for others, use \ :c:func:`cond_resched`\ .
If you still want to use \ :c:func:`yield`\ , do not!

.. _`yield_to`:

yield_to
========

.. c:function:: int __sched yield_to(struct task_struct *p, bool preempt)

    yield the current processor to another thread in your thread group, or accelerate that thread toward the processor it's on.

    :param p:
        target task
    :type p: struct task_struct \*

    :param preempt:
        whether task preemption is allowed or not
    :type preempt: bool

.. _`yield_to.description`:

Description
-----------

It's the caller's job to ensure that the target task struct
can't go away on us before we can do any checks.

.. _`yield_to.return`:

Return
------

     true (>0) if we indeed boosted the target task.
     false (0) if we failed to boost the target.
     -ESRCH if there's no task to yield to.

.. _`sys_sched_get_priority_max`:

sys_sched_get_priority_max
==========================

.. c:function:: long sys_sched_get_priority_max(int policy)

    return maximum RT priority.

    :param policy:
        scheduling class.
    :type policy: int

.. _`sys_sched_get_priority_max.return`:

Return
------

On success, this syscall returns the maximum
rt_priority that can be used by a given scheduling class.
On failure, a negative error code is returned.

.. _`sys_sched_get_priority_min`:

sys_sched_get_priority_min
==========================

.. c:function:: long sys_sched_get_priority_min(int policy)

    return minimum RT priority.

    :param policy:
        scheduling class.
    :type policy: int

.. _`sys_sched_get_priority_min.return`:

Return
------

On success, this syscall returns the minimum
rt_priority that can be used by a given scheduling class.
On failure, a negative error code is returned.

.. _`sys_sched_rr_get_interval`:

sys_sched_rr_get_interval
=========================

.. c:function:: long sys_sched_rr_get_interval(pid_t pid, struct __kernel_timespec __user *interval)

    return the default timeslice of a process.

    :param pid:
        pid of the process.
    :type pid: pid_t

    :param interval:
        userspace pointer to the timeslice value.
    :type interval: struct __kernel_timespec __user \*

.. _`sys_sched_rr_get_interval.description`:

Description
-----------

this syscall writes the default timeslice value of a given process
into the user-space timespec buffer. A value of '0' means infinity.

.. _`sys_sched_rr_get_interval.return`:

Return
------

On success, 0 and the timeslice is in \ ``interval``\ . Otherwise,
an error code.

.. _`init_idle`:

init_idle
=========

.. c:function:: void init_idle(struct task_struct *idle, int cpu)

    set up an idle thread for a given CPU

    :param idle:
        task in question
    :type idle: struct task_struct \*

    :param cpu:
        CPU the idle task belongs to
    :type cpu: int

.. _`init_idle.note`:

NOTE
----

this function does not set the idle thread's NEED_RESCHED
flag, to make booting more robust.

.. _`curr_task`:

curr_task
=========

.. c:function:: struct task_struct *curr_task(int cpu)

    return the current task for a given CPU.

    :param cpu:
        the processor in question.
    :type cpu: int

.. _`curr_task.description`:

Description
-----------

ONLY VALID WHEN THE WHOLE SYSTEM IS STOPPED!

.. _`curr_task.return`:

Return
------

The current task for \ ``cpu``\ .

.. _`ia64_set_curr_task`:

ia64_set_curr_task
==================

.. c:function:: void ia64_set_curr_task(int cpu, struct task_struct *p)

    set the current task for a given CPU.

    :param cpu:
        the processor in question.
    :type cpu: int

    :param p:
        the task pointer to set.
    :type p: struct task_struct \*

.. _`ia64_set_curr_task.description`:

Description
-----------

This function must only be used when non-maskable interrupts
are serviced on a separate stack. It allows the architecture to switch the
notion of the current task on a CPU in a non-blocking manner. This function
must be called with all CPU's synchronized, and interrupts disabled, the
and caller must save the original value of the current task (see
\ :c:func:`curr_task`\  above) and restore that value before reenabling interrupts and
re-starting the system.

ONLY VALID WHEN THE WHOLE SYSTEM IS STOPPED!

.. This file was automatic generated / don't edit.

