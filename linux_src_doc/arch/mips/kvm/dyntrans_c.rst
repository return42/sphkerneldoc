.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kvm/dyntrans.c

.. _`kvm_mips_trans_replace`:

kvm_mips_trans_replace
======================

.. c:function:: int kvm_mips_trans_replace(struct kvm_vcpu *vcpu, u32 *opc, union mips_instruction replace)

    Replace trapping instruction in guest memory.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU.

    :param u32 \*opc:
        PC of instruction to replace.

    :param union mips_instruction replace:
        Instruction to write

.. This file was automatic generated / don't edit.

