.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kvm/dyntrans.c

.. _`kvm_mips_trans_replace`:

kvm_mips_trans_replace
======================

.. c:function:: int kvm_mips_trans_replace(struct kvm_vcpu *vcpu, u32 *opc, union mips_instruction replace)

    Replace trapping instruction in guest memory.

    :param vcpu:
        Virtual CPU.
    :type vcpu: struct kvm_vcpu \*

    :param opc:
        PC of instruction to replace.
    :type opc: u32 \*

    :param replace:
        Instruction to write
    :type replace: union mips_instruction

.. This file was automatic generated / don't edit.

