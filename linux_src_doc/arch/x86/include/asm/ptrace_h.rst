.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/include/asm/ptrace.h

.. _`regs_get_register`:

regs_get_register
=================

.. c:function:: unsigned long regs_get_register(struct pt_regs *regs, unsigned int offset)

    get register value from its offset

    :param regs:
        pt_regs from which register value is gotten.
    :type regs: struct pt_regs \*

    :param offset:
        offset number of the register.
    :type offset: unsigned int

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

.. _`regs_get_kernel_stack_nth_addr`:

regs_get_kernel_stack_nth_addr
==============================

.. c:function:: unsigned long *regs_get_kernel_stack_nth_addr(struct pt_regs *regs, unsigned int n)

    get the address of the Nth entry on stack

    :param regs:
        pt_regs which contains kernel stack pointer.
    :type regs: struct pt_regs \*

    :param n:
        stack entry number.
    :type n: unsigned int

.. _`regs_get_kernel_stack_nth_addr.description`:

Description
-----------

\ :c:func:`regs_get_kernel_stack_nth`\  returns the address of the \ ``n``\  th entry of the
kernel stack which is specified by \ ``regs``\ . If the \ ``n``\  th entry is NOT in
the kernel stack, this returns NULL.

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
is specified by \ ``regs``\ . If the \ ``n``\  th entry is NOT in the kernel stack
this returns 0.

.. _`regs_get_kernel_argument`:

regs_get_kernel_argument
========================

.. c:function:: unsigned long regs_get_kernel_argument(struct pt_regs *regs, unsigned int n)

    get Nth function argument in kernel

    :param regs:
        pt_regs of that context
    :type regs: struct pt_regs \*

    :param n:
        function argument number (start from 0)
    :type n: unsigned int

.. _`regs_get_kernel_argument.description`:

Description
-----------

\ :c:func:`regs_get_argument`\  returns \ ``n``\  th argument of the function call.
Note that this chooses most probably assignment, in some case
it can be incorrect.
This is expected to be called from kprobes or ftrace with regs
where the top of stack is the return address.

.. This file was automatic generated / don't edit.

