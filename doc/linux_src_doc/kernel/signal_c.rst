.. -*- coding: utf-8; mode: rst -*-

========
signal.c
========

.. _`task_set_jobctl_pending`:

task_set_jobctl_pending
=======================

.. c:function:: bool task_set_jobctl_pending (struct task_struct *task, unsigned long mask)

    set jobctl pending bits

    :param struct task_struct \*task:
        target task

    :param unsigned long mask:
        pending bits to set


.. _`task_set_jobctl_pending.description`:

Description
-----------

Clear ``mask`` from ``task``\ ->jobctl.  ``mask`` must be subset of
``JOBCTL_PENDING_MASK`` | ``JOBCTL_STOP_CONSUME`` | ``JOBCTL_STOP_SIGMASK`` |
``JOBCTL_TRAPPING``\ .  If stop signo is being set, the existing signo is
cleared.  If ``task`` is already being killed or exiting, this function
becomes noop.

CONTEXT:
Must be called with ``task``\ ->sighand->siglock held.

RETURNS:
``true`` if ``mask`` is set, ``false`` if made noop because ``task`` was dying.


.. _`task_clear_jobctl_trapping`:

task_clear_jobctl_trapping
==========================

.. c:function:: void task_clear_jobctl_trapping (struct task_struct *task)

    clear jobctl trapping bit

    :param struct task_struct \*task:
        target task


.. _`task_clear_jobctl_trapping.description`:

Description
-----------

If JOBCTL_TRAPPING is set, a ptracer is waiting for us to enter TRACED.
Clear it and wake up the ptracer.  Note that we don't need any further
locking.  ``task``\ ->siglock guarantees that ``task``\ ->parent points to the
ptracer.

CONTEXT:
Must be called with ``task``\ ->sighand->siglock held.


.. _`task_clear_jobctl_pending`:

task_clear_jobctl_pending
=========================

.. c:function:: void task_clear_jobctl_pending (struct task_struct *task, unsigned long mask)

    clear jobctl pending bits

    :param struct task_struct \*task:
        target task

    :param unsigned long mask:
        pending bits to clear


.. _`task_clear_jobctl_pending.description`:

Description
-----------

Clear ``mask`` from ``task``\ ->jobctl.  ``mask`` must be subset of
``JOBCTL_PENDING_MASK``\ .  If ``JOBCTL_STOP_PENDING`` is being cleared, other
STOP bits are cleared together.

If clearing of ``mask`` leaves no stop or trap pending, this function calls
:c:func:`task_clear_jobctl_trapping`.

CONTEXT:
Must be called with ``task``\ ->sighand->siglock held.


.. _`task_participate_group_stop`:

task_participate_group_stop
===========================

.. c:function:: bool task_participate_group_stop (struct task_struct *task)

    participate in a group stop

    :param struct task_struct \*task:
        task participating in a group stop


.. _`task_participate_group_stop.description`:

Description
-----------

``task`` has ``JOBCTL_STOP_PENDING`` set and is participating in a group stop.
Group stop states are cleared and the group stop count is consumed if
``JOBCTL_STOP_CONSUME`` was set.  If the consumption completes the group
stop, the appropriate ``SIGNAL_``\ \* flags are set.

CONTEXT:
Must be called with ``task``\ ->sighand->siglock held.

RETURNS:
``true`` if group stop completion should be notified to the parent, ``false``
otherwise.


.. _`ptrace_trap_notify`:

ptrace_trap_notify
==================

.. c:function:: void ptrace_trap_notify (struct task_struct *t)

    schedule trap to notify ptracer

    :param struct task_struct \*t:
        tracee wanting to notify tracer


.. _`ptrace_trap_notify.description`:

Description
-----------

This function schedules sticky ptrace trap which is cleared on the next
TRAP_STOP to notify ptracer of an event.  ``t`` must have been seized by
ptracer.

If ``t`` is running, STOP trap will be taken.  If trapped for STOP and
ptracer is listening for events, tracee is woken up so that it can
re-trap for the new event.  If trapped otherwise, STOP trap will be
eventually taken without returning to userland after the existing traps
are finished by PTRACE_CONT.

CONTEXT:
Must be called with ``task``\ ->sighand->siglock held.


.. _`do_notify_parent_cldstop`:

do_notify_parent_cldstop
========================

