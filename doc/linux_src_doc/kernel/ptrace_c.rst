.. -*- coding: utf-8; mode: rst -*-

========
ptrace.c
========


.. _`__ptrace_unlink`:

__ptrace_unlink
===============

.. c:function:: void __ptrace_unlink (struct task_struct *child)

    unlink ptracee and restore its execution state

    :param struct task_struct \*child:
        ptracee to be unlinked



.. _`__ptrace_unlink.description`:

Description
-----------

Remove ``child`` from the ptrace list, move it back to the original parent,
and restore the execution state so that it conforms to the group stop
state.

Unlinking can happen via two paths - explicit PTRACE_DETACH or ptracer
exiting.  For PTRACE_DETACH, unless the ptracee has been killed between
:c:func:`ptrace_check_attach` and here, it's guaranteed to be in TASK_TRACED.
If the ptracer is exiting, the ptracee can be in any state.

After detach, the ptracee should be in a state which conforms to the
group stop.  If the group is stopped or in the process of stopping, the
ptracee should be put into TASK_STOPPED; otherwise, it should be woken
up from TASK_TRACED.

If the ptracee is in TASK_TRACED and needs to be moved to TASK_STOPPED,
it goes through TRACED -> RUNNING -> STOPPED transition which is similar
to but in the opposite direction of what happens while attaching to a
stopped task.  However, in this direction, the intermediate RUNNING
state is not hidden even from the current ptracer and if it immediately
re-attaches and performs a WNOHANG wait(2), it may fail.



.. _`__ptrace_unlink.context`:

CONTEXT
-------

write_lock_irq(tasklist_lock)



.. _`ptrace_check_attach`:

ptrace_check_attach
===================

.. c:function:: int ptrace_check_attach (struct task_struct *child, bool ignore_state)

    check whether ptracee is ready for ptrace operation

    :param struct task_struct \*child:
        ptracee to check for

    :param bool ignore_state:
        don't check whether ``child`` is currently ``TASK_TRACED``



.. _`ptrace_check_attach.description`:

Description
-----------

Check whether ``child`` is being ptraced by ``current`` and ready for further
ptrace operations.  If ``ignore_state`` is ``false``\ , ``child`` also should be in
``TASK_TRACED`` state and on return the child is guaranteed to be traced
and not executing.  If ``ignore_state`` is ``true``\ , ``child`` can be in any
state.



.. _`ptrace_check_attach.context`:

CONTEXT
-------

Grabs and releases tasklist_lock and ``child``\ ->sighand->siglock.



.. _`ptrace_check_attach.returns`:

RETURNS
-------

0 on success, -ESRCH if ``child`` is not ready.



.. _`ptrace_traceme`:

ptrace_traceme
==============

.. c:function:: int ptrace_traceme ( void)

    - helper for PTRACE_TRACEME

    :param void:
        no arguments



.. _`ptrace_traceme.description`:

Description
-----------


Performs checks and sets PT_PTRACED.
Should be used by all ptrace implementations for PTRACE_TRACEME.

