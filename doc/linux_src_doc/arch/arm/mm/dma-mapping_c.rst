.. -*- coding: utf-8; mode: rst -*-

=============
dma-mapping.c
=============


.. _`arm_dma_map_page`:

arm_dma_map_page
================

.. c:function:: dma_addr_t arm_dma_map_page (struct device *dev, struct page *page, unsigned long offset, size_t size, enum dma_data_direction dir, struct dma_attrs *attrs)

    map a portion of a page for streaming DMA

    :param struct device \*dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices

    :param struct page \*page:
        page that buffer resides in

    :param unsigned long offset:
        offset into page for start of buffer

    :param size_t size:
        size of buffer to map

    :param enum dma_data_direction dir:
        DMA transfer direction

    :param struct dma_attrs \*attrs:

        *undescribed*



.. _`arm_dma_map_page.description`:

Description
-----------

Ensure that any data held in the cache is appropriately discarded
or written back.

The device owns this memory once this call has completed.  The CPU
can regain ownership by calling :c:func:`dma_unmap_page`.



.. _`arm_dma_unmap_page`:

arm_dma_unmap_page
==================

.. c:function:: void arm_dma_unmap_page (struct device *dev, dma_addr_t handle, size_t size, enum dma_data_direction dir, struct dma_attrs *attrs)

    unmap a buffer previously mapped through dma_map_page()

    :param struct device \*dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices

    :param dma_addr_t handle:
        DMA address of buffer

    :param size_t size:
        size of buffer (same as passed to dma_map_page)

    :param enum dma_data_direction dir:
        DMA transfer direction (same as passed to dma_map_page)

    :param struct dma_attrs \*attrs:

        *undescribed*



.. _`arm_dma_unmap_page.description`:

Description
-----------

Unmap a page streaming mode DMA translation.  The handle and size
must match what was provided in the previous :c:func:`dma_map_page` call.
All other usages are undefined.

After this call, reads by the CPU to the buffer are guaranteed to see
whatever the device wrote there.



.. _`arm_dma_map_sg`:

arm_dma_map_sg
==============

.. c:function:: int arm_dma_map_sg (struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir, struct dma_attrs *attrs)

    map a set of SG buffers for streaming mode DMA

    :param struct device \*dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices

    :param struct scatterlist \*sg:
        list of buffers

    :param int nents:
        number of buffers to map

    :param enum dma_data_direction dir:
        DMA transfer direction

    :param struct dma_attrs \*attrs:

        *undescribed*



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

.. c:function:: void arm_dma_unmap_sg (struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir, struct dma_attrs *attrs)

    unmap a set of SG buffers mapped by dma_map_sg

    :param struct device \*dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices

    :param struct scatterlist \*sg:
        list of buffers

    :param int nents:
        number of buffers to unmap (same as was passed to dma_map_sg)

    :param enum dma_data_direction dir:
        DMA transfer direction (same as was passed to dma_map_sg)

    :param struct dma_attrs \*attrs:

        *undescribed*



.. _`arm_dma_unmap_sg.description`:

Description
-----------

Unmap a set of streaming mode DMA translations.  Again, CPU access
rules concerning calls here are the same as for :c:func:`dma_unmap_single`.



.. _`arm_dma_sync_sg_for_cpu`:

arm_dma_sync_sg_for_cpu
=======================

.. c:function:: void arm_dma_sync_sg_for_cpu (struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir)

    :param struct device \*dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices

    :param struct scatterlist \*sg:
        list of buffers

    :param int nents:
        number of buffers to map (returned from dma_map_sg)

    :param enum dma_data_direction dir:
        DMA transfer direction (same as was passed to dma_map_sg)



.. _`arm_dma_sync_sg_for_device`:

arm_dma_sync_sg_for_device
==========================

