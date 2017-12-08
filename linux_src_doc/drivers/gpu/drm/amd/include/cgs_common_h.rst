.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/include/cgs_common.h

.. _`cgs_gpu_mem_type`:

enum cgs_gpu_mem_type
=====================

.. c:type:: enum cgs_gpu_mem_type

    GPU memory types

.. _`cgs_gpu_mem_type.definition`:

Definition
----------

.. code-block:: c

    enum cgs_gpu_mem_type {
        CGS_GPU_MEM_TYPE__VISIBLE_FB,
        CGS_GPU_MEM_TYPE__INVISIBLE_FB,
        CGS_GPU_MEM_TYPE__VISIBLE_CONTIG_FB,
        CGS_GPU_MEM_TYPE__INVISIBLE_CONTIG_FB,
        CGS_GPU_MEM_TYPE__GART_CACHEABLE,
        CGS_GPU_MEM_TYPE__GART_WRITECOMBINE
    };

.. _`cgs_gpu_mem_type.constants`:

Constants
---------

CGS_GPU_MEM_TYPE__VISIBLE_FB
    *undescribed*

CGS_GPU_MEM_TYPE__INVISIBLE_FB
    *undescribed*

CGS_GPU_MEM_TYPE__VISIBLE_CONTIG_FB
    *undescribed*

CGS_GPU_MEM_TYPE__INVISIBLE_CONTIG_FB
    *undescribed*

CGS_GPU_MEM_TYPE__GART_CACHEABLE
    *undescribed*

CGS_GPU_MEM_TYPE__GART_WRITECOMBINE
    *undescribed*

.. _`cgs_ind_reg`:

enum cgs_ind_reg
================

.. c:type:: enum cgs_ind_reg

    Indirect register spaces

.. _`cgs_ind_reg.definition`:

Definition
----------

.. code-block:: c

    enum cgs_ind_reg {
        CGS_IND_REG__MMIO,
        CGS_IND_REG__PCIE,
        CGS_IND_REG__SMC,
        CGS_IND_REG__UVD_CTX,
        CGS_IND_REG__DIDT,
        CGS_IND_REG_GC_CAC,
        CGS_IND_REG_SE_CAC,
        CGS_IND_REG__AUDIO_ENDPT
    };

.. _`cgs_ind_reg.constants`:

Constants
---------

CGS_IND_REG__MMIO
    *undescribed*

CGS_IND_REG__PCIE
    *undescribed*

CGS_IND_REG__SMC
    *undescribed*

CGS_IND_REG__UVD_CTX
    *undescribed*

CGS_IND_REG__DIDT
    *undescribed*

CGS_IND_REG_GC_CAC
    *undescribed*

CGS_IND_REG_SE_CAC
    *undescribed*

CGS_IND_REG__AUDIO_ENDPT
    *undescribed*

.. _`cgs_engine`:

enum cgs_engine
===============

.. c:type:: enum cgs_engine

    Engines that can be statically power-gated

.. _`cgs_engine.definition`:

Definition
----------

.. code-block:: c

    enum cgs_engine {
        CGS_ENGINE__UVD,
        CGS_ENGINE__VCE,
        CGS_ENGINE__VP8,
        CGS_ENGINE__ACP_DMA,
        CGS_ENGINE__ACP_DSP0,
        CGS_ENGINE__ACP_DSP1,
        CGS_ENGINE__ISP
    };

.. _`cgs_engine.constants`:

Constants
---------

CGS_ENGINE__UVD
    *undescribed*

CGS_ENGINE__VCE
    *undescribed*

CGS_ENGINE__VP8
    *undescribed*

CGS_ENGINE__ACP_DMA
    *undescribed*

CGS_ENGINE__ACP_DSP0
    *undescribed*

CGS_ENGINE__ACP_DSP1
    *undescribed*

CGS_ENGINE__ISP
    *undescribed*

.. _`cgs_firmware_info`:

struct cgs_firmware_info
========================

.. c:type:: struct cgs_firmware_info

    Firmware information

