.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kvm/coproc.c

.. _`kvm_handle_cp15_64`:

kvm_handle_cp15_64
==================

.. c:function:: int kvm_handle_cp15_64(struct kvm_vcpu *vcpu, struct kvm_run *run)

    - handles a mrrc/mcrr trap on a guest CP15 access

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

    :param struct kvm_run \*run:
        The kvm_run struct

.. _`kvm_handle_cp15_32`:

kvm_handle_cp15_32
==================

.. c:function:: int kvm_handle_cp15_32(struct kvm_vcpu *vcpu, struct kvm_run *run)

    - handles a mrc/mcr trap on a guest CP15 access

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

    :param struct kvm_run \*run:
        The kvm_run struct

.. _`kvm_reset_coprocs`:

kvm_reset_coprocs
=================

.. c:function:: void kvm_reset_coprocs(struct kvm_vcpu *vcpu)

    sets cp15 registers to reset value

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

.. _`kvm_reset_coprocs.description`:

Description
-----------

This function finds the right table above and sets the registers on the
virtual CPU struct to their architecturally defined reset values.

.. This file was automatic generated / don't edit.

