.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_gem_cma_helper.c

.. _`cma-helpers`:

cma helpers
===========

The Contiguous Memory Allocator reserves a pool of memory at early boot
that is used to service requests for large blocks of contiguous memory.

The DRM GEM/CMA helpers use this allocator as a means to provide buffer
objects that are physically contiguous in memory. This is useful for
display drivers that are unable to map scattered buffers via an IOMMU.

.. _`__drm_gem_cma_create`:

__drm_gem_cma_create
====================

.. c:function:: struct drm_gem_cma_object *__drm_gem_cma_create(struct drm_device *drm, size_t size)

    Create a GEM CMA object without allocating memory

    :param struct drm_device \*drm:
        DRM device

    :param size_t size:
        size of the object to allocate

.. _`__drm_gem_cma_create.description`:

Description
-----------

This function creates and initializes a GEM CMA object of the given size,
but doesn't allocate any memory to back the object.

.. _`__drm_gem_cma_create.return`:

Return
------

A struct drm_gem_cma_object * on success or an \ :c:func:`ERR_PTR`\ -encoded negative
error code on failure.

.. _`drm_gem_cma_create`:

drm_gem_cma_create
==================

.. c:function:: struct drm_gem_cma_object *drm_gem_cma_create(struct drm_device *drm, size_t size)

    allocate an object with the given size

    :param struct drm_device \*drm:
        DRM device

    :param size_t size:
        size of the object to allocate

.. _`drm_gem_cma_create.description`:

Description
-----------

This function creates a CMA GEM object and allocates a contiguous chunk of
memory as backing store. The backing memory has the writecombine attribute
set.

.. _`drm_gem_cma_create.return`:

Return
------

A struct drm_gem_cma_object * on success or an \ :c:func:`ERR_PTR`\ -encoded negative
error code on failure.

.. _`drm_gem_cma_create_with_handle`:

drm_gem_cma_create_with_handle
==============================

.. c:function:: struct drm_gem_cma_object *drm_gem_cma_create_with_handle(struct drm_file *file_priv, struct drm_device *drm, size_t size, uint32_t *handle)

    allocate an object with the given size and return a GEM handle to it

    :param struct drm_file \*file_priv:
        DRM file-private structure to register the handle for

    :param struct drm_device \*drm:
        DRM device

    :param size_t size:
        size of the object to allocate

    :param uint32_t \*handle:
        return location for the GEM handle

.. _`drm_gem_cma_create_with_handle.description`:

Description
-----------

This function creates a CMA GEM object, allocating a physically contiguous
chunk of memory as backing store. The GEM object is then added to the list
of object associated with the given file and a handle to it is returned.

.. _`drm_gem_cma_create_with_handle.return`:

Return
------

A struct drm_gem_cma_object * on success or an \ :c:func:`ERR_PTR`\ -encoded negative
error code on failure.

.. _`drm_gem_cma_free_object`:

drm_gem_cma_free_object
=======================

.. c:function:: void drm_gem_cma_free_object(struct drm_gem_object *gem_obj)

    free resources associated with a CMA GEM object

    :param struct drm_gem_object \*gem_obj:
        GEM object to free

.. _`drm_gem_cma_free_object.description`:

Description
-----------

This function frees the backing memory of the CMA GEM object, cleans up the
GEM object state and frees the memory used to store the object itself.
Drivers using the CMA helpers should set this as their
\ :c:type:`drm_driver.gem_free_object_unlocked <drm_driver>`\  callback.

.. _`drm_gem_cma_dumb_create_internal`:

drm_gem_cma_dumb_create_internal
================================

.. c:function:: int drm_gem_cma_dumb_create_internal(struct drm_file *file_priv, struct drm_device *drm, struct drm_mode_create_dumb *args)

    create a dumb buffer object

    :param struct drm_file \*file_priv:
        DRM file-private structure to create the dumb buffer for

    :param struct drm_device \*drm:
        DRM device

    :param struct drm_mode_create_dumb \*args:
        IOCTL data

.. _`drm_gem_cma_dumb_create_internal.description`:

Description
-----------