.. _`cgs_firmware_info.definition`:

Definition
----------

.. code-block:: c

    struct cgs_firmware_info {
        uint16_t version;
        uint16_t fw_version;
        uint16_t feature_version;
        uint32_t image_size;
        uint64_t mc_addr;
        uint32_t ucode_start_address;
        void *kptr;
        bool is_kicker;
    }

.. _`cgs_firmware_info.members`:

Members
-------

version
    *undescribed*

fw_version
    *undescribed*

feature_version
    *undescribed*

image_size
    *undescribed*

mc_addr
    *undescribed*

ucode_start_address
    *undescribed*

kptr
    *undescribed*

is_kicker
    *undescribed*

.. _`cgs_alloc_gpu_mem_t`:

cgs_alloc_gpu_mem_t
===================

.. c:function:: int cgs_alloc_gpu_mem_t(struct cgs_device *cgs_device, enum cgs_gpu_mem_type type, uint64_t size, uint64_t align, cgs_handle_t *handle)

    Allocate GPU memory

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param enum cgs_gpu_mem_type type:
        memory type

    :param uint64_t size:
        size in bytes

    :param uint64_t align:
        alignment in bytes

    :param cgs_handle_t \*handle:
        memory handle (output)

.. _`cgs_alloc_gpu_mem_t.description`:

Description
-----------

The memory types CGS_GPU_MEM_TYPE\_\*\_CONTIG_FB force contiguous
memory allocation. This guarantees that the MC address returned by
cgs_gmap_gpu_mem is not mapped through the GART. The non-contiguous
FB memory types may be GART mapped depending on memory
fragmentation and memory allocator policies.

If min/max_offset are non-0, the allocation will be forced to
reside between these offsets in its respective memory heap. The
base address that the offset relates to, depends on the memory
type.

- CGS_GPU_MEM_TYPE_\_\*\_CONTIG_FB: FB MC base address
- CGS_GPU_MEM_TYPE__GART\_\*:      GART aperture base address
- others:                        undefined, don't use with max_offset

.. _`cgs_alloc_gpu_mem_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_free_gpu_mem_t`:

cgs_free_gpu_mem_t
==================

.. c:function:: int cgs_free_gpu_mem_t(struct cgs_device *cgs_device, cgs_handle_t handle)

    Free GPU memory

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param cgs_handle_t handle:
        memory handle returned by alloc or import

.. _`cgs_free_gpu_mem_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_gmap_gpu_mem_t`:

cgs_gmap_gpu_mem_t
==================

.. c:function:: int cgs_gmap_gpu_mem_t(struct cgs_device *cgs_device, cgs_handle_t handle, uint64_t *mcaddr)

    GPU-map GPU memory

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param cgs_handle_t handle:
        memory handle returned by alloc or import

    :param uint64_t \*mcaddr:
        MC address (output)

.. _`cgs_gmap_gpu_mem_t.description`:

Description
-----------

Ensures that a buffer is GPU accessible and returns its MC address.

.. _`cgs_gmap_gpu_mem_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_gunmap_gpu_mem_t`:

cgs_gunmap_gpu_mem_t
====================

.. c:function:: int cgs_gunmap_gpu_mem_t(struct cgs_device *cgs_device, cgs_handle_t handle)

    GPU-unmap GPU memory

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param cgs_handle_t handle:
        memory handle returned by alloc or import

.. _`cgs_gunmap_gpu_mem_t.description`:

Description
-----------

Allows the buffer to be migrated while it's not used by the GPU.

.. _`cgs_gunmap_gpu_mem_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_kmap_gpu_mem_t`:

cgs_kmap_gpu_mem_t
==================

.. c:function:: int cgs_kmap_gpu_mem_t(struct cgs_device *cgs_device, cgs_handle_t handle, void **map)

    Kernel-map GPU memory

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param cgs_handle_t handle:
        memory handle returned by alloc or import

    :param void \*\*map:
        Kernel virtual address the memory was mapped to (output)

