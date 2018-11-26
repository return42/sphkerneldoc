.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kvm/sys_regs.c

.. _`kvm_handle_cp_64`:

kvm_handle_cp_64
================

.. c:function:: int kvm_handle_cp_64(struct kvm_vcpu *vcpu, const struct sys_reg_desc *global, size_t nr_global, const struct sys_reg_desc *target_specific, size_t nr_specific)

    - handles a mrrc/mcrr trap on a guest CP14/CP15 access

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

    :param global:
        *undescribed*
    :type global: const struct sys_reg_desc \*

    :param nr_global:
        *undescribed*
    :type nr_global: size_t

    :param target_specific:
        *undescribed*
    :type target_specific: const struct sys_reg_desc \*

    :param nr_specific:
        *undescribed*
    :type nr_specific: size_t

.. _`kvm_handle_cp_32`:

kvm_handle_cp_32
================

.. c:function:: int kvm_handle_cp_32(struct kvm_vcpu *vcpu, const struct sys_reg_desc *global, size_t nr_global, const struct sys_reg_desc *target_specific, size_t nr_specific)

    - handles a mrc/mcr trap on a guest CP14/CP15 access

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

    :param global:
        *undescribed*
    :type global: const struct sys_reg_desc \*

    :param nr_global:
        *undescribed*
    :type nr_global: size_t

    :param target_specific:
        *undescribed*
    :type target_specific: const struct sys_reg_desc \*

    :param nr_specific:
        *undescribed*
    :type nr_specific: size_t

.. _`kvm_handle_sys_reg`:

kvm_handle_sys_reg
==================

.. c:function:: int kvm_handle_sys_reg(struct kvm_vcpu *vcpu, struct kvm_run *run)

    - handles a mrs/msr trap on a guest sys_reg access

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

    :param run:
        The kvm_run struct
    :type run: struct kvm_run \*

.. _`kvm_reset_sys_regs`:

kvm_reset_sys_regs
==================

.. c:function:: void kvm_reset_sys_regs(struct kvm_vcpu *vcpu)

    sets system registers to reset value

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_reset_sys_regs.description`:

Description
-----------

This function finds the right table above and sets the registers on the
virtual CPU struct to their architecturally defined reset values.

.. This file was automatic generated / don't edit.

