.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kernel/uprobes.c

.. _`arch_uprobe_analyze_insn`:

arch_uprobe_analyze_insn
========================

.. c:function:: int arch_uprobe_analyze_insn(struct arch_uprobe *aup, struct mm_struct *mm, unsigned long addr)

    instruction analysis including validity and fixups.

    :param aup:
        *undescribed*
    :type aup: struct arch_uprobe \*

    :param mm:
        the probed address space.
    :type mm: struct mm_struct \*

    :param addr:
        virtual address at which to install the probepoint
        Return 0 on success or a -ve number on error.
    :type addr: unsigned long

.. _`is_trap_insn`:

is_trap_insn
============

.. c:function:: bool is_trap_insn(uprobe_opcode_t *insn)

    check if the instruction is a trap variant

    :param insn:
        instruction to be checked.
        Returns true if \ ``insn``\  is a trap variant.
    :type insn: uprobe_opcode_t \*

.. _`is_trap_insn.description`:

Description
-----------

This definition overrides the weak definition in kernel/events/uprobes.c.
and is needed for the case where an architecture has multiple trap
instructions (like PowerPC or MIPS).  We treat BREAK just like the more
modern conditional trap instructions.

.. _`set_swbp`:

set_swbp
========

.. c:function:: int set_swbp(struct arch_uprobe *auprobe, struct mm_struct *mm, unsigned long vaddr)

    store breakpoint at a given address.

    :param auprobe:
        arch specific probepoint information.
    :type auprobe: struct arch_uprobe \*

    :param mm:
        the probed process address space.
    :type mm: struct mm_struct \*

    :param vaddr:
        the virtual address to insert the opcode.
    :type vaddr: unsigned long

.. _`set_swbp.description`:

Description
-----------

For mm \ ``mm``\ , store the breakpoint instruction at \ ``vaddr``\ .
Return 0 (success) or a negative errno.

This version overrides the weak version in kernel/events/uprobes.c.
It is required to handle MIPS16 and microMIPS.

.. _`uprobe_get_swbp_addr`:

uprobe_get_swbp_addr
====================

.. c:function:: unsigned long uprobe_get_swbp_addr(struct pt_regs *regs)

    compute address of swbp given post-swbp regs

    :param regs:
        Reflects the saved state of the task after it has hit a breakpoint
        instruction.
        Return the address of the breakpoint instruction.
    :type regs: struct pt_regs \*

.. _`uprobe_get_swbp_addr.description`:

Description
-----------

This overrides the weak version in kernel/events/uprobes.c.

.. This file was automatic generated / don't edit.

