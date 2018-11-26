.. -*- coding: utf-8; mode: rst -*-
.. src-file: virt/kvm/arm/psci.c

.. _`kvm_psci_call`:

kvm_psci_call
=============

.. c:function:: int kvm_psci_call(struct kvm_vcpu *vcpu)

    handle PSCI call if r0 value is in range

    :param vcpu:
        Pointer to the VCPU struct
    :type vcpu: struct kvm_vcpu \*

.. _`kvm_psci_call.description`:

Description
-----------

Handle PSCI calls from guests through traps from HVC instructions.
The calling convention is similar to SMC calls to the secure world
where the function number is placed in r0.

.. _`kvm_psci_call.this-function-returns`:

This function returns
---------------------

> 0 (success), 0 (success but exit to user
space), and < 0 (errors)

.. _`kvm_psci_call.errors`:

Errors
------

-EINVAL: Unrecognized PSCI function

.. This file was automatic generated / don't edit.

