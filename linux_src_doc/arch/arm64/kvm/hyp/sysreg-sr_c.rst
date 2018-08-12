.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kvm/hyp/sysreg-sr.c

.. _`kvm_vcpu_load_sysregs`:

kvm_vcpu_load_sysregs
=====================

.. c:function:: void kvm_vcpu_load_sysregs(struct kvm_vcpu *vcpu)

    Load guest system registers to the physical CPU

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

.. _`kvm_vcpu_load_sysregs.description`:

Description
-----------

Load system registers that do not affect the host's execution, for
example EL1 system registers on a VHE system where the host kernel
runs at EL2.  This function is called from KVM's \ :c:func:`vcpu_load`\  function
and loading system register state early avoids having to load them on
every entry to the VM.

.. _`kvm_vcpu_put_sysregs`:

kvm_vcpu_put_sysregs
====================

.. c:function:: void kvm_vcpu_put_sysregs(struct kvm_vcpu *vcpu)

    Restore host system registers to the physical CPU

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

.. _`kvm_vcpu_put_sysregs.description`:

Description
-----------

Save guest system registers that do not affect the host's execution, for
example EL1 system registers on a VHE system where the host kernel
runs at EL2.  This function is called from KVM's \ :c:func:`vcpu_put`\  function
and deferring saving system register state until we're no longer running the
VCPU avoids having to save them on every exit from the VM.

.. This file was automatic generated / don't edit.

