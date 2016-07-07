.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kernel/uprobes.c

.. _`arch_uprobe_analyze_insn`:

arch_uprobe_analyze_insn
========================

.. c:function:: int arch_uprobe_analyze_insn(struct arch_uprobe *aup, struct mm_struct *mm, unsigned long addr)

    instruction analysis including validity and fixups.

    :param struct arch_uprobe \*aup:
        *undescribed*

    :param struct mm_struct \*mm:
        the probed address space.

    :param unsigned long addr:
        virtual address at which to install the probepoint
        Return 0 on success or a -ve number on error.

.. _`is_trap_insn`:

is_trap_insn
============

.. c:function:: bool is_trap_insn(uprobe_opcode_t *insn)

    check if the instruction is a trap variant

    :param uprobe_opcode_t \*insn:
        instruction to be checked.
        Returns true if \ ``insn``\  is a trap variant.

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

    :param struct arch_uprobe \*auprobe:
        arch specific probepoint information.

    :param struct mm_struct \*mm:
        the probed process address space.

    :param unsigned long vaddr:
        the virtual address to insert the opcode.

.. _`set_swbp.description`:

Description
-----------

For mm \ ``mm``\ , store the breakpoint instruction at \ ``vaddr``\ .
Return 0 (success) or a negative errno.

This version overrides the weak version in kernel/events/uprobes.c.
It is required to handle MIPS16 and microMIPS.

.. _`set_orig_insn`:

set_orig_insn
=============

.. c:function:: int set_orig_insn(struct arch_uprobe *auprobe, struct mm_struct *mm, unsigned long vaddr)

    Restore the original instruction.

    :param struct arch_uprobe \*auprobe:
        arch specific probepoint information.

    :param struct mm_struct \*mm:
        the probed process address space.

    :param unsigned long vaddr:
        the virtual address to insert the opcode.

.. _`set_orig_insn.description`:

Description
-----------

For mm \ ``mm``\ , restore the original opcode (opcode) at \ ``vaddr``\ .
Return 0 (success) or a negative errno.

This overrides the weak version in kernel/events/uprobes.c.

.. _`uprobe_get_swbp_addr`:

uprobe_get_swbp_addr
====================

.. c:function:: unsigned long uprobe_get_swbp_addr(struct pt_regs *regs)

    compute address of swbp given post-swbp regs

    :param struct pt_regs \*regs:
        Reflects the saved state of the task after it has hit a breakpoint
        instruction.
        Return the address of the breakpoint instruction.

.. _`uprobe_get_swbp_addr.description`:

Description
-----------

This overrides the weak version in kernel/events/uprobes.c.

.. This file was automatic generated / don't edit.

