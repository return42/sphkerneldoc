.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/include/asm/kvm_host.h

.. _`kvm_mips_flush`:

enum kvm_mips_flush
===================

.. c:type:: enum kvm_mips_flush

    Types of MMU flushes.

.. _`kvm_mips_flush.definition`:

Definition
----------

.. code-block:: c

    enum kvm_mips_flush {
        KMF_USER,
        KMF_KERN,
        KMF_GPA
    };

.. _`kvm_mips_flush.constants`:

Constants
---------

KMF_USER
    Flush guest user virtual memory mappings.
    Guest USeg only.

KMF_KERN
    Flush guest kernel virtual memory mappings.
    Guest USeg and KSeg2/3.

KMF_GPA
    Flush guest physical memory mappings.
    Also includes KSeg0 if KMF_KERN is set.

.. _`kvm_is_ifetch_fault`:

kvm_is_ifetch_fault
===================

.. c:function:: bool kvm_is_ifetch_fault(struct kvm_vcpu_arch *vcpu)

    Find whether a TLBL exception is due to ifetch fault.

    :param vcpu:
        Virtual CPU.
    :type vcpu: struct kvm_vcpu_arch \*

.. _`kvm_is_ifetch_fault.return`:

Return
------

Whether the TLBL exception was likely due to an instruction
fetch fault rather than a data load fault.

.. This file was automatic generated / don't edit.

