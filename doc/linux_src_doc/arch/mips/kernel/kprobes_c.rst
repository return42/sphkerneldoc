.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kernel/kprobes.c

.. _`evaluate_branch_instruction`:

evaluate_branch_instruction
===========================

.. c:function:: int evaluate_branch_instruction(struct kprobe *p, struct pt_regs *regs, struct kprobe_ctlblk *kcb)

    :param struct kprobe \*p:
        *undescribed*

    :param struct pt_regs \*regs:
        *undescribed*

    :param struct kprobe_ctlblk \*kcb:
        *undescribed*

.. _`evaluate_branch_instruction.description`:

Description
-----------

Evaluate the branch instruction at probed address during probe hit. The
result of evaluation would be the updated epc. The insturction in delayslot
would actually be single stepped using a normal breakpoint) on SSOL slot.

The result is also saved in the kprobe control block for later use,
in case we need to execute the delayslot instruction. The latter will be
false for NOP instruction in dealyslot and the branch-likely instructions
when the branch is taken. And for those cases we set a flag as
SKIP_DELAYSLOT in the kprobe control block

.. This file was automatic generated / don't edit.

