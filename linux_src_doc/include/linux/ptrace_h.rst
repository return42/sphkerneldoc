.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ptrace.h

.. _`ptrace_may_access`:

ptrace_may_access
=================

.. c:function:: bool ptrace_may_access(struct task_struct *task, unsigned int mode)

    check whether the caller is permitted to access a target task.

    :param struct task_struct \*task:
        target task

    :param unsigned int mode:
        selects type of access and caller credentials

.. _`ptrace_may_access.description`:

Description
-----------

Returns true on success, false on denial.

One of the flags PTRACE_MODE_FSCREDS and PTRACE_MODE_REALCREDS must
be set in \ ``mode``\  to specify whether the access was requested through
a filesystem syscall (should use effective capabilities and fsuid
of the caller) or through an explicit syscall such as
process_vm_writev or ptrace (and should use the real credentials).

.. _`ptrace_parent`:

ptrace_parent
=============

.. c:function:: struct task_struct *ptrace_parent(struct task_struct *task)

    return the task that is tracing the given task

    :param struct task_struct \*task:
        task to consider

.. _`ptrace_parent.description`:

Description
-----------

Returns \ ``NULL``\  if no one is tracing \ ``task``\ , or the \ :c:type:`struct task_struct <task_struct>`\ 
pointer to its tracer.

Must called under \ :c:func:`rcu_read_lock`\ .  The pointer returned might be kept
live only by RCU.  During exec, this may be called with \ :c:func:`task_lock`\  held
on \ ``task``\ , still held from when \ :c:func:`check_unsafe_exec`\  was called.

.. _`ptrace_event_enabled`:

ptrace_event_enabled
====================

.. c:function:: bool ptrace_event_enabled(struct task_struct *task, int event)

    test whether a ptrace event is enabled

    :param struct task_struct \*task:
        ptracee of interest

    :param int event:
        %PTRACE_EVENT\_\* to test

.. _`ptrace_event_enabled.description`:

Description
-----------

Test whether \ ``event``\  is enabled for ptracee \ ``task``\ .

Returns \ ``true``\  if \ ``event``\  is enabled, \ ``false``\  otherwise.

.. _`ptrace_event`:

ptrace_event
============

.. c:function:: void ptrace_event(int event, unsigned long message)

    possibly stop for a ptrace event notification

    :param int event:
        %PTRACE_EVENT\_\* value to report

    :param unsigned long message:
        value for \ ``PTRACE_GETEVENTMSG``\  to return

.. _`ptrace_event.description`:

Description
-----------

Check whether \ ``event``\  is enabled and, if so, report \ ``event``\  and \ ``message``\ 
to the ptrace parent.

Called without locks.

.. _`ptrace_event_pid`:

ptrace_event_pid
================

.. c:function:: void ptrace_event_pid(int event, struct pid *pid)

    possibly stop for a ptrace event notification

    :param int event:
        %PTRACE_EVENT\_\* value to report

    :param struct pid \*pid:
        process identifier for \ ``PTRACE_GETEVENTMSG``\  to return

.. _`ptrace_event_pid.description`:

Description
-----------

Check whether \ ``event``\  is enabled and, if so, report \ ``event``\  and \ ``pid``\ 
to the ptrace parent.  \ ``pid``\  is reported as the pid_t seen from the
the ptrace parent's pid namespace.

Called without locks.

.. _`ptrace_init_task`:

ptrace_init_task
================

.. c:function:: void ptrace_init_task(struct task_struct *child, bool ptrace)

    initialize ptrace state for a new child

    :param struct task_struct \*child:
        new child task

    :param bool ptrace:
        true if child should be ptrace'd by parent's tracer

.. _`ptrace_init_task.description`:

Description
-----------

This is called immediately after adding \ ``child``\  to its parent's children
list.  \ ``ptrace``\  is false in the normal case, and true to ptrace \ ``child``\ .

Called with current's siglock and write_lock_irq(&tasklist_lock) held.

.. _`ptrace_release_task`:

ptrace_release_task
===================

.. c:function:: void ptrace_release_task(struct task_struct *task)

    final ptrace-related cleanup of a zombie being reaped

    :param struct task_struct \*task:
        task in \ ``EXIT_DEAD``\  state

.. _`ptrace_release_task.description`:

Description
-----------

Called with write_lock(&tasklist_lock) held.

.. _`arch_has_single_step`:

arch_has_single_step
====================

.. c:function::  arch_has_single_step( void)

    does this CPU support user-mode single-step?

    :param  void:
        no arguments

.. _`arch_has_single_step.description`:

Description
-----------

