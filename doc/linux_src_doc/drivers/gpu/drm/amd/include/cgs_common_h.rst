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
        uint16_t feature_version;
        uint32_t image_size;
        uint64_t mc_addr;
        void *kptr;
    }

.. _`cgs_firmware_info.members`:

Members
-------

version
    *undescribed*

feature_version
    *undescribed*

image_size
    *undescribed*

mc_addr
    *undescribed*

kptr
    *undescribed*

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_gpu_mem_info_t)

    Return information about memory heaps

    :param \*cgs_gpu_mem_info_t:
        *undescribed*

.. _`int.description`:

Description
-----------

This function returns information about memory heaps. The type
parameter is used to select the memory heap. The mc_start and
mc_size for GART heaps may be bigger than the memory available for
allocation.

mc_start and mc_size are undefined for non-contiguous FB memory
types, since buffers allocated with these types may or may not be
GART mapped.

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_gmap_kmem_t)

    map kernel memory to GART aperture

    :param \*cgs_gmap_kmem_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_gunmap_kmem_t)

    unmap kernel memory

    :param \*cgs_gunmap_kmem_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_alloc_gpu_mem_t)

    Allocate GPU memory

    :param \*cgs_alloc_gpu_mem_t:
        *undescribed*

.. _`int.description`:

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

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_free_gpu_mem_t)

    Free GPU memory

    :param \*cgs_free_gpu_mem_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_gmap_gpu_mem_t)

    GPU-map GPU memory

    :param \*cgs_gmap_gpu_mem_t:
        *undescribed*

.. _`int.description`:

Description
-----------

Ensures that a buffer is GPU accessible and returns its MC address.

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_gunmap_gpu_mem_t)

    GPU-unmap GPU memory

    :param \*cgs_gunmap_gpu_mem_t:
        *undescribed*

.. _`int.description`:

Description
-----------

Allows the buffer to be migrated while it's not used by the GPU.

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_kmap_gpu_mem_t)

    Kernel-map GPU memory

    :param \*cgs_kmap_gpu_mem_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_kunmap_gpu_mem_t)

    Kernel-unmap GPU memory

    :param \*cgs_kunmap_gpu_mem_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`uint32_t`:

uint32_t
========

.. c:function:: typedef uint32_t(*cgs_read_register_t)

    Read an MMIO register

    :param \*cgs_read_register_t:
        *undescribed*

.. _`uint32_t.return`:

Return
------

register value

.. _`void`:

void
====

.. c:function:: typedef void(*cgs_write_register_t)

    Write an MMIO register

    :param \*cgs_write_register_t:
        *undescribed*

.. _`uint32_t`:

uint32_t
========

.. c:function:: typedef uint32_t(*cgs_read_ind_register_t)

    Read an indirect register

    :param \*cgs_read_ind_register_t:
        *undescribed*

.. _`uint32_t.return`:

Return
------

register value

.. _`void`:

void
====

.. c:function:: typedef void(*cgs_write_ind_register_t)

    Write an indirect register

    :param \*cgs_write_ind_register_t:
        *undescribed*

.. _`uint8_t`:

uint8_t
=======

.. c:function:: typedef uint8_t(*cgs_read_pci_config_byte_t)

    Read byte from PCI configuration space

    :param \*cgs_read_pci_config_byte_t:
        *undescribed*

.. _`uint8_t.return`:

Return
------

Value read

.. _`uint16_t`:

uint16_t
========

.. c:function:: typedef uint16_t(*cgs_read_pci_config_word_t)

    Read word from PCI configuration space

    :param \*cgs_read_pci_config_word_t:
        *undescribed*

.. _`uint16_t.return`:

Return
------

Value read

.. _`uint32_t`:

uint32_t
========

.. c:function:: typedef uint32_t(*cgs_read_pci_config_dword_t)

    Read dword from PCI configuration space

    :param \*cgs_read_pci_config_dword_t:
        *undescribed*

.. _`uint32_t.return`:

Return
------

Value read

.. _`void`:

void
====

.. c:function:: typedef void(*cgs_write_pci_config_byte_t)

    Write byte to PCI configuration space

    :param \*cgs_write_pci_config_byte_t:
        *undescribed*

.. _`void`:

void
====

.. c:function:: typedef void(*cgs_write_pci_config_word_t)

    Write byte to PCI configuration space

    :param \*cgs_write_pci_config_word_t:
        *undescribed*

.. _`void`:

void
====

.. c:function:: typedef void(*cgs_write_pci_config_dword_t)

    Write byte to PCI configuration space

    :param \*cgs_write_pci_config_dword_t:
        *undescribed*

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_get_pci_resource_t)

    provide access to a device resource (PCI BAR)

    :param \*cgs_get_pci_resource_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_atom_get_cmd_table_revs_t)

    Get ATOM BIOS command table revisions

    :param \*cgs_atom_get_cmd_table_revs_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_atom_exec_cmd_table_t)

    Execute an ATOM BIOS command table

    :param \*cgs_atom_exec_cmd_table_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_create_pm_request_t)

    Create a power management request

    :param \*cgs_create_pm_request_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_destroy_pm_request_t)

    Destroy a power management request

    :param \*cgs_destroy_pm_request_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_set_pm_request_t)

    Activate or deactiveate a PM request

    :param \*cgs_set_pm_request_t:
        *undescribed*

.. _`int.description`:

Description
-----------

While a PM request is active, its minimum clock requests are taken
into account as the requested engines are powered up. When the
request is inactive, the engines may be powered down and clocks may
be lower, depending on other PM requests by other driver
components.

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_pm_request_clock_t)

    Request a minimum frequency for a specific clock

    :param \*cgs_pm_request_clock_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_pm_request_engine_t)

    Request an engine to be powered up

    :param \*cgs_pm_request_engine_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_pm_query_clock_limits_t)

    Query clock frequency limits

    :param \*cgs_pm_query_clock_limits_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_set_camera_voltages_t)

    Apply specific voltages to PMIC voltage planes

    :param \*cgs_set_camera_voltages_t:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. _`int`:

int
===

.. c:function:: typedef int(*cgs_get_firmware_info)

    Get the firmware information from core driver

    :param \*cgs_get_firmware_info:
        *undescribed*

.. _`int.return`:

Return
------

0 on success, -errno otherwise

.. This file was automatic generated / don't edit.

