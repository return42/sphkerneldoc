.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm64/kvm/inject_fault.c

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

.. _`kvm_inject_undefined`:

kvm_inject_undefined
====================

.. c:function:: void kvm_inject_undefined(struct kvm_vcpu *vcpu)

    inject an undefined instruction into the guest

    :param struct kvm_vcpu \*vcpu:
        *undescribed*

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

    :param struct kvm_vcpu \*vcpu:
        The VCPU to receive the exception

.. _`kvm_inject_vabt.description`:

Description
-----------

It is assumed that this code is called from the VCPU thread and that the
VCPU therefore is not currently executing guest code.

.. This file was automatic generated / don't edit.

