.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/signal.c

.. _`task_set_jobctl_pending`:

task_set_jobctl_pending
=======================

.. c:function:: bool task_set_jobctl_pending(struct task_struct *task, unsigned long mask)

    set jobctl pending bits

    :param task:
        target task
    :type task: struct task_struct \*

    :param mask:
        pending bits to set
    :type mask: unsigned long

.. _`task_set_jobctl_pending.description`:

Description
-----------

Clear \ ``mask``\  from \ ``task->jobctl``\ .  \ ``mask``\  must be subset of
\ ``JOBCTL_PENDING_MASK``\  | \ ``JOBCTL_STOP_CONSUME``\  | \ ``JOBCTL_STOP_SIGMASK``\  |
\ ``JOBCTL_TRAPPING``\ .  If stop signo is being set, the existing signo is
cleared.  If \ ``task``\  is already being killed or exiting, this function
becomes noop.

.. _`task_set_jobctl_pending.context`:

Context
-------

Must be called with \ ``task->sighand->siglock``\  held.

.. _`task_set_jobctl_pending.return`:

Return
------

\ ``true``\  if \ ``mask``\  is set, \ ``false``\  if made noop because \ ``task``\  was dying.

.. _`task_clear_jobctl_trapping`:

task_clear_jobctl_trapping
==========================

.. c:function:: void task_clear_jobctl_trapping(struct task_struct *task)

    clear jobctl trapping bit

    :param task:
        target task
    :type task: struct task_struct \*

.. _`task_clear_jobctl_trapping.description`:

Description
-----------

If JOBCTL_TRAPPING is set, a ptracer is waiting for us to enter TRACED.
Clear it and wake up the ptracer.  Note that we don't need any further
locking.  \ ``task->siglock``\  guarantees that \ ``task->parent``\  points to the
ptracer.

.. _`task_clear_jobctl_trapping.context`:

Context
-------

Must be called with \ ``task->sighand->siglock``\  held.

.. _`task_clear_jobctl_pending`:

task_clear_jobctl_pending
=========================

.. c:function:: void task_clear_jobctl_pending(struct task_struct *task, unsigned long mask)

    clear jobctl pending bits

    :param task:
        target task
    :type task: struct task_struct \*

    :param mask:
        pending bits to clear
    :type mask: unsigned long

.. _`task_clear_jobctl_pending.description`:

Description
-----------

Clear \ ``mask``\  from \ ``task->jobctl``\ .  \ ``mask``\  must be subset of
\ ``JOBCTL_PENDING_MASK``\ .  If \ ``JOBCTL_STOP_PENDING``\  is being cleared, other
STOP bits are cleared together.

If clearing of \ ``mask``\  leaves no stop or trap pending, this function calls
\ :c:func:`task_clear_jobctl_trapping`\ .

.. _`task_clear_jobctl_pending.context`:

Context
-------

Must be called with \ ``task->sighand->siglock``\  held.

.. _`task_participate_group_stop`:

task_participate_group_stop
===========================

.. c:function:: bool task_participate_group_stop(struct task_struct *task)

    participate in a group stop

    :param task:
        task participating in a group stop
    :type task: struct task_struct \*

.. _`task_participate_group_stop.description`:

Description
-----------

\ ``task``\  has \ ``JOBCTL_STOP_PENDING``\  set and is participating in a group stop.
Group stop states are cleared and the group stop count is consumed if
\ ``JOBCTL_STOP_CONSUME``\  was set.  If the consumption completes the group
stop, the appropriate \ ``SIGNAL_``\ * flags are set.

.. _`task_participate_group_stop.context`:

Context
-------

Must be called with \ ``task->sighand->siglock``\  held.

.. _`task_participate_group_stop.return`:

Return
------

\ ``true``\  if group stop completion should be notified to the parent, \ ``false``\ 
otherwise.

.. _`ptrace_trap_notify`:

ptrace_trap_notify
==================

.. c:function:: void ptrace_trap_notify(struct task_struct *t)

    schedule trap to notify ptracer

    :param t:
        tracee wanting to notify tracer
    :type t: struct task_struct \*

.. _`ptrace_trap_notify.description`:

Description
-----------

This function schedules sticky ptrace trap which is cleared on the next
TRAP_STOP to notify ptracer of an event.  \ ``t``\  must have been seized by
ptracer.

If \ ``t``\  is running, STOP trap will be taken.  If trapped for STOP and
ptracer is listening for events, tracee is woken up so that it can
re-trap for the new event.  If trapped otherwise, STOP trap will be
eventually taken without returning to userland after the existing traps
are finished by PTRACE_CONT.

.. _`ptrace_trap_notify.context`:

Context
-------

Must be called with \ ``task->sighand->siglock``\  held.

.. _`do_notify_parent_cldstop`:

do_notify_parent_cldstop
========================

