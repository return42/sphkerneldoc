.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/uprobes.c

.. _`arch_uprobe_analyze_insn`:

arch_uprobe_analyze_insn
========================

.. c:function:: int arch_uprobe_analyze_insn(struct arch_uprobe *auprobe, struct mm_struct *mm, unsigned long addr)

    instruction analysis including validity and fixups.

    :param struct arch_uprobe \*auprobe:
        *undescribed*

    :param struct mm_struct \*mm:
        the probed address space.

    :param unsigned long addr:
        virtual address at which to install the probepoint
        Return 0 on success or a -ve number on error.

.. This file was automatic generated / don't edit.

