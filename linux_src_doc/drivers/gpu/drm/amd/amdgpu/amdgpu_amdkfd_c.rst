.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd.c

.. _`amdgpu_doorbell_get_kfd_info`:

amdgpu_doorbell_get_kfd_info
============================

.. c:function:: void amdgpu_doorbell_get_kfd_info(struct amdgpu_device *adev, phys_addr_t *aperture_base, size_t *aperture_size, size_t *start_offset)

    Report doorbell configuration required to setup amdkfd

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

    :param aperture_base:
        output returning doorbell aperture base physical address
    :type aperture_base: phys_addr_t \*

    :param aperture_size:
        output returning doorbell aperture size in bytes
    :type aperture_size: size_t \*

    :param start_offset:
        output returning # of doorbell bytes reserved for amdgpu.
    :type start_offset: size_t \*

.. _`amdgpu_doorbell_get_kfd_info.description`:

Description
-----------

amdgpu and amdkfd share the doorbell aperture. amdgpu sets it up,
takes doorbells required for its own rings and reports the setup to amdkfd.
amdgpu reserved doorbells are at the start of the doorbell aperture.

.. This file was automatic generated / don't edit.