.. c:function:: void do_notify_parent_cldstop(struct task_struct *tsk, bool for_ptracer, int why)

    notify parent of stopped/continued state change

    :param tsk:
        task reporting the state change
    :type tsk: struct task_struct \*

    :param for_ptracer:
        the notification is for ptracer
    :type for_ptracer: bool

    :param why:
        CLD_{CONTINUED|STOPPED|TRAPPED} to report
    :type why: int

.. _`do_notify_parent_cldstop.description`:

Description
-----------

Notify \ ``tsk``\ 's parent that the stopped/continued state has changed.  If
\ ``for_ptracer``\  is \ ``false``\ , \ ``tsk``\ 's group leader notifies to its real parent.
If \ ``true``\ , \ ``tsk``\  reports to \ ``tsk->parent``\  which should be the ptracer.

.. _`do_notify_parent_cldstop.context`:

Context
-------

Must be called with tasklist_lock at least read locked.

.. _`do_signal_stop`:

do_signal_stop
==============

.. c:function:: bool do_signal_stop(int signr)

    handle group stop for SIGSTOP and other stop signals

    :param signr:
        signr causing group stop if initiating
    :type signr: int

.. _`do_signal_stop.description`:

Description
-----------

If \ ``JOBCTL_STOP_PENDING``\  is not set yet, initiate group stop with \ ``signr``\ 
and participate in it.  If already set, participate in the existing
group stop.  If participated in a group stop (and thus slept), \ ``true``\  is
returned with siglock released.

If ptraced, this function doesn't handle stop itself.  Instead,
\ ``JOBCTL_TRAP_STOP``\  is scheduled and \ ``false``\  is returned with siglock
untouched.  The caller must ensure that INTERRUPT trap handling takes
places afterwards.

.. _`do_signal_stop.context`:

Context
-------

Must be called with \ ``current->sighand->siglock``\  held, which is released
on \ ``true``\  return.

.. _`do_signal_stop.return`:

Return
------

\ ``false``\  if group stop is already cancelled or ptrace trap is scheduled.
\ ``true``\  if participated in group stop.

.. _`do_jobctl_trap`:

do_jobctl_trap
==============

.. c:function:: void do_jobctl_trap( void)

    take care of ptrace jobctl traps

    :param void:
        no arguments
    :type void: 

.. _`do_jobctl_trap.description`:

Description
-----------

When PT_SEIZED, it's used for both group stop and explicit
SEIZE/INTERRUPT traps.  Both generate PTRACE_EVENT_STOP trap with
accompanying siginfo.  If stopped, lower eight bits of exit_code contain
the stop signal; otherwise, \ ``SIGTRAP``\ .

When !PT_SEIZED, it's used only for group stop trap with stop signal
number as exit_code and no siginfo.

.. _`do_jobctl_trap.context`:

Context
-------

Must be called with \ ``current->sighand->siglock``\  held, which may be
released and re-acquired before returning with intervening sleep.

.. _`signal_delivered`:

signal_delivered
================

.. c:function:: void signal_delivered(struct ksignal *ksig, int stepping)

    :param ksig:
        kernel signal struct
    :type ksig: struct ksignal \*

    :param stepping:
        nonzero if debugger single-step or block-step in use
    :type stepping: int

.. _`signal_delivered.description`:

Description
-----------

