.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kvm/emulate.c

.. _`kvm_adjust_itstate`:

kvm_adjust_itstate
==================

.. c:function:: void kvm_adjust_itstate(struct kvm_vcpu *vcpu)

    adjust ITSTATE when emulating instructions in IT-block

    :param struct kvm_vcpu \*vcpu:
        The VCPU pointer

.. _`kvm_adjust_itstate.description`:

Description
-----------

When exceptions occur while instructions are executed in Thumb IF-THEN
blocks, the ITSTATE field of the CPSR is not advanved (updated), so we have
to do this little bit of work manually. The fields map like this:

IT[7:0] -> CPSR[26:25],CPSR[15:10]

.. _`kvm_skip_instr`:

kvm_skip_instr
==============

.. c:function:: void kvm_skip_instr(struct kvm_vcpu *vcpu, bool is_wide_instr)

    skip a trapped instruction and proceed to the next

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

    :param bool is_wide_instr:
        *undescribed*

.. _`kvm_inject_undefined`:

kvm_inject_undefined
====================

.. c:function:: void kvm_inject_undefined(struct kvm_vcpu *vcpu)

    inject an undefined exception into the guest

    :param struct kvm_vcpu \*vcpu:
        The VCPU to receive the undefined exception

.. _`kvm_inject_undefined.description`:

Description
-----------

It is assumed that this code is called from the VCPU thread and that the
VCPU therefore is not currently executing guest code.

Modelled after \ :c:func:`TakeUndefInstrException`\  pseudocode.

.. _`kvm_inject_dabt`:

kvm_inject_dabt
===============

.. c:function:: void kvm_inject_dabt(struct kvm_vcpu *vcpu, unsigned long addr)

    inject a data abort into the guest

    :param struct kvm_vcpu \*vcpu:
        The VCPU to receive the undefined exception

    :param unsigned long addr:
        The address to report in the DFAR

.. _`kvm_inject_dabt.description`:

Description
-----------

It is assumed that this code is called from the VCPU thread and that the
VCPU therefore is not currently executing guest code.

.. _`kvm_inject_pabt`:

kvm_inject_pabt
===============

.. c:function:: void kvm_inject_pabt(struct kvm_vcpu *vcpu, unsigned long addr)

    inject a prefetch abort into the guest

    :param struct kvm_vcpu \*vcpu:
        The VCPU to receive the undefined exception

    :param unsigned long addr:
        The address to report in the DFAR

.. _`kvm_inject_pabt.description`:

Description
-----------

It is assumed that this code is called from the VCPU thread and that the
VCPU therefore is not currently executing guest code.

.. This file was automatic generated / don't edit.

