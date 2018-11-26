.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kvm/debug.c

.. _`save_guest_debug_regs`:

save_guest_debug_regs
=====================

.. c:function:: void save_guest_debug_regs(struct kvm_vcpu *vcpu)

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

.. _`save_guest_debug_regs.description`:

Description
-----------

For some debug operations we need to tweak some guest registers. As
a result we need to save the state of those registers before we
make those modifications.

Guest access to MDSCR_EL1 is trapped by the hypervisor and handled
after we have restored the preserved value to the main context.

.. _`kvm_arm_init_debug`:

kvm_arm_init_debug
==================

.. c:function:: void kvm_arm_init_debug( void)

    grab what we need for debug

    :param void:
        no arguments
    :type void: 

.. _`kvm_arm_init_debug.description`:

Description
-----------

Currently the sole task of this function is to retrieve the initial
value of mdcr_el2 so we can preserve MDCR_EL2.HPMN which has
presumably been set-up by some knowledgeable bootcode.

It is called once per-cpu during CPU hyp initialisation.

.. _`kvm_arm_reset_debug_ptr`:

kvm_arm_reset_debug_ptr
=======================

.. c:function:: void kvm_arm_reset_debug_ptr(struct kvm_vcpu *vcpu)

    reset the debug ptr to point to the vcpu state

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_arm_setup_debug`:

kvm_arm_setup_debug
===================

.. c:function:: void kvm_arm_setup_debug(struct kvm_vcpu *vcpu)

    set up debug related stuff

    :param vcpu:
        the vcpu pointer
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_arm_setup_debug.description`:

Description
-----------

This is called before each entry into the hypervisor to setup any
debug related registers. Currently this just ensures we will trap

.. _`kvm_arm_setup_debug.access-to`:

access to
---------

- Performance monitors (MDCR_EL2_TPM/MDCR_EL2_TPMCR)
- Debug ROM Address (MDCR_EL2_TDRA)
- OS related registers (MDCR_EL2_TDOSA)
- Statistical profiler (MDCR_EL2_TPMS/MDCR_EL2_E2PB)

Additionally, KVM only traps guest accesses to the debug registers if
the guest is not actively using them (see the KVM_ARM64_DEBUG_DIRTY
flag on vcpu->arch.flags).  Since the guest must not interfere
with the hardware state when debugging the guest, we must ensure that
trapping is enabled whenever we are debugging the guest using the
debug registers.

.. This file was automatic generated / don't edit.

