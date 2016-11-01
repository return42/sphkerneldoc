.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/videobuf2-dma-contig.c

.. _`vb2_dma_contig_set_max_seg_size`:

vb2_dma_contig_set_max_seg_size
===============================

.. c:function:: int vb2_dma_contig_set_max_seg_size(struct device *dev, unsigned int size)

    configure DMA max segment size

    :param struct device \*dev:
        device for configuring DMA parameters

    :param unsigned int size:
        size of DMA max segment size to set

.. _`vb2_dma_contig_set_max_seg_size.description`:

Description
-----------

To allow mapping the scatter-list into a single chunk in the DMA
address space, the device is required to have the DMA max segment
size parameter set to a value larger than the buffer size. Otherwise,
the DMA-mapping subsystem will split the mapping into max segment
size chunks. This function sets the DMA max segment size
parameter to let DMA-mapping map a buffer as a single chunk in DMA
address space.
This code assumes that the DMA-mapping subsystem will merge all
scatterlist segments if this is really possible (for example when
an IOMMU is available and enabled).
Ideally, this parameter should be set by the generic bus code, but it
is left with the default 64KiB value due to historical litmiations in
other subsystems (like limited USB host drivers) and there no good
place to set it to the proper value.
This function should be called from the drivers, which are known to
operate on platforms with IOMMU and provide access to shared buffers
(either USERPTR or DMABUF). This should be done before initializing
videobuf2 queue.

.. This file was automatic generated / don't edit.

