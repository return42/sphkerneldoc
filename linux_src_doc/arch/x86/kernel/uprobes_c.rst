.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/uprobes.c

.. _`arch_uprobe_analyze_insn`:

arch_uprobe_analyze_insn
========================

.. c:function:: int arch_uprobe_analyze_insn(struct arch_uprobe *auprobe, struct mm_struct *mm, unsigned long addr)

    instruction analysis including validity and fixups.

    :param auprobe:
        *undescribed*
    :type auprobe: struct arch_uprobe \*

    :param mm:
        the probed address space.
    :type mm: struct mm_struct \*

    :param addr:
        virtual address at which to install the probepoint
        Return 0 on success or a -ve number on error.
    :type addr: unsigned long

.. This file was automatic generated / don't edit.