This aligns the pitch and size arguments to the minimum required. This is
an internal helper that can be wrapped by a driver to account for hardware
with more specific alignment requirements. It should not be used directly
as their \ :c:type:`drm_driver.dumb_create <drm_driver>`\  callback.

.. _`drm_gem_cma_dumb_create_internal.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_gem_cma_dumb_create`:

drm_gem_cma_dumb_create
=======================

.. c:function:: int drm_gem_cma_dumb_create(struct drm_file *file_priv, struct drm_device *drm, struct drm_mode_create_dumb *args)

    create a dumb buffer object

    :param struct drm_file \*file_priv:
        DRM file-private structure to create the dumb buffer for

    :param struct drm_device \*drm:
        DRM device

    :param struct drm_mode_create_dumb \*args:
        IOCTL data

.. _`drm_gem_cma_dumb_create.description`:

Description
-----------

This function computes the pitch of the dumb buffer and rounds it up to an
integer number of bytes per pixel. Drivers for hardware that doesn't have
any additional restrictions on the pitch can directly use this function as
their \ :c:type:`drm_driver.dumb_create <drm_driver>`\  callback.

For hardware with additional restrictions, drivers can adjust the fields
set up by userspace and pass the IOCTL data along to the
\ :c:func:`drm_gem_cma_dumb_create_internal`\  function.

.. _`drm_gem_cma_dumb_create.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_gem_cma_mmap`:

drm_gem_cma_mmap
================

.. c:function:: int drm_gem_cma_mmap(struct file *filp, struct vm_area_struct *vma)

    memory-map a CMA GEM object

    :param struct file \*filp:
        file object

    :param struct vm_area_struct \*vma:
        VMA for the area to be mapped

.. _`drm_gem_cma_mmap.description`:

Description
-----------

This function implements an augmented version of the GEM DRM file mmap
operation for CMA objects: In addition to the usual GEM VMA setup it
immediately faults in the entire object instead of using on-demaind
faulting. Drivers which employ the CMA helpers should use this function
as their ->mmap() handler in the DRM device file's file_operations
structure.

Instead of directly referencing this function, drivers should use the
\ :c:func:`DEFINE_DRM_GEM_CMA_FOPS`\ .macro.

.. _`drm_gem_cma_mmap.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_gem_cma_get_unmapped_area`:

drm_gem_cma_get_unmapped_area
=============================

.. c:function:: unsigned long drm_gem_cma_get_unmapped_area(struct file *filp, unsigned long addr, unsigned long len, unsigned long pgoff, unsigned long flags)

    propose address for mapping in noMMU cases

    :param struct file \*filp:
        file object

    :param unsigned long addr:
        memory address

    :param unsigned long len:
        buffer size

    :param unsigned long pgoff:
        page offset

    :param unsigned long flags:
        memory flags

.. _`drm_gem_cma_get_unmapped_area.description`:

Description
-----------

This function is used in noMMU platforms to propose address mapping
for a given buffer.
It's intended to be used as a direct handler for the struct
\ :c:type:`file_operations.get_unmapped_area <file_operations>`\  operation.

.. _`drm_gem_cma_get_unmapped_area.return`:

Return
------

mapping address on success or a negative error code on failure.

.. _`drm_gem_cma_print_info`:

drm_gem_cma_print_info
======================

.. c:function:: void drm_gem_cma_print_info(struct drm_printer *p, unsigned int indent, const struct drm_gem_object *obj)

    Print \ :c:type:`struct drm_gem_cma_object <drm_gem_cma_object>`\  info for debugfs

    :param struct drm_printer \*p:
        DRM printer

    :param unsigned int indent:
        Tab indentation level

    :param const struct drm_gem_object \*obj:
        GEM object

.. _`drm_gem_cma_print_info.description`:

Description
-----------

This function can be used as the \ :c:type:`drm_driver->gem_print_info <drm_driver>`\  callback.
It prints paddr and vaddr for use in e.g. debugfs output.

.. _`drm_gem_cma_prime_get_sg_table`:

drm_gem_cma_prime_get_sg_table
==============================

.. c:function:: struct sg_table *drm_gem_cma_prime_get_sg_table(struct drm_gem_object *obj)

    provide a scatter/gather table of pinned pages for a CMA GEM object

    :param struct drm_gem_object \*obj:
        GEM object

