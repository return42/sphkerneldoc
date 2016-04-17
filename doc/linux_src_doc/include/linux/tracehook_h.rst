.. -*- coding: utf-8; mode: rst -*-

===========
tracehook.h
===========


.. _`tracehook_report_syscall_entry`:

tracehook_report_syscall_entry
==============================

.. c:function:: int tracehook_report_syscall_entry (struct pt_regs *regs)

    task is about to attempt a system call

    :param struct pt_regs \*regs:
        user register state of current task



.. _`tracehook_report_syscall_entry.description`:

Description
-----------

This will be called if ``TIF_SYSCALL_TRACE`` has been set, when the
current task has just entered the kernel for a system call.
Full user register state is available here.  Changing the values
in ``regs`` can affect the system call number and arguments to be tried.
It is safe to block here, preventing the system call from beginning.

Returns zero normally, or nonzero if the calling arch code should abort
the system call.  That must prevent normal entry so no system call is
made.  If ``task`` ever returns to user mode after this, its register state
is unspecified, but should be something harmless like an ``ENOSYS`` error
return.  It should preserve enough information so that :c:func:`syscall_rollback`
can work (see asm-generic/syscall.h).

Called without locks, just after entering kernel mode.



.. _`tracehook_report_syscall_exit`:

tracehook_report_syscall_exit
=============================

.. c:function:: void tracehook_report_syscall_exit (struct pt_regs *regs, int step)

    task has just finished a system call

    :param struct pt_regs \*regs:
        user register state of current task

    :param int step:
        nonzero if simulating single-step or block-step



.. _`tracehook_report_syscall_exit.description`:

Description
-----------

This will be called if ``TIF_SYSCALL_TRACE`` has been set, when the
current task has just finished an attempted system call.  Full
user register state is available here.  It is safe to block here,
preventing signals from being processed.

If ``step`` is nonzero, this report is also in lieu of the normal
trap that would follow the system call instruction because
:c:func:`user_enable_block_step` or :c:func:`user_enable_single_step` was used.
In this case, ``TIF_SYSCALL_TRACE`` might not be set.

Called without locks, just before checking for pending signals.



.. _`tracehook_signal_handler`:

tracehook_signal_handler
========================

.. c:function:: void tracehook_signal_handler (int stepping)

    signal handler setup is complete

    :param int stepping:
        nonzero if debugger single-step or block-step in use



.. _`tracehook_signal_handler.description`:

Description
-----------

Called by the arch code after a signal handler has been set up.
Register and stack state reflects the user handler about to run.
Signal mask changes have already been made.

Called without locks, shortly before returning to user mode
(or handling more signals).



.. _`set_notify_resume`:

set_notify_resume
=================

.. c:function:: void set_notify_resume (struct task_struct *task)

    cause tracehook_notify_resume() to be called

    :param struct task_struct \*task:
        task that will call :c:func:`tracehook_notify_resume`



.. _`set_notify_resume.description`:

Description
-----------

Calling this arranges that ``task`` will call :c:func:`tracehook_notify_resume`
before returning to user mode.  If it's already running in user mode,
it will enter the kernel and call :c:func:`tracehook_notify_resume` soon.
If it's blocked, it will not be woken.



.. _`tracehook_notify_resume`:

tracehook_notify_resume
=======================

.. c:function:: void tracehook_notify_resume (struct pt_regs *regs)

    report when about to return to user mode

    :param struct pt_regs \*regs:
        user-mode registers of ``current`` task



.. _`tracehook_notify_resume.description`:

Description
-----------

This is called when ``TIF_NOTIFY_RESUME`` has been set.  Now we are
about to return to user mode, and the user state in ``regs`` can be
inspected or adjusted.  The caller in arch code has cleared
``TIF_NOTIFY_RESUME`` before the call.  If the flag gets set again
asynchronously, this will be called again before we return to
user mode.

Called without locks.

