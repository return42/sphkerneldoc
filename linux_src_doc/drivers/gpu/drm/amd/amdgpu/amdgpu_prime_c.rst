.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_prime.c

.. _`prime-buffer-sharing`:

PRIME Buffer Sharing
====================

The following callback implementations are used for :ref:`sharing GEM buffer
objects between different devices via PRIME <prime_buffer_sharing>`.

.. _`amdgpu_gem_prime_get_sg_table`:

amdgpu_gem_prime_get_sg_table
=============================

.. c:function:: struct sg_table *amdgpu_gem_prime_get_sg_table(struct drm_gem_object *obj)

    \ :c:type:`drm_driver.gem_prime_get_sg_table <drm_driver>`\  implementation

    :param obj:
        GEM buffer object (BO)
    :type obj: struct drm_gem_object \*

.. _`amdgpu_gem_prime_get_sg_table.return`:

Return
------

A scatter/gather table for the pinned pages of the BO's memory.

.. _`amdgpu_gem_prime_vmap`:

amdgpu_gem_prime_vmap
=====================

.. c:function:: void *amdgpu_gem_prime_vmap(struct drm_gem_object *obj)

    \ :c:type:`dma_buf_ops.vmap <dma_buf_ops>`\  implementation

    :param obj:
        GEM BO
    :type obj: struct drm_gem_object \*

.. _`amdgpu_gem_prime_vmap.description`:

Description
-----------

Sets up an in-kernel virtual mapping of the BO's memory.

.. _`amdgpu_gem_prime_vmap.return`:

Return
------

The virtual address of the mapping or an error pointer.

.. _`amdgpu_gem_prime_vunmap`:

amdgpu_gem_prime_vunmap
=======================

.. c:function:: void amdgpu_gem_prime_vunmap(struct drm_gem_object *obj, void *vaddr)

    \ :c:type:`dma_buf_ops.vunmap <dma_buf_ops>`\  implementation

    :param obj:
        GEM BO
    :type obj: struct drm_gem_object \*

    :param vaddr:
        Virtual address (unused)
    :type vaddr: void \*

.. _`amdgpu_gem_prime_vunmap.description`:

Description
-----------

Tears down the in-kernel virtual mapping of the BO's memory.

.. _`amdgpu_gem_prime_mmap`:

amdgpu_gem_prime_mmap
=====================

.. c:function:: int amdgpu_gem_prime_mmap(struct drm_gem_object *obj, struct vm_area_struct *vma)

    \ :c:type:`drm_driver.gem_prime_mmap <drm_driver>`\  implementation

    :param obj:
        GEM BO
    :type obj: struct drm_gem_object \*

    :param vma:
        Virtual memory area
    :type vma: struct vm_area_struct \*

.. _`amdgpu_gem_prime_mmap.description`:

Description
-----------

Sets up a userspace mapping of the BO's memory in the given
virtual memory area.

.. _`amdgpu_gem_prime_mmap.return`:

Return
------

0 on success or a negative error code on failure.

.. _`amdgpu_gem_prime_import_sg_table`:

amdgpu_gem_prime_import_sg_table
================================

.. c:function:: struct drm_gem_object *amdgpu_gem_prime_import_sg_table(struct drm_device *dev, struct dma_buf_attachment *attach, struct sg_table *sg)

    \ :c:type:`drm_driver.gem_prime_import_sg_table <drm_driver>`\  implementation

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param attach:
        DMA-buf attachment
    :type attach: struct dma_buf_attachment \*

    :param sg:
        Scatter/gather table
    :type sg: struct sg_table \*

.. _`amdgpu_gem_prime_import_sg_table.description`:

Description
-----------

Imports shared DMA buffer memory exported by another device.

.. _`amdgpu_gem_prime_import_sg_table.return`:

Return
------

A new GEM BO of the given DRM device, representing the memory
described by the given DMA-buf attachment and scatter/gather table.

.. _`amdgpu_gem_map_attach`:

amdgpu_gem_map_attach
=====================

.. c:function:: int amdgpu_gem_map_attach(struct dma_buf *dma_buf, struct dma_buf_attachment *attach)

    \ :c:type:`dma_buf_ops.attach <dma_buf_ops>`\  implementation

    :param dma_buf:
        Shared DMA buffer
    :type dma_buf: struct dma_buf \*

    :param attach:
        DMA-buf attachment
    :type attach: struct dma_buf_attachment \*

