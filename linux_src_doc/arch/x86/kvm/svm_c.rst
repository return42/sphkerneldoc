.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kvm/svm.c

.. _`avic_init_access_page`:

avic_init_access_page
=====================

.. c:function:: int avic_init_access_page(struct kvm_vcpu *vcpu)

    AVIC hardware walks the nested page table to check permissions, but does not use the SPA address specified in the leaf page table entry since it uses  address in the AVIC_BACKING_PAGE pointer field of the VMCB. Therefore, we set up the APIC_ACCESS_PAGE_PRIVATE_MEMSLOT (4KB) here.

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

.. _`avic_set_running`:

avic_set_running
================

.. c:function:: void avic_set_running(struct kvm_vcpu *vcpu, bool is_run)

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

    :param is_run:
        *undescribed*
    :type is_run: bool

.. _`get_pi_vcpu_info`:

get_pi_vcpu_info
================

.. c:function:: int get_pi_vcpu_info(struct kvm *kvm, struct kvm_kernel_irq_routing_entry *e, struct vcpu_data *vcpu_info, struct vcpu_svm **svm)

    The HW cannot support posting multicast/broadcast interrupts to a vCPU. So, we still use legacy interrupt remapping for these kind of interrupts.

    :param kvm:
        *undescribed*
    :type kvm: struct kvm \*

    :param e:
        *undescribed*
    :type e: struct kvm_kernel_irq_routing_entry \*

    :param vcpu_info:
        *undescribed*
    :type vcpu_info: struct vcpu_data \*

    :param svm:
        *undescribed*
    :type svm: struct vcpu_svm \*\*

.. _`get_pi_vcpu_info.description`:

Description
-----------

For lowest-priority interrupts, we only support
those with single CPU as the destination, e.g. user
configures the interrupts via /proc/irq or uses
irqbalance to make the interrupts single-CPU.

.. This file was automatic generated / don't edit.

