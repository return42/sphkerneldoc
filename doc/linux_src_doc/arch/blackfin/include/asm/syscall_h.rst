.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/blackfin/include/asm/syscall.h

.. _`syscall_get_arguments`:

syscall_get_arguments
=====================

.. c:function:: void syscall_get_arguments(struct task_struct *task, struct pt_regs *regs, unsigned int i, unsigned int n, unsigned long *args)

    :param struct task_struct \*task:
        unused

    :param struct pt_regs \*regs:
        the register layout to extract syscall arguments from

    :param unsigned int i:
        first syscall argument to extract

    :param unsigned int n:
        number of syscall arguments to extract

    :param unsigned long \*args:
        array to return the syscall arguments in

.. _`syscall_get_arguments.description`:

Description
-----------

args[0] gets i'th argument, args[n - 1] gets the i+n-1'th argument

.. This file was automatic generated / don't edit.

