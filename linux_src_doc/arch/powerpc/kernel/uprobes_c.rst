.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/uprobes.c

.. _`is_trap_insn`:

is_trap_insn
============

.. c:function:: bool is_trap_insn(uprobe_opcode_t *insn)

    check if the instruction is a trap variant

    :param insn:
        instruction to be checked.
        Returns true if \ ``insn``\  is a trap variant.
    :type insn: uprobe_opcode_t \*

.. _`arch_uprobe_analyze_insn`:

arch_uprobe_analyze_insn
========================

.. c:function:: int arch_uprobe_analyze_insn(struct arch_uprobe *auprobe, struct mm_struct *mm, unsigned long addr)

    :param auprobe:
        *undescribed*
    :type auprobe: struct arch_uprobe \*

    :param mm:
        the probed address space.
    :type mm: struct mm_struct \*

    :param addr:
        vaddr to probe.
        Return 0 on success or a -ve number on error.
    :type addr: unsigned long

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

.. This file was automatic generated / don't edit.

