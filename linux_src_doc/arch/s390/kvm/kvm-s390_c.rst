.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/kvm/kvm-s390.c

.. _`kvm_arch_fault_in_page`:

kvm_arch_fault_in_page
======================

.. c:function:: long kvm_arch_fault_in_page(struct kvm_vcpu *vcpu, gpa_t gpa, int writable)

    fault-in guest page if necessary

    :param struct kvm_vcpu \*vcpu:
        The corresponding virtual cpu

    :param gpa_t gpa:
        Guest physical address

    :param int writable:
        Whether the page should be writable or not

.. _`kvm_arch_fault_in_page.description`:

Description
-----------

Make sure that a guest page has been faulted-in on the host.

.. _`kvm_arch_fault_in_page.return`:

Return
------

Zero on success, negative error code otherwise.

.. This file was automatic generated / don't edit.

