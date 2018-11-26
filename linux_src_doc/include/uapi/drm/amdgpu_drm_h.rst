.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/drm/amdgpu_drm.h

.. _`memory-domains`:

memory domains
==============

\ ``AMDGPU_GEM_DOMAIN_CPU``\        System memory that is not GPU accessible.
Memory in this pool could be swapped out to disk if there is pressure.

\ ``AMDGPU_GEM_DOMAIN_GTT``\        GPU accessible system memory, mapped into the
GPU's virtual address space via gart. Gart memory linearizes non-contiguous
pages of system memory, allows GPU access system memory in a linezrized
fashion.

\ ``AMDGPU_GEM_DOMAIN_VRAM``\       Local video memory. For APUs, it is memory
carved out by the BIOS.

\ ``AMDGPU_GEM_DOMAIN_GDS``\        Global on-chip data storage used to share data
across shader threads.

\ ``AMDGPU_GEM_DOMAIN_GWS``\        Global wave sync, used to synchronize the
execution of all the waves on a device.

\ ``AMDGPU_GEM_DOMAIN_OA``\         Ordered append, used by 3D or Compute engines
for appending data.

.. _`amdgpu_ids_flags_fusion`:

AMDGPU_IDS_FLAGS_FUSION
=======================

.. c:function::  AMDGPU_IDS_FLAGS_FUSION()

    Flag that this is integrated (a.h.a. fusion) GPU

.. This file was automatic generated / don't edit.

