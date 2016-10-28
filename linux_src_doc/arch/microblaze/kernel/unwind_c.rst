.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/microblaze/kernel/unwind.c

.. _`get_frame_size`:

get_frame_size
==============

.. c:function:: long get_frame_size(unsigned long instr)

    Extract the stack adjustment from an "addik r1, r1, adjust" instruction

    :param unsigned long instr:
        Microblaze instruction

.. _`get_frame_size.description`:

Description
-----------

Return - Number of stack bytes the instruction reserves or reclaims

.. _`find_frame_creation`:

find_frame_creation
===================

.. c:function:: unsigned long *find_frame_creation(unsigned long *pc)

    Search backward to find the instruction that creates the stack frame (hopefully, for the same function the initial PC is in).

    :param unsigned long \*pc:
        Program counter at which to begin the search

.. _`find_frame_creation.description`:

Description
-----------

Return - PC at which stack frame creation occurs
NULL if this cannot be found, i.e. a leaf function

.. _`lookup_prev_stack_frame`:

lookup_prev_stack_frame
=======================

.. c:function:: int lookup_prev_stack_frame(unsigned long fp, unsigned long pc, unsigned long leaf_return, unsigned long *pprev_fp, unsigned long *pprev_pc)

    Find the stack frame of the previous function.

    :param unsigned long fp:
        Frame (stack) pointer for current function

    :param unsigned long pc:
        Program counter within current function

    :param unsigned long leaf_return:
        r15 value within current function. If the current function
        is a leaf, this is the caller's return address.

    :param unsigned long \*pprev_fp:
        On exit, set to frame (stack) pointer for previous function

    :param unsigned long \*pprev_pc:
        On exit, set to current function caller's return address

.. _`lookup_prev_stack_frame.description`:

Description
-----------

Return - 0 on success, -EINVAL if the previous frame cannot be found

.. _`unwind_trap`:

unwind_trap
===========

.. c:function:: void unwind_trap(struct task_struct *task, unsigned long pc, unsigned long fp, struct stack_trace *trace)

    Unwind through a system trap, that stored previous state on the stack.

    :param struct task_struct \*task:
        *undescribed*

    :param unsigned long pc:
        *undescribed*

    :param unsigned long fp:
        *undescribed*

    :param struct stack_trace \*trace:
        *undescribed*

.. _`microblaze_unwind_inner`:

microblaze_unwind_inner
=======================

.. c:function:: void microblaze_unwind_inner(struct task_struct *task, unsigned long pc, unsigned long fp, unsigned long leaf_return, struct stack_trace *trace)

    Unwind the stack from the specified point

    :param struct task_struct \*task:
        Task whose stack we are to unwind (may be NULL)

    :param unsigned long pc:
        Program counter from which we start unwinding

    :param unsigned long fp:
        Frame (stack) pointer from which we start unwinding

    :param unsigned long leaf_return:
        Value of r15 at pc. If the function is a leaf, this is
        the caller's return address.

    :param struct stack_trace \*trace:
        Where to store stack backtrace (PC values).
        NULL == print backtrace to kernel log

.. _`microblaze_unwind`:

microblaze_unwind
=================

.. c:function:: void microblaze_unwind(struct task_struct *task, struct stack_trace *trace)

    Stack unwinder for Microblaze (external entry point)

    :param struct task_struct \*task:
        Task whose stack we are to unwind (NULL == current)

    :param struct stack_trace \*trace:
        Where to store stack backtrace (PC values).
        NULL == print backtrace to kernel log

.. This file was automatic generated / don't edit.

