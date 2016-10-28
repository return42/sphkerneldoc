.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kvm/svm.c

.. _`avic_init_access_page`:

avic_init_access_page
=====================

.. c:function:: int avic_init_access_page(struct kvm_vcpu *vcpu)

    AVIC hardware walks the nested page table to check permissions, but does not use the SPA address specified in the leaf page table entry since it uses  address in the AVIC_BACKING_PAGE pointer field of the VMCB. Therefore, we set up the APIC_ACCESS_PAGE_PRIVATE_MEMSLOT (4KB) here.

    :param struct kvm_vcpu \*vcpu:
        *undescribed*

.. _`avic_set_running`:

avic_set_running
================

.. c:function:: void avic_set_running(struct kvm_vcpu *vcpu, bool is_run)

    :param struct kvm_vcpu \*vcpu:
        *undescribed*

    :param bool is_run:
        *undescribed*

.. This file was automatic generated / don't edit.

