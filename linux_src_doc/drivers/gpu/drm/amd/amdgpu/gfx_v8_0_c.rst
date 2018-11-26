.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/gfx_v8_0.c

.. _`default_sh_mem_bases`:

DEFAULT_SH_MEM_BASES
====================

.. c:function::  DEFAULT_SH_MEM_BASES()

    gart enable

.. _`default_sh_mem_bases.description`:

Description
-----------

Initialize compute vmid sh_mem registers

.. _`gfx_v8_0_get_gpu_clock_counter`:

gfx_v8_0_get_gpu_clock_counter
==============================

.. c:function:: uint64_t gfx_v8_0_get_gpu_clock_counter(struct amdgpu_device *adev)

    return GPU clock counter snapshot

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`gfx_v8_0_get_gpu_clock_counter.description`:

Description
-----------

Fetches a GPU clock counter snapshot.
Returns the 64 bit clock counter snapshot.

.. This file was automatic generated / don't edit.

