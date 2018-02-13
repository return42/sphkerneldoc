.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd.c

.. _`amdgpu_doorbell_get_kfd_info`:

amdgpu_doorbell_get_kfd_info
============================

.. c:function:: void amdgpu_doorbell_get_kfd_info(struct amdgpu_device *adev, phys_addr_t *aperture_base, size_t *aperture_size, size_t *start_offset)

    Report doorbell configuration required to setup amdkfd

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param phys_addr_t \*aperture_base:
        output returning doorbell aperture base physical address

    :param size_t \*aperture_size:
        output returning doorbell aperture size in bytes

    :param size_t \*start_offset:
        output returning # of doorbell bytes reserved for amdgpu.

.. _`amdgpu_doorbell_get_kfd_info.description`:

Description
-----------

amdgpu and amdkfd share the doorbell aperture. amdgpu sets it up,
takes doorbells required for its own rings and reports the setup to amdkfd.
amdgpu reserved doorbells are at the start of the doorbell aperture.

.. This file was automatic generated / don't edit.