This function should be called when a signal has successfully been
delivered. It updates the blocked signals accordingly (@ksig->ka.sa.sa_mask
is always blocked, and the signal itself is blocked unless \ ``SA_NODEFER``\ 
is set in \ ``ksig->ka.sa.sa_flags``\ .  Tracing is notified.

.. _`sys_restart_syscall`:

sys_restart_syscall
===================

.. c:function:: long sys_restart_syscall( void)

    restart a system call

    :param void:
        no arguments
    :type void: 

.. _`set_current_blocked`:

set_current_blocked
===================

.. c:function:: void set_current_blocked(sigset_t *newset)

    change current->blocked mask

    :param newset:
        new mask
    :type newset: sigset_t \*

.. _`set_current_blocked.description`:

Description
-----------

It is wrong to change ->blocked directly, this helper should be used
to ensure the process can't miss a shared signal we are going to block.

.. _`sys_rt_sigprocmask`:

sys_rt_sigprocmask
==================

.. c:function:: long sys_rt_sigprocmask(int how, sigset_t __user *nset, sigset_t __user *oset, size_t sigsetsize)

    change the list of currently blocked signals

    :param how:
        whether to add, remove, or set signals
    :type how: int

    :param nset:
        stores pending signals
    :type nset: sigset_t __user \*

    :param oset:
        previous value of signal mask if non-null
    :type oset: sigset_t __user \*

    :param sigsetsize:
        size of sigset_t type
    :type sigsetsize: size_t

.. _`sys_rt_sigpending`:

sys_rt_sigpending
=================

.. c:function:: long sys_rt_sigpending(sigset_t __user *uset, size_t sigsetsize)

    examine a pending signal that has been raised while blocked

    :param uset:
        stores pending signals
    :type uset: sigset_t __user \*

    :param sigsetsize:
        size of sigset_t type or larger
    :type sigsetsize: size_t

.. _`do_sigtimedwait`:

do_sigtimedwait
===============

.. c:function:: int do_sigtimedwait(const sigset_t *which, kernel_siginfo_t *info, const struct timespec64 *ts)

    wait for queued signals specified in \ ``which``\ 

    :param which:
        queued signals to wait for
    :type which: const sigset_t \*

    :param info:
        if non-null, the signal's siginfo is returned here
    :type info: kernel_siginfo_t \*

    :param ts:
        upper bound on process time suspension
    :type ts: const struct timespec64 \*

.. _`sys_rt_sigtimedwait`:

sys_rt_sigtimedwait
===================

.. c:function:: long sys_rt_sigtimedwait(const sigset_t __user *uthese, siginfo_t __user *uinfo, const struct __kernel_timespec __user *uts, size_t sigsetsize)

    synchronously wait for queued signals specified in \ ``uthese``\ 

    :param uthese:
        queued signals to wait for
    :type uthese: const sigset_t __user \*

    :param uinfo:
        if non-null, the signal's siginfo is returned here
    :type uinfo: siginfo_t __user \*

    :param uts:
        upper bound on process time suspension
    :type uts: const struct __kernel_timespec __user \*

    :param sigsetsize:
        size of sigset_t type
    :type sigsetsize: size_t

.. _`sys_kill`:

sys_kill
========

.. c:function:: long sys_kill(pid_t pid, int sig)

    send a signal to a process

    :param pid:
        the PID of the process
    :type pid: pid_t

    :param sig:
        signal to be sent
    :type sig: int

.. _`sys_tgkill`:

sys_tgkill
==========

.. c:function:: long sys_tgkill(pid_t tgid, pid_t pid, int sig)

    send signal to one specific thread

    :param tgid:
        the thread group ID of the thread
    :type tgid: pid_t

    :param pid:
        the PID of the thread
    :type pid: pid_t

    :param sig:
        signal to be sent
    :type sig: int

.. _`sys_tgkill.description`:

Description
-----------

 This syscall also checks the \ ``tgid``\  and returns -ESRCH even if the PID
 exists but it's not belonging to the target process anymore. This
 method solves the problem of threads exiting and PIDs getting reused.

.. _`sys_tkill`:

sys_tkill
=========

.. c:function:: long sys_tkill(pid_t pid, int sig)

    send signal to one specific task

    :param pid:
        the PID of the task
    :type pid: pid_t

    :param sig:
        signal to be sent
    :type sig: int

.. _`sys_tkill.description`:

Description
-----------

 Send a signal to only one task, even if it's a CLONE_THREAD task.

.. _`sys_rt_sigqueueinfo`:

sys_rt_sigqueueinfo
===================

.. c:function:: long sys_rt_sigqueueinfo(pid_t pid, int sig, siginfo_t __user *uinfo)

    send signal information to a signal

    :param pid:
        the PID of the thread
    :type pid: pid_t

    :param sig:
        signal to be sent
    :type sig: int

    :param uinfo:
        signal info to be sent
    :type uinfo: siginfo_t __user \*

.. _`sys_sigpending`:

sys_sigpending
==============

.. c:function:: long sys_sigpending(old_sigset_t __user *uset)

    examine pending signals

    :param uset:
        where mask of pending signal is returned
    :type uset: old_sigset_t __user \*

.. _`sys_sigprocmask`:

sys_sigprocmask
===============

.. c:function:: long sys_sigprocmask(int how, old_sigset_t __user *nset, old_sigset_t __user *oset)

    examine and change blocked signals

    :param how:
        whether to add, remove, or set signals
    :type how: int

    :param nset:
        signals to add or remove (if non-null)
    :type nset: old_sigset_t __user \*

    :param oset:
        previous value of signal mask if non-null
    :type oset: old_sigset_t __user \*

.. _`sys_sigprocmask.description`:

Description
-----------

Some platforms have their own version with special arguments;
others support only sys_rt_sigprocmask.

.. _`sys_rt_sigaction`:

sys_rt_sigaction
================

.. c:function:: long sys_rt_sigaction(int sig, const struct sigaction __user *act, struct sigaction __user *oact, size_t sigsetsize)

    alter an action taken by a process

    :param sig:
        signal to be sent
    :type sig: int

    :param act:
        new sigaction
    :type act: const struct sigaction __user \*

    :param oact:
        used to save the previous sigaction
    :type oact: struct sigaction __user \*

    :param sigsetsize:
        size of sigset_t type
    :type sigsetsize: size_t

.. _`sys_rt_sigsuspend`:

sys_rt_sigsuspend
=================

.. c:function:: long sys_rt_sigsuspend(sigset_t __user *unewset, size_t sigsetsize)

    replace the signal mask for a value with the \ ``unewset``\  value until a signal is received

    :param unewset:
        new signal mask value
    :type unewset: sigset_t __user \*

    :param sigsetsize:
        size of sigset_t type
    :type sigsetsize: size_t

.. This file was automatic generated / don't edit.

