.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kvm/booke.c

.. _`kvmppc_handle_exit`:

kvmppc_handle_exit
==================

.. c:function:: int kvmppc_handle_exit(struct kvm_run *run, struct kvm_vcpu *vcpu, unsigned int exit_nr)

    :param struct kvm_run \*run:
        *undescribed*

    :param struct kvm_vcpu \*vcpu:
        *undescribed*

    :param unsigned int exit_nr:
        *undescribed*

.. _`kvmppc_handle_exit.description`:

Description
-----------

Return value is in the form (errcode<<2 \| RESUME_FLAG_HOST \| RESUME_FLAG_NV)

.. This file was automatic generated / don't edit.