If this is defined, then there must be function declarations or
inlines for \ :c:func:`user_enable_single_step`\  and \ :c:func:`user_disable_single_step`\ .
\ :c:func:`arch_has_single_step`\  should evaluate to nonzero iff the machine
supports instruction single-step for user mode.
It can be a constant or it can test a CPU feature bit.

.. _`user_enable_single_step`:

user_enable_single_step
=======================

.. c:function:: void user_enable_single_step(struct task_struct *task)

    single-step in user-mode task

    :param struct task_struct \*task:
        either current or a task stopped in \ ``TASK_TRACED``\ 

.. _`user_enable_single_step.description`:

Description
-----------

This can only be called when \ :c:func:`arch_has_single_step`\  has returned nonzero.
Set \ ``task``\  so that when it returns to user mode, it will trap after the
next single instruction executes.  If \ :c:func:`arch_has_block_step`\  is defined,
this must clear the effects of \ :c:func:`user_enable_block_step`\  too.

.. _`user_disable_single_step`:

user_disable_single_step
========================

.. c:function:: void user_disable_single_step(struct task_struct *task)

    cancel user-mode single-step

    :param struct task_struct \*task:
        either current or a task stopped in \ ``TASK_TRACED``\ 

.. _`user_disable_single_step.description`:

Description
-----------

Clear \ ``task``\  of the effects of \ :c:func:`user_enable_single_step`\  and
\ :c:func:`user_enable_block_step`\ .  This can be called whether or not either
of those was ever called on \ ``task``\ , and even if \ :c:func:`arch_has_single_step`\ 
returned zero.

.. _`arch_has_block_step`:

arch_has_block_step
===================

.. c:function::  arch_has_block_step( void)

    does this CPU support user-mode block-step?

    :param  void:
        no arguments

.. _`arch_has_block_step.description`:

Description
-----------

If this is defined, then there must be a function declaration or inline
for \ :c:func:`user_enable_block_step`\ , and \ :c:func:`arch_has_single_step`\  must be defined
too.  \ :c:func:`arch_has_block_step`\  should evaluate to nonzero iff the machine
supports step-until-branch for user mode.  It can be a constant or it
can test a CPU feature bit.

.. _`user_enable_block_step`:

user_enable_block_step
======================

.. c:function:: void user_enable_block_step(struct task_struct *task)

    step until branch in user-mode task

    :param struct task_struct \*task:
        either current or a task stopped in \ ``TASK_TRACED``\ 

.. _`user_enable_block_step.description`:

Description
-----------

This can only be called when \ :c:func:`arch_has_block_step`\  has returned nonzero,
and will never be called when single-instruction stepping is being used.
Set \ ``task``\  so that when it returns to user mode, it will trap after the
next branch or trap taken.

.. _`arch_ptrace_stop_needed`:

arch_ptrace_stop_needed
=======================

.. c:function::  arch_ptrace_stop_needed( code,  info)

    Decide whether \ :c:func:`arch_ptrace_stop`\  should be called

    :param  code:
        current->exit_code value ptrace will stop with

    :param  info:
        siginfo_t pointer (or \ ``NULL``\ ) for signal ptrace will stop with

.. _`arch_ptrace_stop_needed.description`:

Description
-----------

This is called with the siglock held, to decide whether or not it's
necessary to release the siglock and call \ :c:func:`arch_ptrace_stop`\  with the
same \ ``code``\  and \ ``info``\  arguments.  It can be defined to a constant if
\ :c:func:`arch_ptrace_stop`\  is never required, or always is.  On machines where
this makes sense, it should be defined to a quick test to optimize out
calling \ :c:func:`arch_ptrace_stop`\  when it would be superfluous.  For example,
if the thread has not been back to user mode since the last stop, the
thread state might indicate that nothing needs to be done.

This is guaranteed to be invoked once before a task stops for ptrace and
may include arch-specific operations necessary prior to a ptrace stop.

.. _`arch_ptrace_stop`:

arch_ptrace_stop
================

.. c:function::  arch_ptrace_stop( code,  info)

    Do machine-specific work before stopping for ptrace

    :param  code:
        current->exit_code value ptrace will stop with

    :param  info:
        siginfo_t pointer (or \ ``NULL``\ ) for signal ptrace will stop with

.. _`arch_ptrace_stop.description`:

Description
-----------

This is called with no locks held when \ :c:func:`arch_ptrace_stop_needed`\  has
just returned nonzero.  It is allowed to block, e.g. for user memory
access.  The arch can have machine-specific work to be done before
ptrace stops.  On ia64, register backing store gets written back to user
memory here.  Since this can be costly (requires dropping the siglock),
we only do it when the arch requires it for this particular stop, as
indicated by \ :c:func:`arch_ptrace_stop_needed`\ .

.. This file was automatic generated / don't edit.

