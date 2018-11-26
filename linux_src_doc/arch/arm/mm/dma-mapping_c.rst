.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mm/dma-mapping.c

.. _`arm_dma_map_page`:

arm_dma_map_page
================

.. c:function:: dma_addr_t arm_dma_map_page(struct device *dev, struct page *page, unsigned long offset, size_t size, enum dma_data_direction dir, unsigned long attrs)

    map a portion of a page for streaming DMA

    :param dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices
    :type dev: struct device \*

    :param page:
        page that buffer resides in
    :type page: struct page \*

    :param offset:
        offset into page for start of buffer
    :type offset: unsigned long

    :param size:
        size of buffer to map
    :type size: size_t

    :param dir:
        DMA transfer direction
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_dma_map_page.description`:

Description
-----------

Ensure that any data held in the cache is appropriately discarded
or written back.

The device owns this memory once this call has completed.  The CPU
can regain ownership by calling \ :c:func:`dma_unmap_page`\ .

.. _`arm_dma_unmap_page`:

arm_dma_unmap_page
==================

.. c:function:: void arm_dma_unmap_page(struct device *dev, dma_addr_t handle, size_t size, enum dma_data_direction dir, unsigned long attrs)

    unmap a buffer previously mapped through \ :c:func:`dma_map_page`\ 

    :param dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices
    :type dev: struct device \*

    :param handle:
        DMA address of buffer
    :type handle: dma_addr_t

    :param size:
        size of buffer (same as passed to dma_map_page)
    :type size: size_t

    :param dir:
        DMA transfer direction (same as passed to dma_map_page)
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_dma_unmap_page.description`:

Description
-----------

Unmap a page streaming mode DMA translation.  The handle and size
must match what was provided in the previous \ :c:func:`dma_map_page`\  call.
All other usages are undefined.

After this call, reads by the CPU to the buffer are guaranteed to see
whatever the device wrote there.

.. _`arm_dma_map_sg`:

arm_dma_map_sg
==============

.. c:function:: int arm_dma_map_sg(struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir, unsigned long attrs)

    map a set of SG buffers for streaming mode DMA

    :param dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices
    :type dev: struct device \*

    :param sg:
        list of buffers
    :type sg: struct scatterlist \*

    :param nents:
        number of buffers to map
    :type nents: int

    :param dir:
        DMA transfer direction
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_dma_map_sg.description`:

Description
-----------

Map a set of buffers described by scatterlist in streaming mode for DMA.
This is the scatter-gather version of the dma_map_single interface.
Here the scatter gather list elements are each tagged with the
appropriate dma address and length.  They are obtained via
sg_dma_{address,length}.

Device ownership issues as mentioned for dma_map_single are the same
here.

.. _`arm_dma_unmap_sg`:

arm_dma_unmap_sg
================

.. c:function:: void arm_dma_unmap_sg(struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir, unsigned long attrs)

    unmap a set of SG buffers mapped by dma_map_sg

    :param dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices
    :type dev: struct device \*

    :param sg:
        list of buffers
    :type sg: struct scatterlist \*

    :param nents:
        number of buffers to unmap (same as was passed to dma_map_sg)
    :type nents: int

    :param dir:
        DMA transfer direction (same as was passed to dma_map_sg)
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_dma_unmap_sg.description`:

Description
-----------

Unmap a set of streaming mode DMA translations.  Again, CPU access
rules concerning calls here are the same as for \ :c:func:`dma_unmap_single`\ .

.. _`arm_dma_sync_sg_for_cpu`:

arm_dma_sync_sg_for_cpu
=======================

.. c:function:: void arm_dma_sync_sg_for_cpu(struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir)

    :param dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices
    :type dev: struct device \*

    :param sg:
        list of buffers
    :type sg: struct scatterlist \*

    :param nents:
        number of buffers to map (returned from dma_map_sg)
    :type nents: int

    :param dir:
        DMA transfer direction (same as was passed to dma_map_sg)
    :type dir: enum dma_data_direction

.. _`arm_dma_sync_sg_for_device`:

arm_dma_sync_sg_for_device
==========================

.. c:function:: void arm_dma_sync_sg_for_device(struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir)

    :param dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices
    :type dev: struct device \*

    :param sg:
        list of buffers
    :type sg: struct scatterlist \*

    :param nents:
        number of buffers to map (returned from dma_map_sg)
    :type nents: int

    :param dir:
        DMA transfer direction (same as was passed to dma_map_sg)
    :type dir: enum dma_data_direction

.. _`arm_coherent_iommu_map_sg`:

arm_coherent_iommu_map_sg
=========================

