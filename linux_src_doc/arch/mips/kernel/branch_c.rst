.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kernel/branch.c

.. _`__compute_return_epc_for_insn`:

__compute_return_epc_for_insn
=============================

.. c:function:: int __compute_return_epc_for_insn(struct pt_regs *regs, union mips_instruction insn)

    Computes the return address and do emulate branch simulation, if required.

    :param struct pt_regs \*regs:
        Pointer to pt_regs

    :param union mips_instruction insn:
        branch instruction to decode

.. _`__compute_return_epc_for_insn.mips-r6-compact-branches-and-forbidden-slots`:

MIPS R6 Compact branches and forbidden slots
--------------------------------------------

Compact branches do not throw exceptions because they do
not have delay slots. The forbidden slot instruction ($PC+4)
is only executed if the branch was not taken. Otherwise the
forbidden slot is skipped entirely. This means that the
only possible reason to be here because of a MIPS R6 compact
branch instruction is that the forbidden slot has thrown one.
In that case the branch was not taken, so the EPC can be safely
set to EPC + 8.

.. This file was automatic generated / don't edit.