.. c:function:: void arm_dma_sync_sg_for_device (struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir)

    :param struct device \*dev:
        valid struct device pointer, or NULL for ISA and EISA-like devices

    :param struct scatterlist \*sg:
        list of buffers

    :param int nents:
        number of buffers to map (returned from dma_map_sg)

    :param enum dma_data_direction dir:
        DMA transfer direction (same as was passed to dma_map_sg)



.. _`arm_coherent_iommu_map_sg`:

arm_coherent_iommu_map_sg
=========================

.. c:function:: int arm_coherent_iommu_map_sg (struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir, struct dma_attrs *attrs)

    map a set of SG buffers for streaming mode DMA

    :param struct device \*dev:
        valid struct device pointer

    :param struct scatterlist \*sg:
        list of buffers

    :param int nents:
        number of buffers to map

    :param enum dma_data_direction dir:
        DMA transfer direction

    :param struct dma_attrs \*attrs:

        *undescribed*



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

.. c:function:: int arm_iommu_map_sg (struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir, struct dma_attrs *attrs)

    map a set of SG buffers for streaming mode DMA

    :param struct device \*dev:
        valid struct device pointer

    :param struct scatterlist \*sg:
        list of buffers

    :param int nents:
        number of buffers to map

    :param enum dma_data_direction dir:
        DMA transfer direction

    :param struct dma_attrs \*attrs:

        *undescribed*



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

.. c:function:: void arm_coherent_iommu_unmap_sg (struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir, struct dma_attrs *attrs)

    unmap a set of SG buffers mapped by dma_map_sg

    :param struct device \*dev:
        valid struct device pointer

    :param struct scatterlist \*sg:
        list of buffers

    :param int nents:
        number of buffers to unmap (same as was passed to dma_map_sg)

    :param enum dma_data_direction dir:
        DMA transfer direction (same as was passed to dma_map_sg)

    :param struct dma_attrs \*attrs:

        *undescribed*



.. _`arm_coherent_iommu_unmap_sg.description`:

Description
-----------

Unmap a set of streaming mode DMA translations.  Again, CPU access
rules concerning calls here are the same as for :c:func:`dma_unmap_single`.



.. _`arm_iommu_unmap_sg`:

arm_iommu_unmap_sg
==================

.. c:function:: void arm_iommu_unmap_sg (struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir, struct dma_attrs *attrs)

    unmap a set of SG buffers mapped by dma_map_sg

    :param struct device \*dev:
        valid struct device pointer

    :param struct scatterlist \*sg:
        list of buffers

    :param int nents:
        number of buffers to unmap (same as was passed to dma_map_sg)

    :param enum dma_data_direction dir:
        DMA transfer direction (same as was passed to dma_map_sg)

    :param struct dma_attrs \*attrs:

        *undescribed*



.. _`arm_iommu_unmap_sg.description`:

Description
-----------

Unmap a set of streaming mode DMA translations.  Again, CPU access
rules concerning calls here are the same as for :c:func:`dma_unmap_single`.



.. _`arm_iommu_sync_sg_for_cpu`:

arm_iommu_sync_sg_for_cpu
=========================

.. c:function:: void arm_iommu_sync_sg_for_cpu (struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir)

    :param struct device \*dev:
        valid struct device pointer

    :param struct scatterlist \*sg:
        list of buffers

    :param int nents:
        number of buffers to map (returned from dma_map_sg)

    :param enum dma_data_direction dir:
        DMA transfer direction (same as was passed to dma_map_sg)



.. _`arm_iommu_sync_sg_for_device`:

arm_iommu_sync_sg_for_device
============================

.. c:function:: void arm_iommu_sync_sg_for_device (struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir)

    :param struct device \*dev:
        valid struct device pointer

    :param struct scatterlist \*sg:
        list of buffers

    :param int nents:
        number of buffers to map (returned from dma_map_sg)

    :param enum dma_data_direction dir:
        DMA transfer direction (same as was passed to dma_map_sg)



.. _`arm_coherent_iommu_map_page`:

arm_coherent_iommu_map_page
===========================