.. c:function:: int arm_coherent_iommu_map_sg(struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir, unsigned long attrs)

    map a set of SG buffers for streaming mode DMA

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param sg:
        list of buffers
    :type sg: struct scatterlist \*

    :param nents:
        number of buffers to map
    :type nents: int

    :param dir:
        DMA transfer direction
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_coherent_iommu_map_sg.description`:

Description
-----------

Map a set of i/o coherent buffers described by scatterlist in streaming
mode for DMA. The scatter gather list elements are merged together (if
possible) and tagged with the appropriate dma address and length. They are
obtained via sg_dma_{address,length}.

.. _`arm_iommu_map_sg`:

arm_iommu_map_sg
================

.. c:function:: int arm_iommu_map_sg(struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir, unsigned long attrs)

    map a set of SG buffers for streaming mode DMA

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param sg:
        list of buffers
    :type sg: struct scatterlist \*

    :param nents:
        number of buffers to map
    :type nents: int

    :param dir:
        DMA transfer direction
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_iommu_map_sg.description`:

Description
-----------

Map a set of buffers described by scatterlist in streaming mode for DMA.
The scatter gather list elements are merged together (if possible) and
tagged with the appropriate dma address and length. They are obtained via
sg_dma_{address,length}.

.. _`arm_coherent_iommu_unmap_sg`:

arm_coherent_iommu_unmap_sg
===========================

.. c:function:: void arm_coherent_iommu_unmap_sg(struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir, unsigned long attrs)

    unmap a set of SG buffers mapped by dma_map_sg

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param sg:
        list of buffers
    :type sg: struct scatterlist \*

    :param nents:
        number of buffers to unmap (same as was passed to dma_map_sg)
    :type nents: int

    :param dir:
        DMA transfer direction (same as was passed to dma_map_sg)
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_coherent_iommu_unmap_sg.description`:

Description
-----------

Unmap a set of streaming mode DMA translations.  Again, CPU access
rules concerning calls here are the same as for \ :c:func:`dma_unmap_single`\ .

.. _`arm_iommu_unmap_sg`:

arm_iommu_unmap_sg
==================

.. c:function:: void arm_iommu_unmap_sg(struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir, unsigned long attrs)

    unmap a set of SG buffers mapped by dma_map_sg

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param sg:
        list of buffers
    :type sg: struct scatterlist \*

    :param nents:
        number of buffers to unmap (same as was passed to dma_map_sg)
    :type nents: int

    :param dir:
        DMA transfer direction (same as was passed to dma_map_sg)
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_iommu_unmap_sg.description`:

Description
-----------

Unmap a set of streaming mode DMA translations.  Again, CPU access
rules concerning calls here are the same as for \ :c:func:`dma_unmap_single`\ .

.. _`arm_iommu_sync_sg_for_cpu`:

arm_iommu_sync_sg_for_cpu
=========================

.. c:function:: void arm_iommu_sync_sg_for_cpu(struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir)

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param sg:
        list of buffers
    :type sg: struct scatterlist \*

    :param nents:
        number of buffers to map (returned from dma_map_sg)
    :type nents: int

    :param dir:
        DMA transfer direction (same as was passed to dma_map_sg)
    :type dir: enum dma_data_direction

.. _`arm_iommu_sync_sg_for_device`:

arm_iommu_sync_sg_for_device
============================

.. c:function:: void arm_iommu_sync_sg_for_device(struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir)

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param sg:
        list of buffers
    :type sg: struct scatterlist \*

    :param nents:
        number of buffers to map (returned from dma_map_sg)
    :type nents: int

    :param dir:
        DMA transfer direction (same as was passed to dma_map_sg)
    :type dir: enum dma_data_direction

.. _`arm_coherent_iommu_map_page`:

arm_coherent_iommu_map_page
===========================

.. c:function:: dma_addr_t arm_coherent_iommu_map_page(struct device *dev, struct page *page, unsigned long offset, size_t size, enum dma_data_direction dir, unsigned long attrs)

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param page:
        page that buffer resides in
    :type page: struct page \*

    :param offset:
        offset into page for start of buffer
    :type offset: unsigned long

    :param size:
        size of buffer to map
    :type size: size_t

    :param dir:
        DMA transfer direction
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_coherent_iommu_map_page.description`:

Description
-----------

Coherent IOMMU aware version of \ :c:func:`arm_dma_map_page`\ 

.. _`arm_iommu_map_page`:

arm_iommu_map_page
==================

.. c:function:: dma_addr_t arm_iommu_map_page(struct device *dev, struct page *page, unsigned long offset, size_t size, enum dma_data_direction dir, unsigned long attrs)

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param page:
        page that buffer resides in
    :type page: struct page \*

    :param offset:
        offset into page for start of buffer
    :type offset: unsigned long

    :param size:
        size of buffer to map
    :type size: size_t

    :param dir:
        DMA transfer direction
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_iommu_map_page.description`:

