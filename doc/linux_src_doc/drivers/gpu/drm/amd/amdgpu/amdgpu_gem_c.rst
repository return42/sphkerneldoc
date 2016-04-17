.. -*- coding: utf-8; mode: rst -*-

============
amdgpu_gem.c
============


.. _`amdgpu_gem_timeout`:

amdgpu_gem_timeout
==================

.. c:function:: unsigned long amdgpu_gem_timeout (uint64_t timeout_ns)

    calculate jiffies timeout from absolute value

    :param uint64_t timeout_ns:
        timeout in ns



.. _`amdgpu_gem_timeout.description`:

Description
-----------

Calculate the timeout in jiffies from an absolute timeout in ns.



.. _`amdgpu_gem_va_update_vm`:

amdgpu_gem_va_update_vm
=======================

.. c:function:: void amdgpu_gem_va_update_vm (struct amdgpu_device *adev, struct amdgpu_bo_va *bo_va, uint32_t operation)

    update the bo_va in its VM

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_bo_va \*bo_va:
        bo_va to update

    :param uint32_t operation:

        *undescribed*



.. _`amdgpu_gem_va_update_vm.description`:

Description
-----------

Update the bo_va directly after setting it's address. Errors are not
vital here, so they are not reported back to userspace.

