.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kvm/inject_fault.c

.. _`kvm_inject_dabt`:

kvm_inject_dabt
===============

.. c:function:: void kvm_inject_dabt(struct kvm_vcpu *vcpu, unsigned long addr)

    inject a data abort into the guest

    :param vcpu:
        The VCPU to receive the undefined exception
    :type vcpu: struct kvm_vcpu \*

    :param addr:
        The address to report in the DFAR
    :type addr: unsigned long

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

    :param vcpu:
        The VCPU to receive the undefined exception
    :type vcpu: struct kvm_vcpu \*

    :param addr:
        The address to report in the DFAR
    :type addr: unsigned long

.. _`kvm_inject_pabt.description`:

Description
-----------

It is assumed that this code is called from the VCPU thread and that the
VCPU therefore is not currently executing guest code.

.. _`kvm_inject_undefined`:

kvm_inject_undefined
====================

.. c:function:: void kvm_inject_undefined(struct kvm_vcpu *vcpu)

    inject an undefined instruction into the guest

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_inject_undefined.description`:

Description
-----------

It is assumed that this code is called from the VCPU thread and that the
VCPU therefore is not currently executing guest code.

.. _`kvm_inject_vabt`:

kvm_inject_vabt
===============

.. c:function:: void kvm_inject_vabt(struct kvm_vcpu *vcpu)

    inject an async abort / SError into the guest

    :param vcpu:
        The VCPU to receive the exception
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_inject_vabt.description`:

Description
-----------

It is assumed that this code is called from the VCPU thread and that the
VCPU therefore is not currently executing guest code.

Systems with the RAS Extensions specify an imp-def ESR (ISV/IDS = 1) with
the remaining ISS all-zeros so that this error is not interpreted as an
uncategorized RAS error. Without the RAS Extensions we can't specify an ESR
value, so the CPU generates an imp-def value.

.. This file was automatic generated / don't edit.

