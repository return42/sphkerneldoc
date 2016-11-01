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

CGS_IND_REG__AUDIO_ENDPT
    *undescribed*

.. _`cgs_clock`:

enum cgs_clock
==============

.. c:type:: enum cgs_clock

    Clocks controlled by the SMU

.. _`cgs_clock.definition`:

Definition
----------

.. code-block:: c

    enum cgs_clock {
        CGS_CLOCK__SCLK,
        CGS_CLOCK__MCLK,
        CGS_CLOCK__VCLK,
        CGS_CLOCK__DCLK,
        CGS_CLOCK__ECLK,
        CGS_CLOCK__ACLK,
        CGS_CLOCK__ICLK
    };

.. _`cgs_clock.constants`:

Constants
---------

CGS_CLOCK__SCLK
    *undescribed*

CGS_CLOCK__MCLK
    *undescribed*

CGS_CLOCK__VCLK
    *undescribed*

CGS_CLOCK__DCLK
    *undescribed*

CGS_CLOCK__ECLK
    *undescribed*

CGS_CLOCK__ACLK
    *undescribed*

CGS_CLOCK__ICLK
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

.. _`cgs_voltage_planes`:

enum cgs_voltage_planes
=======================

.. c:type:: enum cgs_voltage_planes

    Voltage planes for external camera HW

.. _`cgs_voltage_planes.definition`:

Definition
----------

.. code-block:: c

    enum cgs_voltage_planes {
        CGS_VOLTAGE_PLANE__SENSOR0,
        CGS_VOLTAGE_PLANE__SENSOR1
    };

.. _`cgs_voltage_planes.constants`:

Constants
---------

CGS_VOLTAGE_PLANE__SENSOR0
    *undescribed*

CGS_VOLTAGE_PLANE__SENSOR1
    *undescribed*

.. _`cgs_clock_limits`:

struct cgs_clock_limits
=======================

.. c:type:: struct cgs_clock_limits

    Clock limits

.. _`cgs_clock_limits.definition`:

Definition
----------

.. code-block:: c

    struct cgs_clock_limits {
        unsigned min;
        unsigned max;
        unsigned sustainable;
    }

.. _`cgs_clock_limits.members`:

Members
-------

min
    *undescribed*

max
    *undescribed*

sustainable
    *undescribed*

.. _`cgs_clock_limits.description`:

Description
-----------

Clocks are specified in 10KHz units.

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

.. _`cgs_gpu_mem_info_t`:

cgs_gpu_mem_info_t
==================

.. c:function:: int cgs_gpu_mem_info_t(struct cgs_device *cgs_device, enum cgs_gpu_mem_type type, uint64_t *mc_start, uint64_t *mc_size, uint64_t *mem_size)

    Return information about memory heaps

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param enum cgs_gpu_mem_type type:
        memory type

    :param uint64_t \*mc_start:
        Start MC address of the heap (output)

    :param uint64_t \*mc_size:
        MC address space size (output)

    :param uint64_t \*mem_size:
        maximum amount of memory available for allocation (output)

.. _`cgs_gpu_mem_info_t.description`:

Description
-----------

This function returns information about memory heaps. The type
parameter is used to select the memory heap. The mc_start and
mc_size for GART heaps may be bigger than the memory available for
allocation.

mc_start and mc_size are undefined for non-contiguous FB memory
types, since buffers allocated with these types may or may not be
GART mapped.

.. _`cgs_gpu_mem_info_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_gmap_kmem_t`:

cgs_gmap_kmem_t
===============

.. c:function:: int cgs_gmap_kmem_t(struct cgs_device *cgs_device, void *kmem, uint64_t size, uint64_t min_offset, uint64_t max_offset, cgs_handle_t *kmem_handle, uint64_t *mcaddr)

    map kernel memory to GART aperture

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param void \*kmem:
        pointer to kernel memory

    :param uint64_t size:
        size to map

    :param uint64_t min_offset:
        minimum offset from start of GART aperture

    :param uint64_t max_offset:
        maximum offset from start of GART aperture

    :param cgs_handle_t \*kmem_handle:
        kernel memory handle (output)

    :param uint64_t \*mcaddr:
        MC address (output)

.. _`cgs_gmap_kmem_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_gunmap_kmem_t`:

cgs_gunmap_kmem_t
=================

.. c:function:: int cgs_gunmap_kmem_t(struct cgs_device *cgs_device, cgs_handle_t kmem_handle)

    unmap kernel memory

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param cgs_handle_t kmem_handle:
        kernel memory handle returned by gmap_kmem

.. _`cgs_gunmap_kmem_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_alloc_gpu_mem_t`:

cgs_alloc_gpu_mem_t
===================

.. c:function:: int cgs_alloc_gpu_mem_t(struct cgs_device *cgs_device, enum cgs_gpu_mem_type type, uint64_t size, uint64_t align, uint64_t min_offset, uint64_t max_offset, cgs_handle_t *handle)

    Allocate GPU memory

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param enum cgs_gpu_mem_type type:
        memory type

    :param uint64_t size:
        size in bytes

    :param uint64_t align:
        alignment in bytes

    :param uint64_t min_offset:
        minimum offset from start of heap

    :param uint64_t max_offset:
        maximum offset from start of heap

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

.. _`cgs_read_pci_config_byte_t`:

cgs_read_pci_config_byte_t
==========================

.. c:function:: uint8_t cgs_read_pci_config_byte_t(struct cgs_device *cgs_device, unsigned addr)

    Read byte from PCI configuration space

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param unsigned addr:
        address

