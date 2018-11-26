.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/kvm/gaccess.c

.. _`guest_translate`:

guest_translate
===============

.. c:function:: unsigned long guest_translate(struct kvm_vcpu *vcpu, unsigned long gva, unsigned long *gpa, const union asce asce, enum gacc_mode mode, enum prot_type *prot)

    translate a guest virtual into a guest absolute address

    :param vcpu:
        virtual cpu
    :type vcpu: struct kvm_vcpu \*

    :param gva:
        guest virtual address
    :type gva: unsigned long

    :param gpa:
        points to where guest physical (absolute) address should be stored
    :type gpa: unsigned long \*

    :param asce:
        effective asce
    :type asce: const union asce

    :param mode:
        indicates the access mode to be used
    :type mode: enum gacc_mode

    :param prot:
        returns the type for protection exceptions
    :type prot: enum prot_type \*

.. _`guest_translate.description`:

Description
-----------

Translate a guest virtual address into a guest absolute address by means
of dynamic address translation as specified by the architecture.
If the resulting absolute address is not available in the configuration
an addressing exception is indicated and \ ``gpa``\  will not be changed.

.. _`guest_translate.return`:

Return
------

- zero on success; \ ``gpa``\  contains the resulting absolute address
- a negative value if guest access failed due to e.g. broken
guest mapping
- a positve value if an access exception happened. In this case
the returned value is the program interruption code as defined
by the architecture

.. _`guest_translate_address`:

guest_translate_address
=======================

.. c:function:: int guest_translate_address(struct kvm_vcpu *vcpu, unsigned long gva, u8 ar, unsigned long *gpa, enum gacc_mode mode)

    translate guest logical into guest absolute address

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

    :param gva:
        *undescribed*
    :type gva: unsigned long

    :param ar:
        *undescribed*
    :type ar: u8

    :param gpa:
        *undescribed*
    :type gpa: unsigned long \*

    :param mode:
        *undescribed*
    :type mode: enum gacc_mode

.. _`guest_translate_address.description`:

Description
-----------

Parameter semantics are the same as the ones from guest_translate.
The memory contents at the guest address are not changed.

.. _`guest_translate_address.note`:

Note
----

The IPTE lock is not taken during this function, so the caller
has to take care of this.

.. _`check_gva_range`:

check_gva_range
===============

.. c:function:: int check_gva_range(struct kvm_vcpu *vcpu, unsigned long gva, u8 ar, unsigned long length, enum gacc_mode mode)

    test a range of guest virtual addresses for accessibility

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

    :param gva:
        *undescribed*
    :type gva: unsigned long

    :param ar:
        *undescribed*
    :type ar: u8

    :param length:
        *undescribed*
    :type length: unsigned long

    :param mode:
        *undescribed*
    :type mode: enum gacc_mode

.. _`kvm_s390_check_low_addr_prot_real`:

kvm_s390_check_low_addr_prot_real
=================================

.. c:function:: int kvm_s390_check_low_addr_prot_real(struct kvm_vcpu *vcpu, unsigned long gra)

    check for low-address protection

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

    :param gra:
        Guest real address
    :type gra: unsigned long

.. _`kvm_s390_check_low_addr_prot_real.description`:

Description
-----------

Checks whether an address is subject to low-address protection and set
up vcpu->arch.pgm accordingly if necessary.

.. _`kvm_s390_check_low_addr_prot_real.return`:

Return
------

0 if no protection exception, or PGM_PROTECTION if protected.

.. _`kvm_s390_shadow_tables`:

kvm_s390_shadow_tables
======================

.. c:function:: int kvm_s390_shadow_tables(struct gmap *sg, unsigned long saddr, unsigned long *pgt, int *dat_protection, int *fake)

    walk the guest page table and create shadow tables

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param saddr:
        faulting address in the shadow gmap
    :type saddr: unsigned long

    :param pgt:
        pointer to the page table address result
    :type pgt: unsigned long \*

    :param dat_protection:
        *undescribed*
    :type dat_protection: int \*

    :param fake:
        pgt references contiguous guest memory block, not a pgtable
    :type fake: int \*

.. _`kvm_s390_shadow_fault`:

kvm_s390_shadow_fault
=====================

.. c:function:: int kvm_s390_shadow_fault(struct kvm_vcpu *vcpu, struct gmap *sg, unsigned long saddr)

    handle fault on a shadow page table

    :param vcpu:
        virtual cpu
    :type vcpu: struct kvm_vcpu \*

    :param sg:
        pointer to the shadow guest address space structure
    :type sg: struct gmap \*

    :param saddr:
        faulting address in the shadow gmap
    :type saddr: unsigned long

.. _`kvm_s390_shadow_fault.return`:

Return
------

- 0 if the shadow fault was successfully resolved
- > 0 (pgm exception code) on exceptions while faulting
- -EAGAIN if the caller can retry immediately
- -EFAULT when accessing invalid guest addresses
- -ENOMEM if out of memory

.. This file was automatic generated / don't edit.

