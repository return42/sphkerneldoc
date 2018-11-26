.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/include/asm/ptrace.h

.. _`regs_get_register`:

regs_get_register
=================

.. c:function:: unsigned long regs_get_register(struct pt_regs *regs, unsigned int offset)

    get register value from its offset

    :param regs:
        pt_regs from which register value is gotten
    :type regs: struct pt_regs \*

    :param offset:
        offset number of the register.
    :type offset: unsigned int

.. _`regs_get_register.description`:

Description
-----------

regs_get_register returns the value of a register whose offset from \ ``regs``\ .
The \ ``offset``\  is the offset of the register in struct pt_regs.
If \ ``offset``\  is bigger than MAX_REG_OFFSET, this returns 0.

.. This file was automatic generated / don't edit.

