.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/aarch32.c

.. _`kvm_adjust_itstate`:

kvm_adjust_itstate
==================

.. c:function:: void __hyp_text kvm_adjust_itstate(struct kvm_vcpu *vcpu)

    adjust ITSTATE when emulating instructions in IT-block

    :param vcpu:
        The VCPU pointer
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_adjust_itstate.description`:

Description
-----------

When exceptions occur while instructions are executed in Thumb IF-THEN
blocks, the ITSTATE field of the CPSR is not advanced (updated), so we have
to do this little bit of work manually. The fields map like this:

IT[7:0] -> CPSR[26:25],CPSR[15:10]

.. _`kvm_skip_instr32`:

kvm_skip_instr32
================

.. c:function:: void __hyp_text kvm_skip_instr32(struct kvm_vcpu *vcpu, bool is_wide_instr)

    skip a trapped instruction and proceed to the next

    :param vcpu:
        The vcpu pointer
    :type vcpu: struct kvm_vcpu \*

    :param is_wide_instr:
        *undescribed*
    :type is_wide_instr: bool

.. This file was automatic generated / don't edit.