Description
-----------

IOMMU aware version of \ :c:func:`arm_dma_map_page`\ 

.. _`arm_coherent_iommu_unmap_page`:

arm_coherent_iommu_unmap_page
=============================

.. c:function:: void arm_coherent_iommu_unmap_page(struct device *dev, dma_addr_t handle, size_t size, enum dma_data_direction dir, unsigned long attrs)

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param handle:
        DMA address of buffer
    :type handle: dma_addr_t

    :param size:
        size of buffer (same as passed to dma_map_page)
    :type size: size_t

    :param dir:
        DMA transfer direction (same as passed to dma_map_page)
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_coherent_iommu_unmap_page.description`:

Description
-----------

Coherent IOMMU aware version of \ :c:func:`arm_dma_unmap_page`\ 

.. _`arm_iommu_unmap_page`:

arm_iommu_unmap_page
====================

.. c:function:: void arm_iommu_unmap_page(struct device *dev, dma_addr_t handle, size_t size, enum dma_data_direction dir, unsigned long attrs)

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param handle:
        DMA address of buffer
    :type handle: dma_addr_t

    :param size:
        size of buffer (same as passed to dma_map_page)
    :type size: size_t

    :param dir:
        DMA transfer direction (same as passed to dma_map_page)
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_iommu_unmap_page.description`:

Description
-----------

IOMMU aware version of \ :c:func:`arm_dma_unmap_page`\ 

.. _`arm_iommu_map_resource`:

arm_iommu_map_resource
======================

.. c:function:: dma_addr_t arm_iommu_map_resource(struct device *dev, phys_addr_t phys_addr, size_t size, enum dma_data_direction dir, unsigned long attrs)

    map a device resource for DMA

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param phys_addr:
        physical address of resource
    :type phys_addr: phys_addr_t

    :param size:
        size of resource to map
    :type size: size_t

    :param dir:
        DMA transfer direction
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_iommu_unmap_resource`:

arm_iommu_unmap_resource
========================

.. c:function:: void arm_iommu_unmap_resource(struct device *dev, dma_addr_t dma_handle, size_t size, enum dma_data_direction dir, unsigned long attrs)

    unmap a device DMA resource

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param dma_handle:
        DMA address to resource
    :type dma_handle: dma_addr_t

    :param size:
        size of resource to map
    :type size: size_t

    :param dir:
        DMA transfer direction
    :type dir: enum dma_data_direction

    :param attrs:
        *undescribed*
    :type attrs: unsigned long

.. _`arm_iommu_create_mapping`:

arm_iommu_create_mapping
========================

.. c:function:: struct dma_iommu_mapping *arm_iommu_create_mapping(struct bus_type *bus, dma_addr_t base, u64 size)

    :param bus:
        pointer to the bus holding the client device (for IOMMU calls)
    :type bus: struct bus_type \*

    :param base:
        start address of the valid IO address space
    :type base: dma_addr_t

    :param size:
        maximum size of the valid IO address space
    :type size: u64

.. _`arm_iommu_create_mapping.description`:

Description
-----------

Creates a mapping structure which holds information about used/unused
IO address ranges, which is required to perform memory allocation and
mapping with IOMMU aware functions.

The client device need to be attached to the mapping with
arm_iommu_attach_device function.

.. _`arm_iommu_attach_device`:

arm_iommu_attach_device
=======================

.. c:function:: int arm_iommu_attach_device(struct device *dev, struct dma_iommu_mapping *mapping)

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

    :param mapping:
        io address space mapping structure (returned from
        arm_iommu_create_mapping)
    :type mapping: struct dma_iommu_mapping \*

.. _`arm_iommu_attach_device.description`:

Description
-----------

Attaches specified io address space mapping to the provided device.
This replaces the dma operations (dma_map_ops pointer) with the
IOMMU aware version.

More than one client might be attached to the same io address space
mapping.

.. _`arm_iommu_detach_device`:

arm_iommu_detach_device
=======================

.. c:function:: void arm_iommu_detach_device(struct device *dev)

    :param dev:
        valid struct device pointer
    :type dev: struct device \*

.. _`arm_iommu_detach_device.description`:

Description
-----------

Detaches the provided device from a previously attached map.
This voids the dma operations (dma_map_ops pointer)

.. This file was automatic generated / don't edit.