.. _`cgs_read_pci_config_byte_t.return`:

Return
------

Value read

.. _`cgs_read_pci_config_word_t`:

cgs_read_pci_config_word_t
==========================

.. c:function:: uint16_t cgs_read_pci_config_word_t(struct cgs_device *cgs_device, unsigned addr)

    Read word from PCI configuration space

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param unsigned addr:
        address, must be word-aligned

.. _`cgs_read_pci_config_word_t.return`:

Return
------

Value read

.. _`cgs_read_pci_config_dword_t`:

cgs_read_pci_config_dword_t
===========================

.. c:function:: uint32_t cgs_read_pci_config_dword_t(struct cgs_device *cgs_device, unsigned addr)

    Read dword from PCI configuration space

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param unsigned addr:
        address, must be dword-aligned

.. _`cgs_read_pci_config_dword_t.return`:

Return
------

Value read

.. _`cgs_write_pci_config_byte_t`:

cgs_write_pci_config_byte_t
===========================

.. c:function:: void cgs_write_pci_config_byte_t(struct cgs_device *cgs_device, unsigned addr, uint8_t value)

    Write byte to PCI configuration space

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param unsigned addr:
        address

    :param uint8_t value:
        value to write

.. _`cgs_write_pci_config_word_t`:

cgs_write_pci_config_word_t
===========================

.. c:function:: void cgs_write_pci_config_word_t(struct cgs_device *cgs_device, unsigned addr, uint16_t value)

    Write byte to PCI configuration space

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param unsigned addr:
        address, must be word-aligned

    :param uint16_t value:
        value to write

.. _`cgs_write_pci_config_dword_t`:

cgs_write_pci_config_dword_t
============================

.. c:function:: void cgs_write_pci_config_dword_t(struct cgs_device *cgs_device, unsigned addr, uint32_t value)

    Write byte to PCI configuration space

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param unsigned addr:
        address, must be dword-aligned

    :param uint32_t value:
        value to write

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

.. _`cgs_create_pm_request_t`:

cgs_create_pm_request_t
=======================

.. c:function:: int cgs_create_pm_request_t(struct cgs_device *cgs_device, cgs_handle_t *request)

    Create a power management request

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param cgs_handle_t \*request:
        handle of created PM request (output)

.. _`cgs_create_pm_request_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_destroy_pm_request_t`:

cgs_destroy_pm_request_t
========================

.. c:function:: int cgs_destroy_pm_request_t(struct cgs_device *cgs_device, cgs_handle_t request)

    Destroy a power management request

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param cgs_handle_t request:
        handle of created PM request

.. _`cgs_destroy_pm_request_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_set_pm_request_t`:

cgs_set_pm_request_t
====================

.. c:function:: int cgs_set_pm_request_t(struct cgs_device *cgs_device, cgs_handle_t request, int active)

    Activate or deactiveate a PM request

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param cgs_handle_t request:
        PM request handle

    :param int active:
        0 = deactivate, non-0 = activate

.. _`cgs_set_pm_request_t.description`:

Description
-----------

While a PM request is active, its minimum clock requests are taken
into account as the requested engines are powered up. When the
request is inactive, the engines may be powered down and clocks may
be lower, depending on other PM requests by other driver
components.

.. _`cgs_set_pm_request_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_pm_request_clock_t`:

cgs_pm_request_clock_t
======================

.. c:function:: int cgs_pm_request_clock_t(struct cgs_device *cgs_device, cgs_handle_t request, enum cgs_clock clock, unsigned freq)

    Request a minimum frequency for a specific clock

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param cgs_handle_t request:
        PM request handle

    :param enum cgs_clock clock:
        which clock?

    :param unsigned freq:
        requested min. frequency in 10KHz units (0 to clear request)

.. _`cgs_pm_request_clock_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_pm_request_engine_t`:

cgs_pm_request_engine_t
=======================

.. c:function:: int cgs_pm_request_engine_t(struct cgs_device *cgs_device, cgs_handle_t request, enum cgs_engine engine, int powered)

    Request an engine to be powered up

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param cgs_handle_t request:
        PM request handle

    :param enum cgs_engine engine:
        which engine?

    :param int powered:
        0 = powered down, non-0 = powered up

.. _`cgs_pm_request_engine_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_pm_query_clock_limits_t`:

cgs_pm_query_clock_limits_t
===========================

.. c:function:: int cgs_pm_query_clock_limits_t(struct cgs_device *cgs_device, enum cgs_clock clock, struct cgs_clock_limits *limits)

    Query clock frequency limits

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param enum cgs_clock clock:
        which clock?

    :param struct cgs_clock_limits \*limits:
        clock limits

.. _`cgs_pm_query_clock_limits_t.return`:

Return
------

0 on success, -errno otherwise

.. _`cgs_set_camera_voltages_t`:

cgs_set_camera_voltages_t
=========================

.. c:function:: int cgs_set_camera_voltages_t(struct cgs_device *cgs_device, uint32_t mask, const uint32_t *voltages)

    Apply specific voltages to PMIC voltage planes

    :param struct cgs_device \*cgs_device:
        opaque device handle

    :param uint32_t mask:
        bitmask of voltages to change (1<<CGS_VOLTAGE_PLANE__xyz\|...)

    :param const uint32_t \*voltages:
        pointer to array of voltage values in 1mV units

.. _`cgs_set_camera_voltages_t.return`:

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

