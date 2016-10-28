.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/arch_timer.c

.. _`kvm_timer_flush_hwstate`:

kvm_timer_flush_hwstate
=======================

.. c:function:: void kvm_timer_flush_hwstate(struct kvm_vcpu *vcpu)

    prepare to move the virt timer to the cpu

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

.. _`kvm_timer_flush_hwstate.description`:

Description
-----------

Check if the virtual timer has expired while we were running in the host,
and inject an interrupt if that was the case.

.. _`kvm_timer_sync_hwstate`:

kvm_timer_sync_hwstate
======================

.. c:function:: void kvm_timer_sync_hwstate(struct kvm_vcpu *vcpu)

    sync timer state from cpu

    :param struct kvm_vcpu \*vcpu:
        The vcpu pointer

.. _`kvm_timer_sync_hwstate.description`:

Description
-----------

Check if the virtual timer has expired while we were running in the guest,
and inject an interrupt if that was the case.

.. This file was automatic generated / don't edit.

