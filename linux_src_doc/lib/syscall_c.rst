.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/syscall.c

.. _`task_current_syscall`:

task_current_syscall
====================

.. c:function:: int task_current_syscall(struct task_struct *target, long *callno, unsigned long args, unsigned int maxargs, unsigned long *sp, unsigned long *pc)

    Discover what a blocked task is doing.

    :param target:
        thread to examine
    :type target: struct task_struct \*

    :param callno:
        filled with system call number or -1
    :type callno: long \*

    :param args:
        filled with \ ``maxargs``\  system call arguments
    :type args: unsigned long

    :param maxargs:
        number of elements in \ ``args``\  to fill
    :type maxargs: unsigned int

    :param sp:
        filled with user stack pointer
    :type sp: unsigned long \*

    :param pc:
        filled with user PC
    :type pc: unsigned long \*

.. _`task_current_syscall.description`:

Description
-----------

If \ ``target``\  is blocked in a system call, returns zero with \*@callno
set to the the call's number and \ ``args``\  filled in with its arguments.
Registers not used for system call arguments may not be available and
it is not kosher to use \ :c:type:`struct user_regset <user_regset>`\  calls while the system
call is still in progress.  Note we may get this result if \ ``target``\ 
has finished its system call but not yet returned to user mode, such
as when it's stopped for signal handling or syscall exit tracing.

If \ ``target``\  is blocked in the kernel during a fault or exception,
returns zero with \*@callno set to -1 and does not fill in \ ``args``\ .
If so, it's now safe to examine \ ``target``\  using \ :c:type:`struct user_regset <user_regset>`\ 
\ :c:func:`get`\  calls as long as we're sure \ ``target``\  won't return to user mode.

Returns -%EAGAIN if \ ``target``\  does not remain blocked.

Returns -%EINVAL if \ ``maxargs``\  is too large (maximum is six).

.. This file was automatic generated / don't edit.

