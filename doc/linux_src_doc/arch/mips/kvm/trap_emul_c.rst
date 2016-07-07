.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kvm/trap_emul.c

.. _`kvm_trap_emul_handle_msa_disabled`:

kvm_trap_emul_handle_msa_disabled
=================================

.. c:function:: int kvm_trap_emul_handle_msa_disabled(struct kvm_vcpu *vcpu)

    Guest used MSA while disabled in root.

    :param struct kvm_vcpu \*vcpu:
        Virtual CPU context.

.. _`kvm_trap_emul_handle_msa_disabled.description`:

Description
-----------

Handle when the guest attempts to use MSA when it is disabled.

.. This file was automatic generated / don't edit.

