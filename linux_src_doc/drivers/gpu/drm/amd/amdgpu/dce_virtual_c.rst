.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/dce_virtual.c

.. _`dce_virtual_bandwidth_update`:

dce_virtual_bandwidth_update
============================

.. c:function:: void dce_virtual_bandwidth_update(struct amdgpu_device *adev)

    program display watermarks

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`dce_virtual_bandwidth_update.description`:

Description
-----------

Calculate and program the display watermarks and line
buffer allocation (CIK).

.. This file was automatic generated / don't edit.

