.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_gpuvm.c

.. _`reserve_bo_and_vm`:

reserve_bo_and_vm
=================

.. c:function:: int reserve_bo_and_vm(struct kgd_mem *mem, struct amdgpu_vm *vm, struct bo_vm_reservation_context *ctx)

    reserve a BO and a VM unconditionally.

    :param struct kgd_mem \*mem:
        KFD BO structure.

    :param struct amdgpu_vm \*vm:
        the VM to reserve.

    :param struct bo_vm_reservation_context \*ctx:
        the struct that will be used in \ :c:func:`unreserve_bo_and_vms`\ .

.. _`reserve_bo_and_cond_vms`:

reserve_bo_and_cond_vms
=======================

.. c:function:: int reserve_bo_and_cond_vms(struct kgd_mem *mem, struct amdgpu_vm *vm, enum bo_vm_match map_type, struct bo_vm_reservation_context *ctx)

    reserve a BO and some VMs conditionally

    :param struct kgd_mem \*mem:
        KFD BO structure.

    :param struct amdgpu_vm \*vm:
        the VM to reserve. If NULL, then all VMs associated with the BO
        is used. Otherwise, a single VM associated with the BO.

    :param enum bo_vm_match map_type:
        the mapping status that will be used to filter the VMs.

    :param struct bo_vm_reservation_context \*ctx:
        the struct that will be used in \ :c:func:`unreserve_bo_and_vms`\ .

.. _`reserve_bo_and_cond_vms.description`:

Description
-----------

Returns 0 for success, negative for failure.

.. _`unreserve_bo_and_vms`:

unreserve_bo_and_vms
====================

.. c:function:: int unreserve_bo_and_vms(struct bo_vm_reservation_context *ctx, bool wait, bool intr)

    Unreserve BO and VMs from a reservation context

    :param struct bo_vm_reservation_context \*ctx:
        Reservation context to unreserve

    :param bool wait:
        Optionally wait for a sync object representing pending VM updates

    :param bool intr:
        Whether the wait is interruptible

.. _`unreserve_bo_and_vms.description`:

Description
-----------

Also frees any resources allocated in
reserve_bo_and_(cond_)vm(s). Returns the status from
amdgpu_sync_wait.

.. This file was automatic generated / don't edit.