.. _`drm_gem_cma_prime_get_sg_table.description`:

Description
-----------

This function exports a scatter/gather table suitable for PRIME usage by
calling the standard DMA mapping API. Drivers using the CMA helpers should
set this as their \ :c:type:`drm_driver.gem_prime_get_sg_table <drm_driver>`\  callback.

.. _`drm_gem_cma_prime_get_sg_table.return`:

Return
------

A pointer to the scatter/gather table of pinned pages or NULL on failure.

.. _`drm_gem_cma_prime_import_sg_table`:

drm_gem_cma_prime_import_sg_table
=================================

.. c:function:: struct drm_gem_object *drm_gem_cma_prime_import_sg_table(struct drm_device *dev, struct dma_buf_attachment *attach, struct sg_table *sgt)

    produce a CMA GEM object from another driver's scatter/gather table of pinned pages

    :param struct drm_device \*dev:
        device to import into

    :param struct dma_buf_attachment \*attach:
        DMA-BUF attachment

    :param struct sg_table \*sgt:
        scatter/gather table of pinned pages

.. _`drm_gem_cma_prime_import_sg_table.description`:

Description
-----------

This function imports a scatter/gather table exported via DMA-BUF by
another driver. Imported buffers must be physically contiguous in memory
(i.e. the scatter/gather table must contain a single entry). Drivers that
use the CMA helpers should set this as their
\ :c:type:`drm_driver.gem_prime_import_sg_table <drm_driver>`\  callback.

.. _`drm_gem_cma_prime_import_sg_table.return`:

Return
------

A pointer to a newly created GEM object or an ERR_PTR-encoded negative
error code on failure.

.. _`drm_gem_cma_prime_mmap`:

drm_gem_cma_prime_mmap
======================

.. c:function:: int drm_gem_cma_prime_mmap(struct drm_gem_object *obj, struct vm_area_struct *vma)

    memory-map an exported CMA GEM object

    :param struct drm_gem_object \*obj:
        GEM object

    :param struct vm_area_struct \*vma:
        VMA for the area to be mapped

.. _`drm_gem_cma_prime_mmap.description`:

Description
-----------

This function maps a buffer imported via DRM PRIME into a userspace
process's address space. Drivers that use the CMA helpers should set this
as their \ :c:type:`drm_driver.gem_prime_mmap <drm_driver>`\  callback.

.. _`drm_gem_cma_prime_mmap.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_gem_cma_prime_vmap`:

drm_gem_cma_prime_vmap
======================

.. c:function:: void *drm_gem_cma_prime_vmap(struct drm_gem_object *obj)

    map a CMA GEM object into the kernel's virtual address space

    :param struct drm_gem_object \*obj:
        GEM object

.. _`drm_gem_cma_prime_vmap.description`:

Description
-----------

This function maps a buffer exported via DRM PRIME into the kernel's
virtual address space. Since the CMA buffers are already mapped into the
kernel virtual address space this simply returns the cached virtual
address. Drivers using the CMA helpers should set this as their DRM
driver's \ :c:type:`drm_driver.gem_prime_vmap <drm_driver>`\  callback.

.. _`drm_gem_cma_prime_vmap.return`:

Return
------

The kernel virtual address of the CMA GEM object's backing store.

.. _`drm_gem_cma_prime_vunmap`:

drm_gem_cma_prime_vunmap
========================

.. c:function:: void drm_gem_cma_prime_vunmap(struct drm_gem_object *obj, void *vaddr)

    unmap a CMA GEM object from the kernel's virtual address space

    :param struct drm_gem_object \*obj:
        GEM object

    :param void \*vaddr:
        kernel virtual address where the CMA GEM object was mapped

.. _`drm_gem_cma_prime_vunmap.description`:

Description
-----------

This function removes a buffer exported via DRM PRIME from the kernel's
virtual address space. This is a no-op because CMA buffers cannot be
unmapped from kernel space. Drivers using the CMA helpers should set this
as their \ :c:type:`drm_driver.gem_prime_vunmap <drm_driver>`\  callback.

.. This file was automatic generated / don't edit.