.. c:function:: dma_addr_t arm_coherent_iommu_map_page (struct device *dev, struct page *page, unsigned long offset, size_t size, enum dma_data_direction dir, struct dma_attrs *attrs)

    :param struct device \*dev:
        valid struct device pointer

    :param struct page \*page:
        page that buffer resides in

    :param unsigned long offset:
        offset into page for start of buffer

    :param size_t size:
        size of buffer to map

    :param enum dma_data_direction dir:
        DMA transfer direction

    :param struct dma_attrs \*attrs:

        *undescribed*



.. _`arm_coherent_iommu_map_page.description`:

Description
-----------

Coherent IOMMU aware version of :c:func:`arm_dma_map_page`



.. _`arm_iommu_map_page`:

arm_iommu_map_page
==================

.. c:function:: dma_addr_t arm_iommu_map_page (struct device *dev, struct page *page, unsigned long offset, size_t size, enum dma_data_direction dir, struct dma_attrs *attrs)

    :param struct device \*dev:
        valid struct device pointer

    :param struct page \*page:
        page that buffer resides in

    :param unsigned long offset:
        offset into page for start of buffer

    :param size_t size:
        size of buffer to map

    :param enum dma_data_direction dir:
        DMA transfer direction

    :param struct dma_attrs \*attrs:

        *undescribed*



.. _`arm_iommu_map_page.description`:

Description
-----------

IOMMU aware version of :c:func:`arm_dma_map_page`



.. _`arm_coherent_iommu_unmap_page`:

arm_coherent_iommu_unmap_page
=============================

.. c:function:: void arm_coherent_iommu_unmap_page (struct device *dev, dma_addr_t handle, size_t size, enum dma_data_direction dir, struct dma_attrs *attrs)

    :param struct device \*dev:
        valid struct device pointer

    :param dma_addr_t handle:
        DMA address of buffer

    :param size_t size:
        size of buffer (same as passed to dma_map_page)

    :param enum dma_data_direction dir:
        DMA transfer direction (same as passed to dma_map_page)

    :param struct dma_attrs \*attrs:

        *undescribed*



.. _`arm_coherent_iommu_unmap_page.description`:

Description
-----------

Coherent IOMMU aware version of :c:func:`arm_dma_unmap_page`



.. _`arm_iommu_unmap_page`:

arm_iommu_unmap_page
====================

.. c:function:: void arm_iommu_unmap_page (struct device *dev, dma_addr_t handle, size_t size, enum dma_data_direction dir, struct dma_attrs *attrs)

    :param struct device \*dev:
        valid struct device pointer

    :param dma_addr_t handle:
        DMA address of buffer

    :param size_t size:
        size of buffer (same as passed to dma_map_page)

    :param enum dma_data_direction dir:
        DMA transfer direction (same as passed to dma_map_page)

    :param struct dma_attrs \*attrs:

        *undescribed*



.. _`arm_iommu_unmap_page.description`:

Description
-----------

IOMMU aware version of :c:func:`arm_dma_unmap_page`



.. _`arm_iommu_create_mapping`:

arm_iommu_create_mapping
========================

.. c:function:: struct dma_iommu_mapping *arm_iommu_create_mapping (struct bus_type *bus, dma_addr_t base, u64 size)

    :param struct bus_type \*bus:
        pointer to the bus holding the client device (for IOMMU calls)

    :param dma_addr_t base:
        start address of the valid IO address space

    :param u64 size:
        maximum size of the valid IO address space



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

.. c:function:: int arm_iommu_attach_device (struct device *dev, struct dma_iommu_mapping *mapping)

    :param struct device \*dev:
        valid struct device pointer

    :param struct dma_iommu_mapping \*mapping:
        io address space mapping structure (returned from
        arm_iommu_create_mapping)



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

.. c:function:: void arm_iommu_detach_device (struct device *dev)

    :param struct device \*dev:
        valid struct device pointer



.. _`arm_iommu_detach_device.description`:

Description
-----------

Detaches the provided device from a previously attached map.
This voids the dma operations (dma_map_ops pointer)

