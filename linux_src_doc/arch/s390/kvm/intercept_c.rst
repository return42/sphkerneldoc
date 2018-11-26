.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/kvm/intercept.c

.. _`handle_external_interrupt`:

handle_external_interrupt
=========================

.. c:function:: int handle_external_interrupt(struct kvm_vcpu *vcpu)

    used for external interruption interceptions

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

.. _`handle_external_interrupt.description`:

Description
-----------

This interception only occurs if the CPUSTAT_EXT_INT bit was set, or if
the new PSW does not have external interrupts disabled. In the first case,
we've got to deliver the interrupt manually, and in the second case, we
drop to userspace to handle the situation there.

.. _`handle_mvpg_pei`:

handle_mvpg_pei
===============

.. c:function:: int handle_mvpg_pei(struct kvm_vcpu *vcpu)

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

.. _`handle_mvpg_pei.description`:

Description
-----------

This interception can only happen for guests with DAT disabled and
addresses that are currently not mapped in the host. Thus we try to
set up the mappings for the corresponding user pages here (or throw
addressing exceptions in case of illegal guest addresses).

.. This file was automatic generated / don't edit.

