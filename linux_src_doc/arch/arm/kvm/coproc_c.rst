.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kvm/coproc.c

.. _`kvm_handle_cp15_64`:

kvm_handle_cp15_64
==================

.. c:function:: int kvm_handle_cp15_64(struct kvm_vcpu *vcpu, struct kvm_run *run)

    - handles a mrrc/mcrr trap on a guest CP15 access

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

    :param run:
        The kvm_run struct
    :type run: struct kvm_run \*

.. _`kvm_handle_cp14_64`:

kvm_handle_cp14_64
==================

.. c:function:: int kvm_handle_cp14_64(struct kvm_vcpu *vcpu, struct kvm_run *run)

    - handles a mrrc/mcrr trap on a guest CP14 access

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

    :param run:
        The kvm_run struct
    :type run: struct kvm_run \*

.. _`kvm_handle_cp15_32`:

kvm_handle_cp15_32
==================

.. c:function:: int kvm_handle_cp15_32(struct kvm_vcpu *vcpu, struct kvm_run *run)

    - handles a mrc/mcr trap on a guest CP15 access

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

    :param run:
        The kvm_run struct
    :type run: struct kvm_run \*

.. _`kvm_handle_cp14_32`:

kvm_handle_cp14_32
==================

.. c:function:: int kvm_handle_cp14_32(struct kvm_vcpu *vcpu, struct kvm_run *run)

    - handles a mrc/mcr trap on a guest CP14 access

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

    :param run:
        The kvm_run struct
    :type run: struct kvm_run \*

.. _`kvm_reset_coprocs`:

kvm_reset_coprocs
=================

.. c:function:: void kvm_reset_coprocs(struct kvm_vcpu *vcpu)

    sets cp15 registers to reset value

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_reset_coprocs.description`:

Description
-----------

This function finds the right table above and sets the registers on the
virtual CPU struct to their architecturally defined reset values.

.. This file was automatic generated / don't edit.

