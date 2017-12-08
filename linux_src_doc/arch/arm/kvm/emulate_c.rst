.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/kvm/emulate.c

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

