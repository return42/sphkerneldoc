.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/kernel/ptrace.c

.. _`regs_get_kernel_stack_nth`:

regs_get_kernel_stack_nth
=========================

.. c:function:: unsigned long regs_get_kernel_stack_nth(struct pt_regs *regs, unsigned int n)

    get Nth entry of the stack

    :param regs:
        pt_regs which contains kernel stack pointer.
    :type regs: struct pt_regs \*

    :param n:
        stack entry number.
    :type n: unsigned int

.. _`regs_get_kernel_stack_nth.description`:

Description
-----------

\ :c:func:`regs_get_kernel_stack_nth`\  returns \ ``n``\  th entry of the kernel stack which
is specifined by \ ``regs``\ . If the \ ``n``\  th entry is NOT in the kernel stack,
this returns 0.

.. This file was automatic generated / don't edit.

