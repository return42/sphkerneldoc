.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/kvm/trap_emul.c

.. _`kvm_trap_emul_handle_msa_disabled`:

kvm_trap_emul_handle_msa_disabled
=================================

.. c:function:: int kvm_trap_emul_handle_msa_disabled(struct kvm_vcpu *vcpu)

    Guest used MSA while disabled in root.

    :param vcpu:
        Virtual CPU context.
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_trap_emul_handle_msa_disabled.description`:

Description
-----------

Handle when the guest attempts to use MSA when it is disabled.

.. _`kvm_trap_emul_gva_lockless_begin`:

kvm_trap_emul_gva_lockless_begin
================================

.. c:function:: void kvm_trap_emul_gva_lockless_begin(struct kvm_vcpu *vcpu)

    Begin lockless access to GVA space.

    :param vcpu:
        VCPU pointer.
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_trap_emul_gva_lockless_begin.description`:

Description
-----------

Call before a GVA space access outside of guest mode, to ensure that
asynchronous TLB flush requests are handled or delayed until completion of
the GVA access (as indicated by a matching \ :c:func:`kvm_trap_emul_gva_lockless_end`\ ).

Should be called with IRQs already enabled.

.. _`kvm_trap_emul_gva_lockless_end`:

kvm_trap_emul_gva_lockless_end
==============================

.. c:function:: void kvm_trap_emul_gva_lockless_end(struct kvm_vcpu *vcpu)

    End lockless access to GVA space.

    :param vcpu:
        VCPU pointer.
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_trap_emul_gva_lockless_end.description`:

Description
-----------

Called after a GVA space access outside of guest mode. Should have a matching
call to \ :c:func:`kvm_trap_emul_gva_lockless_begin`\ .

.. This file was automatic generated / don't edit.

