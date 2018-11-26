.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/kvm/vsie.c

.. _`setup_apcb00`:

setup_apcb00
============

.. c:function:: int setup_apcb00(struct kvm_vcpu *vcpu, unsigned long *apcb_s, unsigned long apcb_o, unsigned long *apcb_h)

    Copy to APCB FORMAT0 from APCB FORMAT0

    :param vcpu:
        pointer to the virtual CPU
    :type vcpu: struct kvm_vcpu \*

    :param apcb_s:
        pointer to start of apcb in the shadow crycb
    :type apcb_s: unsigned long \*

    :param apcb_o:
        pointer to start of original apcb in the guest2
    :type apcb_o: unsigned long

    :param apcb_h:
        pointer to start of apcb in the guest1
    :type apcb_h: unsigned long \*

.. _`setup_apcb00.description`:

Description
-----------

Returns 0 and -EFAULT on error reading guest apcb

.. _`setup_apcb11`:

setup_apcb11
============

.. c:function:: int setup_apcb11(struct kvm_vcpu *vcpu, unsigned long *apcb_s, unsigned long apcb_o, unsigned long *apcb_h)

    Copy the FORMAT1 APCB from the guest to the shadow CRYCB

    :param vcpu:
        pointer to the virtual CPU
    :type vcpu: struct kvm_vcpu \*

    :param apcb_s:
        pointer to start of apcb in the shadow crycb
    :type apcb_s: unsigned long \*

    :param apcb_o:
        pointer to start of original guest apcb
    :type apcb_o: unsigned long

    :param apcb_h:
        pointer to start of apcb in the host
    :type apcb_h: unsigned long \*

.. _`setup_apcb11.description`:

Description
-----------

Returns 0 and -EFAULT on error reading guest apcb

.. _`setup_apcb`:

setup_apcb
==========

.. c:function:: int setup_apcb(struct kvm_vcpu *vcpu, struct kvm_s390_crypto_cb *crycb_s, const u32 crycb_o, struct kvm_s390_crypto_cb *crycb_h, int fmt_o, int fmt_h)

    Create a shadow copy of the apcb.

    :param vcpu:
        pointer to the virtual CPU
    :type vcpu: struct kvm_vcpu \*

    :param crycb_s:
        pointer to shadow crycb
    :type crycb_s: struct kvm_s390_crypto_cb \*

    :param crycb_o:
        pointer to original guest crycb
    :type crycb_o: const u32

    :param crycb_h:
        pointer to the host crycb
    :type crycb_h: struct kvm_s390_crypto_cb \*

    :param fmt_o:
        format of the original guest crycb.
    :type fmt_o: int

    :param fmt_h:
        format of the host crycb.
    :type fmt_h: int

.. _`setup_apcb.description`:

Description
-----------

Checks the compatibility between the guest and host crycb and calls the
appropriate copy function.

Return 0 or an error number if the guest and host crycb are incompatible.

.. _`shadow_crycb`:

shadow_crycb
============

.. c:function:: int shadow_crycb(struct kvm_vcpu *vcpu, struct vsie_page *vsie_page)

    Create a shadow copy of the crycb block

    :param vcpu:
        a pointer to the virtual CPU
    :type vcpu: struct kvm_vcpu \*

    :param vsie_page:
        a pointer to internal date used for the vSIE
    :type vsie_page: struct vsie_page \*

.. _`shadow_crycb.description`:

Description
-----------

Create a shadow copy of the crycb block and setup key wrapping, if
requested for guest 3 and enabled for guest 2.

We accept format-1 or format-2, but we convert format-1 into format-2
in the shadow CRYCB.
Using format-2 enables the firmware to choose the right format when
scheduling the SIE.
There is nothing to do for format-0.

This function centralize the issuing of \ :c:func:`set_validity_icpt`\  for all
the subfunctions working on the crycb.

.. _`shadow_crycb.return`:

Return
------

- 0 if shadowed or nothing to do
- > 0 if control has to be given to guest 2

.. This file was automatic generated / don't edit.