.. _`cgs_kmap_gpu_mem_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_kunmap_gpu_mem_t`:

cgs_kunmap_gpu_mem_t
====================

.. c:function:: int cgs_kunmap_gpu_mem_t(struct cgs_device *cgs_device, cgs_handle_t handle)

    Kernel-unmap GPU memory

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param cgs_handle_t handle:
        memory handle returned by alloc or import

.. _`cgs_kunmap_gpu_mem_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_read_register_t`:

cgs_read_register_t
===================

.. c:function:: uint32_t cgs_read_register_t(struct cgs_device *cgs_device, unsigned offset)

    Read an MMIO register

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param unsigned offset:
        register offset

.. _`cgs_read_register_t.return`:

Return
------

register value

.. _`cgs_write_register_t`:

cgs_write_register_t
====================

.. c:function:: void cgs_write_register_t(struct cgs_device *cgs_device, unsigned offset, uint32_t value)

    Write an MMIO register

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param unsigned offset:
        register offset

    :param uint32_t value:
        register value

.. _`cgs_read_ind_register_t`:

cgs_read_ind_register_t
=======================

.. c:function:: uint32_t cgs_read_ind_register_t(struct cgs_device *cgs_device, enum cgs_ind_reg space, unsigned index)

    Read an indirect register

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param enum cgs_ind_reg space:
        *undescribed*

    :param unsigned index:
        *undescribed*

.. _`cgs_read_ind_register_t.return`:

Return
------

register value

.. _`cgs_write_ind_register_t`:

cgs_write_ind_register_t
========================

.. c:function:: void cgs_write_ind_register_t(struct cgs_device *cgs_device, enum cgs_ind_reg space, unsigned index, uint32_t value)

    Write an indirect register

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param enum cgs_ind_reg space:
        *undescribed*

    :param unsigned index:
        *undescribed*

    :param uint32_t value:
        register value

.. _`cgs_get_pci_resource_t`:

cgs_get_pci_resource_t
======================

.. c:function:: int cgs_get_pci_resource_t(struct cgs_device *cgs_device, enum cgs_resource_type resource_type, uint64_t size, uint64_t offset, uint64_t *resource_base)

    provide access to a device resource (PCI BAR)

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param enum cgs_resource_type resource_type:
        Type of Resource (MMIO, IO, ROM, FB, DOORBELL)

    :param uint64_t size:
        size of the region

    :param uint64_t offset:
        offset from the start of the region

    :param uint64_t \*resource_base:
        base address (not including offset) returned

.. _`cgs_get_pci_resource_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_atom_get_cmd_table_revs_t`:

cgs_atom_get_cmd_table_revs_t
=============================

.. c:function:: int cgs_atom_get_cmd_table_revs_t(struct cgs_device *cgs_device, unsigned table, uint8_t *frev, uint8_t *crev)

    Get ATOM BIOS command table revisions

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param unsigned table:
        data table index

    :param uint8_t \*frev:
        table format revision (output, may be NULL)

    :param uint8_t \*crev:
        table content revision (output, may be NULL)

.. _`cgs_atom_get_cmd_table_revs_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_atom_exec_cmd_table_t`:

cgs_atom_exec_cmd_table_t
=========================

.. c:function:: int cgs_atom_exec_cmd_table_t(struct cgs_device *cgs_device, unsigned table, void *args)

    Execute an ATOM BIOS command table

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param unsigned table:
        command table index

    :param void \*args:
        arguments

.. _`cgs_atom_exec_cmd_table_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_get_firmware_info`:

cgs_get_firmware_info
=====================

.. c:function:: int cgs_get_firmware_info(struct cgs_device *cgs_device, enum cgs_ucode_id type, struct cgs_firmware_info *info)

    Get the firmware information from core driver

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param enum cgs_ucode_id type:
        the firmware type

    :param struct cgs_firmware_info \*info:
        returend firmware information

.. _`cgs_get_firmware_info.return`:

Return
------

0 on success, -errno otherwise

.. This file was automatic generated / don't edit.

