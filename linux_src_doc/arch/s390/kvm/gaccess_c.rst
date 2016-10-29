.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/kvm/gaccess.c

.. _`guest_translate`:

guest_translate
===============

.. c:function:: unsigned long guest_translate(struct kvm_vcpu *vcpu, unsigned long gva, unsigned long *gpa, const union asce asce, enum gacc_mode mode)

    translate a guest virtual into a guest absolute address

    :param struct kvm_vcpu \*vcpu:
        virtual cpu

    :param unsigned long gva:
        guest virtual address

    :param unsigned long \*gpa:
        points to where guest physical (absolute) address should be stored

    :param const union asce asce:
        effective asce

    :param enum gacc_mode mode:
        indicates the access mode to be used

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

.. c:function:: int guest_translate_address(struct kvm_vcpu *vcpu, unsigned long gva, ar_t ar, unsigned long *gpa, enum gacc_mode mode)

    translate guest logical into guest absolute address

    :param struct kvm_vcpu \*vcpu:
        *undescribed*

    :param unsigned long gva:
        *undescribed*

    :param ar_t ar:
        *undescribed*

    :param unsigned long \*gpa:
        *undescribed*

    :param enum gacc_mode mode:
        *undescribed*

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

.. c:function:: int check_gva_range(struct kvm_vcpu *vcpu, unsigned long gva, ar_t ar, unsigned long length, enum gacc_mode mode)

    test a range of guest virtual addresses for accessibility

    :param struct kvm_vcpu \*vcpu:
        *undescribed*

    :param unsigned long gva:
        *undescribed*

    :param ar_t ar:
        *undescribed*

    :param unsigned long length:
        *undescribed*

    :param enum gacc_mode mode:
        *undescribed*

.. _`kvm_s390_check_low_addr_prot_real`:

kvm_s390_check_low_addr_prot_real
=================================

.. c:function:: int kvm_s390_check_low_addr_prot_real(struct kvm_vcpu *vcpu, unsigned long gra)

    check for low-address protection

    :param struct kvm_vcpu \*vcpu:
        *undescribed*

    :param unsigned long gra:
        Guest real address

.. _`kvm_s390_check_low_addr_prot_real.description`:

Description
-----------

Checks whether an address is subject to low-address protection and set
up vcpu->arch.pgm accordingly if necessary.

.. _`kvm_s390_check_low_addr_prot_real.return`:

Return
------

0 if no protection exception, or PGM_PROTECTION if protected.

.. This file was automatic generated / don't edit.
