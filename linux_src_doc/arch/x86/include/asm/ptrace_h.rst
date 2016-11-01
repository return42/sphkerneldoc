.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/ptrace.h

.. _`regs_get_register`:

regs_get_register
=================

.. c:function:: unsigned long regs_get_register(struct pt_regs *regs, unsigned int offset)

    get register value from its offset

    :param struct pt_regs \*regs:
        pt_regs from which register value is gotten.

    :param unsigned int offset:
        offset number of the register.

.. _`regs_get_register.description`:

Description
-----------

regs_get_register returns the value of a register. The \ ``offset``\  is the
offset of the register in struct pt_regs address which specified by \ ``regs``\ .
If \ ``offset``\  is bigger than MAX_REG_OFFSET, this returns 0.

.. _`regs_within_kernel_stack`:

regs_within_kernel_stack
========================

.. c:function:: int regs_within_kernel_stack(struct pt_regs *regs, unsigned long addr)

    check the address in the stack

    :param struct pt_regs \*regs:
        pt_regs which contains kernel stack pointer.

    :param unsigned long addr:
        address which is checked.

.. _`regs_within_kernel_stack.description`:

Description
-----------

regs_within_kernel_stack() checks \ ``addr``\  is within the kernel stack page(s).
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

regs_get_kernel_stack_nth() returns \ ``n``\  th entry of the kernel stack which
is specified by \ ``regs``\ . If the \ ``n``\  th entry is NOT in the kernel stack,
this returns 0.

.. This file was automatic generated / don't edit.