.. c:function:: void do_notify_parent_cldstop (struct task_struct *tsk, bool for_ptracer, int why)

    notify parent of stopped/continued state change

    :param struct task_struct \*tsk:
        task reporting the state change

    :param bool for_ptracer:
        the notification is for ptracer

    :param int why:
        CLD_{CONTINUED|STOPPED|TRAPPED} to report


.. _`do_notify_parent_cldstop.description`:

Description
-----------

Notify ``tsk``\ 's parent that the stopped/continued state has changed.  If
``for_ptracer`` is ``false``\ , ``tsk``\ 's group leader notifies to its real parent.
If ``true``\ , ``tsk`` reports to ``tsk``\ ->parent which should be the ptracer.

CONTEXT:
Must be called with tasklist_lock at least read locked.


.. _`do_signal_stop`:

do_signal_stop
==============

.. c:function:: bool do_signal_stop (int signr)

    handle group stop for SIGSTOP and other stop signals

    :param int signr:
        signr causing group stop if initiating


.. _`do_signal_stop.description`:

Description
-----------

If ``JOBCTL_STOP_PENDING`` is not set yet, initiate group stop with ``signr``
and participate in it.  If already set, participate in the existing
group stop.  If participated in a group stop (and thus slept), ``true`` is
returned with siglock released.

If ptraced, this function doesn't handle stop itself.  Instead,
``JOBCTL_TRAP_STOP`` is scheduled and ``false`` is returned with siglock
untouched.  The caller must ensure that INTERRUPT trap handling takes
places afterwards.

CONTEXT:
Must be called with ``current``\ ->sighand->siglock held, which is released
on ``true`` return.

RETURNS:
``false`` if group stop is already cancelled or ptrace trap is scheduled.
``true`` if participated in group stop.


.. _`do_jobctl_trap`:

do_jobctl_trap
==============

.. c:function:: void do_jobctl_trap ( void)

    take care of ptrace jobctl traps

    :param void:
        no arguments


.. _`do_jobctl_trap.description`:

Description
-----------


When PT_SEIZED, it's used for both group stop and explicit
SEIZE/INTERRUPT traps.  Both generate PTRACE_EVENT_STOP trap with
accompanying siginfo.  If stopped, lower eight bits of exit_code contain
the stop signal; otherwise, ``SIGTRAP``\ .

When !PT_SEIZED, it's used only for group stop trap with stop signal
number as exit_code and no siginfo.

CONTEXT:
Must be called with ``current``\ ->sighand->siglock held, which may be
released and re-acquired before returning with intervening sleep.


.. _`signal_delivered`:

signal_delivered
================

.. c:function:: void signal_delivered (struct ksignal *ksig, int stepping)

    :param struct ksignal \*ksig:
        kernel signal struct

    :param int stepping:
        nonzero if debugger single-step or block-step in use


.. _`signal_delivered.description`:

Description
-----------

