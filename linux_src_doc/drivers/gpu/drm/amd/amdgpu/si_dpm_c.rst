.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/si_dpm.c

.. _`si_dpm_init_microcode`:

si_dpm_init_microcode
=====================

.. c:function:: int si_dpm_init_microcode(struct amdgpu_device *adev)

    load ucode images from disk

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`si_dpm_init_microcode.description`:

Description
-----------

Use the firmware interface to load the ucode images into
the driver (not loaded into hw).
Returns 0 on success, error on failure.

.. This file was automatic generated / don't edit.