.. _`amdgpu_gem_map_attach.description`:

Description
-----------

Makes sure that the shared DMA buffer can be accessed by the target device.
For now, simply pins it to the GTT domain, where it should be accessible by
all DMA devices.

.. _`amdgpu_gem_map_attach.return`:

Return
------

0 on success or a negative error code on failure.

.. _`amdgpu_gem_map_detach`:

amdgpu_gem_map_detach
=====================

.. c:function:: void amdgpu_gem_map_detach(struct dma_buf *dma_buf, struct dma_buf_attachment *attach)

    \ :c:type:`dma_buf_ops.detach <dma_buf_ops>`\  implementation

    :param dma_buf:
        Shared DMA buffer
    :type dma_buf: struct dma_buf \*

    :param attach:
        DMA-buf attachment
    :type attach: struct dma_buf_attachment \*

.. _`amdgpu_gem_map_detach.description`:

Description
-----------

This is called when a shared DMA buffer no longer needs to be accessible by
another device. For now, simply unpins the buffer from GTT.

.. _`amdgpu_gem_prime_res_obj`:

amdgpu_gem_prime_res_obj
========================

.. c:function:: struct reservation_object *amdgpu_gem_prime_res_obj(struct drm_gem_object *obj)

    \ :c:type:`drm_driver.gem_prime_res_obj <drm_driver>`\  implementation

    :param obj:
        GEM BO
    :type obj: struct drm_gem_object \*

.. _`amdgpu_gem_prime_res_obj.return`:

Return
------

The BO's reservation object.

.. _`amdgpu_gem_begin_cpu_access`:

amdgpu_gem_begin_cpu_access
===========================

.. c:function:: int amdgpu_gem_begin_cpu_access(struct dma_buf *dma_buf, enum dma_data_direction direction)

    \ :c:type:`dma_buf_ops.begin_cpu_access <dma_buf_ops>`\  implementation

    :param dma_buf:
        Shared DMA buffer
    :type dma_buf: struct dma_buf \*

    :param direction:
        Direction of DMA transfer
    :type direction: enum dma_data_direction

.. _`amdgpu_gem_begin_cpu_access.description`:

Description
-----------

This is called before CPU access to the shared DMA buffer's memory. If it's
a read access, the buffer is moved to the GTT domain if possible, for optimal
CPU read performance.

.. _`amdgpu_gem_begin_cpu_access.return`:

Return
------

0 on success or a negative error code on failure.

.. _`amdgpu_gem_prime_export`:

amdgpu_gem_prime_export
=======================

.. c:function:: struct dma_buf *amdgpu_gem_prime_export(struct drm_device *dev, struct drm_gem_object *gobj, int flags)

    \ :c:type:`drm_driver.gem_prime_export <drm_driver>`\  implementation

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param gobj:
        GEM BO
    :type gobj: struct drm_gem_object \*

    :param flags:
        Flags such as DRM_CLOEXEC and DRM_RDWR.
    :type flags: int

.. _`amdgpu_gem_prime_export.description`:

Description
-----------

The main work is done by the \ :c:type:`struct drm_gem_prime_export <drm_gem_prime_export>`\  helper, which in turn
uses \ :c:type:`struct amdgpu_gem_prime_res_obj <amdgpu_gem_prime_res_obj>`\ .

.. _`amdgpu_gem_prime_export.return`:

Return
------

Shared DMA buffer representing the GEM BO from the given device.

.. _`amdgpu_gem_prime_import`:

amdgpu_gem_prime_import
=======================

.. c:function:: struct drm_gem_object *amdgpu_gem_prime_import(struct drm_device *dev, struct dma_buf *dma_buf)

    \ :c:type:`drm_driver.gem_prime_import <drm_driver>`\  implementation

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param dma_buf:
        Shared DMA buffer
    :type dma_buf: struct dma_buf \*

.. _`amdgpu_gem_prime_import.description`:

Description
-----------

The main work is done by the \ :c:type:`struct drm_gem_prime_import <drm_gem_prime_import>`\  helper, which in turn
uses \ :c:type:`struct amdgpu_gem_prime_import_sg_table <amdgpu_gem_prime_import_sg_table>`\ .

.. _`amdgpu_gem_prime_import.return`:

Return
------

GEM BO representing the shared DMA buffer for the given device.

.. This file was automatic generated / don't edit.

