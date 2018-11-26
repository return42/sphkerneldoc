.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kvm/booke.c

.. _`kvmppc_handle_exit`:

kvmppc_handle_exit
==================

.. c:function:: int kvmppc_handle_exit(struct kvm_run *run, struct kvm_vcpu *vcpu, unsigned int exit_nr)

    :param run:
        *undescribed*
    :type run: struct kvm_run \*

    :param vcpu:
        *undescribed*
    :type vcpu: struct kvm_vcpu \*

    :param exit_nr:
        *undescribed*
    :type exit_nr: unsigned int

.. _`kvmppc_handle_exit.description`:

Description
-----------

Return value is in the form (errcode<<2 \| RESUME_FLAG_HOST \| RESUME_FLAG_NV)

.. This file was automatic generated / don't edit.

