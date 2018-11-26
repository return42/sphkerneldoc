.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_bios.c

.. _`amdgpu_atrm_call`:

amdgpu_atrm_call
================

.. c:function:: int amdgpu_atrm_call(acpi_handle atrm_handle, uint8_t *bios, int offset, int len)

    fetch a chunk of the vbios

    :param atrm_handle:
        acpi ATRM handle
    :type atrm_handle: acpi_handle

    :param bios:
        vbios image pointer
    :type bios: uint8_t \*

    :param offset:
        offset of vbios image data to fetch
    :type offset: int

    :param len:
        length of vbios image data to fetch
    :type len: int

.. _`amdgpu_atrm_call.description`:

Description
-----------

Executes ATRM to fetch a chunk of the discrete
vbios image on PX systems (all asics).
Returns the length of the buffer fetched.

.. This file was automatic generated / don't edit.

