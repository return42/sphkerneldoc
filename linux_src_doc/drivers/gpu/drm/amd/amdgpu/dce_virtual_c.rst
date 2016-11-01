.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/dce_virtual.c

.. _`dce_virtual_vblank_wait`:

dce_virtual_vblank_wait
=======================

.. c:function:: void dce_virtual_vblank_wait(struct amdgpu_device *adev, int crtc)

    vblank wait asic callback.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param int crtc:
        crtc to wait for vblank on

.. _`dce_virtual_vblank_wait.description`:

Description
-----------

Wait for vblank on the requested crtc (evergreen+).

.. _`dce_virtual_bandwidth_update`:

dce_virtual_bandwidth_update
============================

.. c:function:: void dce_virtual_bandwidth_update(struct amdgpu_device *adev)

    program display watermarks

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`dce_virtual_bandwidth_update.description`:

Description
-----------

Calculate and program the display watermarks and line
buffer allocation (CIK).

.. This file was automatic generated / don't edit.