This function should be called when a signal has successfully been
delivered. It updates the blocked signals accordingly (\ ``ksig``\ ->ka.sa.sa_mask
is always blocked, and the signal itself is blocked unless ``SA_NODEFER``
is set in ``ksig``\ ->ka.sa.sa_flags.  Tracing is notified.


.. _`sys_restart_syscall`:

sys_restart_syscall
===================

.. c:function:: long sys_restart_syscall ( void)

    restart a system call

    :param void:
        no arguments


.. _`set_current_blocked`:

set_current_blocked
===================

.. c:function:: void set_current_blocked (sigset_t *newset)

    change current->blocked mask

    :param sigset_t \*newset:
        new mask


.. _`set_current_blocked.description`:

Description
-----------

It is wrong to change ->blocked directly, this helper should be used
to ensure the process can't miss a shared signal we are going to block.


.. _`sys_rt_sigprocmask`:

sys_rt_sigprocmask
==================

.. c:function:: long sys_rt_sigprocmask (int how, sigset_t __user *nset, sigset_t __user *oset, size_t sigsetsize)

    change the list of currently blocked signals

    :param int how:
        whether to add, remove, or set signals

    :param sigset_t __user \*nset:
        stores pending signals

    :param sigset_t __user \*oset:
        previous value of signal mask if non-null

    :param size_t sigsetsize:
        size of sigset_t type


.. _`sys_rt_sigpending`:

sys_rt_sigpending
=================

.. c:function:: long sys_rt_sigpending (sigset_t __user *uset, size_t sigsetsize)

    examine a pending signal that has been raised while blocked

    :param sigset_t __user \*uset:
        stores pending signals

    :param size_t sigsetsize:
        size of sigset_t type or larger


.. _`do_sigtimedwait`:

do_sigtimedwait
===============

.. c:function:: int do_sigtimedwait (const sigset_t *which, siginfo_t *info, const struct timespec *ts)

    wait for queued signals specified in @which

    :param const sigset_t \*which:
        queued signals to wait for

    :param siginfo_t \*info:
        if non-null, the signal's siginfo is returned here

    :param const struct timespec \*ts:
        upper bound on process time suspension


.. _`sys_rt_sigtimedwait`:

sys_rt_sigtimedwait
===================

.. c:function:: long sys_rt_sigtimedwait (const sigset_t __user *uthese, siginfo_t __user *uinfo, const struct timespec __user *uts, size_t sigsetsize)

    synchronously wait for queued signals specified in @uthese

    :param const sigset_t __user \*uthese:
        queued signals to wait for

    :param siginfo_t __user \*uinfo:
        if non-null, the signal's siginfo is returned here

    :param const struct timespec __user \*uts:
        upper bound on process time suspension

    :param size_t sigsetsize:
        size of sigset_t type


.. _`sys_kill`:

sys_kill
========

.. c:function:: long sys_kill (pid_t pid, int sig)

    send a signal to a process

    :param pid_t pid:
        the PID of the process

    :param int sig:
        signal to be sent


.. _`sys_tgkill`:

sys_tgkill
==========

.. c:function:: long sys_tgkill (pid_t tgid, pid_t pid, int sig)

    send signal to one specific thread

    :param pid_t tgid:
        the thread group ID of the thread

    :param pid_t pid:
        the PID of the thread

    :param int sig:
        signal to be sent


.. _`sys_tgkill.description`:

Description
-----------

This syscall also checks the ``tgid`` and returns -ESRCH even if the PID
exists but it's not belonging to the target process anymore. This
method solves the problem of threads exiting and PIDs getting reused.


.. _`sys_tkill`:

sys_tkill
=========

.. c:function:: long sys_tkill (pid_t pid, int sig)

    send signal to one specific task

    :param pid_t pid:
        the PID of the task

    :param int sig:
        signal to be sent


.. _`sys_tkill.description`:

Description
-----------

Send a signal to only one task, even if it's a CLONE_THREAD task.


.. _`sys_rt_sigqueueinfo`:

sys_rt_sigqueueinfo
===================

.. c:function:: long sys_rt_sigqueueinfo (pid_t pid, int sig, siginfo_t __user *uinfo)

    send signal information to a signal

    :param pid_t pid:
        the PID of the thread

    :param int sig:
        signal to be sent

    :param siginfo_t __user \*uinfo:
        signal info to be sent


.. _`sys_sigpending`:

sys_sigpending
==============

.. c:function:: long sys_sigpending (old_sigset_t __user *set)

    examine pending signals

    :param old_sigset_t __user \*set:
        where mask of pending signal is returned


.. _`sys_sigprocmask`:

sys_sigprocmask
===============

.. c:function:: long sys_sigprocmask (int how, old_sigset_t __user *nset, old_sigset_t __user *oset)

    examine and change blocked signals

    :param int how:
        whether to add, remove, or set signals

    :param old_sigset_t __user \*nset:
        signals to add or remove (if non-null)

    :param old_sigset_t __user \*oset:
        previous value of signal mask if non-null


.. _`sys_sigprocmask.description`:

Description
-----------

Some platforms have their own version with special arguments;
others support only sys_rt_sigprocmask.


.. _`sys_rt_sigaction`:

sys_rt_sigaction
================

.. c:function:: long sys_rt_sigaction (int sig, const struct sigaction __user *act, struct sigaction __user *oact, size_t sigsetsize)

    alter an action taken by a process

    :param int sig:
        signal to be sent

    :param const struct sigaction __user \*act:
        new sigaction

    :param struct sigaction __user \*oact:
        used to save the previous sigaction

    :param size_t sigsetsize:
        size of sigset_t type


.. _`sys_rt_sigsuspend`:

sys_rt_sigsuspend
=================

.. c:function:: long sys_rt_sigsuspend (sigset_t __user *unewset, size_t sigsetsize)

    replace the signal mask for a value with the @unewset value until a signal is received

    :param sigset_t __user \*unewset:
        new signal mask value

    :param size_t sigsetsize:
        size of sigset_t type

