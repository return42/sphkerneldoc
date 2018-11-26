.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sparc/kernel/ptrace_64.c

.. _`regs_query_register_offset`:

regs_query_register_offset
==========================

.. c:function:: int regs_query_register_offset(const char *name)

    query register offset from its name

    :param name:
        the name of a register
    :type name: const char \*

.. _`regs_query_register_offset.description`:

Description
-----------

\ :c:func:`regs_query_register_offset`\  returns the offset of a register in struct
pt_regs from its name. If the name is invalid, this returns -EINVAL;

.. _`regs_within_kernel_stack`:

regs_within_kernel_stack
========================

.. c:function:: int regs_within_kernel_stack(struct pt_regs *regs, unsigned long addr)

    check the address in the stack

    :param regs:
        pt_regs which contains kernel stack pointer.
    :type regs: struct pt_regs \*

    :param addr:
        address which is checked.
    :type addr: unsigned long

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
is specified by \ ``regs``\ . If the \ ``n``\  th entry is NOT in the kernel stack,
this returns 0.

.. This file was automatic generated / don't edit.

