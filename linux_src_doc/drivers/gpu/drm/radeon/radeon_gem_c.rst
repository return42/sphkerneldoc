.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_gem.c

.. _`radeon_gem_va_update_vm`:

radeon_gem_va_update_vm
=======================

.. c:function:: void radeon_gem_va_update_vm(struct radeon_device *rdev, struct radeon_bo_va *bo_va)

    update the bo_va in its VM

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param bo_va:
        bo_va to update
    :type bo_va: struct radeon_bo_va \*

.. _`radeon_gem_va_update_vm.description`:

Description
-----------

Update the bo_va directly after setting it's address. Errors are not
vital here, so they are not reported back to userspace.

.. This file was automatic generated / don't edit.

