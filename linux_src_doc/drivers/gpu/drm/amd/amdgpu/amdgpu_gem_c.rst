.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_gem.c

.. _`amdgpu_gem_timeout`:

amdgpu_gem_timeout
==================

.. c:function:: unsigned long amdgpu_gem_timeout(uint64_t timeout_ns)

    calculate jiffies timeout from absolute value

    :param timeout_ns:
        timeout in ns
    :type timeout_ns: uint64_t

.. _`amdgpu_gem_timeout.description`:

Description
-----------

Calculate the timeout in jiffies from an absolute timeout in ns.

.. _`amdgpu_gem_va_update_vm`:

amdgpu_gem_va_update_vm
=======================

.. c:function:: void amdgpu_gem_va_update_vm(struct amdgpu_device *adev, struct amdgpu_vm *vm, struct amdgpu_bo_va *bo_va, uint32_t operation)

    update the bo_va in its VM

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param vm:
        vm to update
    :type vm: struct amdgpu_vm \*

    :param bo_va:
        bo_va to update
    :type bo_va: struct amdgpu_bo_va \*

    :param operation:
        map, unmap or clear
    :type operation: uint32_t

.. _`amdgpu_gem_va_update_vm.description`:

Description
-----------

Update the bo_va directly after setting its address. Errors are not
vital here, so they are not reported back to userspace.

.. This file was automatic generated / don't edit.

