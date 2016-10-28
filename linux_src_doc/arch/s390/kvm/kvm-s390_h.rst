.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/kvm/kvm-s390.h

.. _`kvm_s390_inject_prog_cond`:

kvm_s390_inject_prog_cond
=========================

.. c:function:: int kvm_s390_inject_prog_cond(struct kvm_vcpu *vcpu, int rc)

    conditionally inject a program check

    :param struct kvm_vcpu \*vcpu:
        virtual cpu

    :param int rc:
        original return/error code

.. _`kvm_s390_inject_prog_cond.description`:

Description
-----------

This function is supposed to be used after regular guest access functions
failed, to conditionally inject a program check to a vcpu. The typical
pattern would look like

rc = write_guest(vcpu, addr, data, len);
if (rc)
return kvm_s390_inject_prog_cond(vcpu, rc);

A negative return code from guest access functions implies an internal error
like e.g. out of memory. In these cases no program check should be injected
to the guest.
A positive value implies that an exception happened while accessing a guest's
memory. In this case all data belonging to the corresponding program check
has been stored in vcpu->arch.pgm and can be injected with
\ :c:func:`kvm_s390_inject_prog_irq`\ .

.. _`kvm_s390_inject_prog_cond.return`:

Return
------

- the original \ ``rc``\  value if \ ``rc``\  was negative (internal error)
- zero if \ ``rc``\  was already zero
- zero or error code from injecting if \ ``rc``\  was positive
(program check injected to \ ``vcpu``\ )

.. This file was automatic generated / don't edit.

