.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kernel/ptrace.c

.. _`regs_query_register_offset`:

regs_query_register_offset
==========================

.. c:function:: int regs_query_register_offset(const char *name)

    query register offset from its name

    :param const char \*name:
        the name of a register

.. _`regs_query_register_offset.description`:

Description
-----------

\ :c:func:`regs_query_register_offset`\  returns the offset of a register in struct
pt_regs from its name. If the name is invalid, this returns -EINVAL;

.. _`regs_within_kernel_stack`:

regs_within_kernel_stack
========================

.. c:function:: bool regs_within_kernel_stack(struct pt_regs *regs, unsigned long addr)

    check the address in the stack

    :param struct pt_regs \*regs:
        pt_regs which contains kernel stack pointer.

    :param unsigned long addr:
        address which is checked.

.. _`regs_within_kernel_stack.description`:

Description
-----------

\ :c:func:`regs_within_kernel_stack`\  checks \ ``addr``\  is within the kernel stack page(s).
If \ ``addr``\  is within the kernel stack, it returns true. If not, returns false.

.. _`regs_get_kernel_stack_nth`:

regs_get_kernel_stack_nth
=========================

.. c:function:: unsigned long regs_get_kernel_stack_nth(struct pt_regs *regs, unsigned int n)

    get Nth entry of the stack

    :param struct pt_regs \*regs:
        pt_regs which contains kernel stack pointer.

    :param unsigned int n:
        stack entry number.

.. _`regs_get_kernel_stack_nth.description`:

Description
-----------

\ :c:func:`regs_get_kernel_stack_nth`\  returns \ ``n``\  th entry of the kernel stack which
is specified by \ ``regs``\ . If the \ ``n``\  th entry is NOT in the kernel stack,
this returns 0.

.. This file was automatic generated / don't edit.

