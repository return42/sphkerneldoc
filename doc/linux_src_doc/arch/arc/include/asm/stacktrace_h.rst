.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arc/include/asm/stacktrace.h

.. _`arc_unwind_core`:

arc_unwind_core
===============

.. c:function:: notrace noinline unsigned int arc_unwind_core(struct task_struct *tsk, struct pt_regs *regs, int (*) consumer_fn (unsigned int, void *, void *arg)

    Unwind the kernel mode stack for an execution context

    :param struct task_struct \*tsk:
        NULL for current task, specific task otherwise

    :param struct pt_regs \*regs:
        pt_regs used to seed the unwinder {SP, FP, BLINK, PC}
        If NULL, use pt_regs of \ ``tsk``\  (if !NULL) otherwise
        use the current values of {SP, FP, BLINK, PC}

    :param (int (\*) consumer_fn (unsigned int, void \*):
        Callback invoked for each frame unwound
        Returns 0 to continue unwinding, -1 to stop

    :param void \*arg:
        Arg to callback

.. _`arc_unwind_core.description`:

Description
-----------

Returns the address of first function in stack

.. _`arc_unwind_core.semantics`:

Semantics
---------

- synchronous unwinding (e.g. dump_stack): \ ``tsk``\   NULL, \ ``regs``\   NULL
- Asynchronous unwinding of sleeping task: \ ``tsk``\  !NULL, \ ``regs``\   NULL
- Asynchronous unwinding of intr/excp etc: \ ``tsk``\  !NULL, \ ``regs``\  !NULL

.. This file was automatic generated / don't edit.

