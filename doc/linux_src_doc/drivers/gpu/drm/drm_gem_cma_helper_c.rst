.. -*- coding: utf-8; mode: rst -*-

====================
drm_gem_cma_helper.c
====================



.. _xref___drm_gem_cma_create:

__drm_gem_cma_create
====================

.. c:function:: struct drm_gem_cma_object * __drm_gem_cma_create (struct drm_device * drm, size_t size)

    Create a GEM CMA object without allocating memory

    :param struct drm_device * drm:
        DRM device

    :param size_t size:
        size of the object to allocate



Description
-----------

This function creates and initializes a GEM CMA object of the given size,
but doesn't allocate any memory to back the object.



Returns
-------

A struct drm_gem_cma_object * on success or an :c:func:`ERR_PTR`-encoded negative
error code on failure.




.. _xref_drm_gem_cma_create:

drm_gem_cma_create
==================

.. c:function:: struct drm_gem_cma_object * drm_gem_cma_create (struct drm_device * drm, size_t size)

    allocate an object with the given size

    :param struct drm_device * drm:
        DRM device

    :param size_t size:
        size of the object to allocate



Description
-----------

This function creates a CMA GEM object and allocates a contiguous chunk of
memory as backing store. The backing memory has the writecombine attribute
set.



Returns
-------

A struct drm_gem_cma_object * on success or an :c:func:`ERR_PTR`-encoded negative
error code on failure.




.. _xref_drm_gem_cma_create_with_handle:

drm_gem_cma_create_with_handle
==============================

.. c:function:: struct drm_gem_cma_object * drm_gem_cma_create_with_handle (struct drm_file * file_priv, struct drm_device * drm, size_t size, uint32_t * handle)

    allocate an object with the given size and return a GEM handle to it

    :param struct drm_file * file_priv:
        DRM file-private structure to register the handle for

    :param struct drm_device * drm:
        DRM device

    :param size_t size:
        size of the object to allocate

    :param uint32_t * handle:
        return location for the GEM handle



Description
-----------

This function creates a CMA GEM object, allocating a physically contiguous
chunk of memory as backing store. The GEM object is then added to the list
of object associated with the given file and a handle to it is returned.



Returns
-------

A struct drm_gem_cma_object * on success or an :c:func:`ERR_PTR`-encoded negative
error code on failure.




.. _xref_drm_gem_cma_free_object:

drm_gem_cma_free_object
=======================

.. c:function:: void drm_gem_cma_free_object (struct drm_gem_object * gem_obj)

    free resources associated with a CMA GEM object

    :param struct drm_gem_object * gem_obj:
        GEM object to free



Description
-----------

This function frees the backing memory of the CMA GEM object, cleans up the
GEM object state and frees the memory used to store the object itself.
Drivers using the CMA helpers should set this as their DRM driver's
->:c:func:`gem_free_object` callback.




.. _xref_drm_gem_cma_dumb_create_internal:

drm_gem_cma_dumb_create_internal
================================

.. c:function:: int drm_gem_cma_dumb_create_internal (struct drm_file * file_priv, struct drm_device * drm, struct drm_mode_create_dumb * args)

    create a dumb buffer object

    :param struct drm_file * file_priv:
        DRM file-private structure to create the dumb buffer for

    :param struct drm_device * drm:
        DRM device

    :param struct drm_mode_create_dumb * args:
        IOCTL data



Description
-----------

This aligns the pitch and size arguments to the minimum required. This is
an internal helper that can be wrapped by a driver to account for hardware
with more specific alignment requirements. It should not be used directly
as the ->:c:func:`dumb_create` callback in a DRM driver.



Returns
-------

0 on success or a negative error code on failure.




.. _xref_drm_gem_cma_dumb_create:

drm_gem_cma_dumb_create
=======================

.. c:function:: int drm_gem_cma_dumb_create (struct drm_file * file_priv, struct drm_device * drm, struct drm_mode_create_dumb * args)

    create a dumb buffer object

    :param struct drm_file * file_priv:
        DRM file-private structure to create the dumb buffer for

    :param struct drm_device * drm:
        DRM device

    :param struct drm_mode_create_dumb * args:
        IOCTL data



Description
-----------

This function computes the pitch of the dumb buffer and rounds it up to an
integer number of bytes per pixel. Drivers for hardware that doesn't have
any additional restrictions on the pitch can directly use this function as
their ->:c:func:`dumb_create` callback.


For hardware with additional restrictions, drivers can adjust the fields
set up by userspace and pass the IOCTL data along to the
:c:func:`drm_gem_cma_dumb_create_internal` function.



Returns
-------

0 on success or a negative error code on failure.




.. _xref_drm_gem_cma_dumb_map_offset:

drm_gem_cma_dumb_map_offset
===========================

.. c:function:: int drm_gem_cma_dumb_map_offset (struct drm_file * file_priv, struct drm_device * drm, u32 handle, u64 * offset)

    return the fake mmap offset for a CMA GEM object

    :param struct drm_file * file_priv:
        DRM file-private structure containing the GEM object

    :param struct drm_device * drm:
        DRM device

    :param u32 handle:
        GEM object handle

    :param u64 * offset:
        return location for the fake mmap offset



Description
-----------

This function look up an object by its handle and returns the fake mmap
offset associated with it. Drivers using the CMA helpers should set this
as their DRM driver's ->:c:func:`dumb_map_offset` callback.



Returns
-------

0 on success or a negative error code on failure.




.. _xref_drm_gem_cma_mmap:

drm_gem_cma_mmap
================

.. c:function:: int drm_gem_cma_mmap (struct file * filp, struct vm_area_struct * vma)

    memory-map a CMA GEM object

    :param struct file * filp:
        file object

    :param struct vm_area_struct * vma:
        VMA for the area to be mapped



Description
-----------

This function implements an augmented version of the GEM DRM file mmap



operation for CMA objects
-------------------------

In addition to the usual GEM VMA setup it
immediately faults in the entire object instead of using on-demaind
faulting. Drivers which employ the CMA helpers should use this function
as their ->:c:func:`mmap` handler in the DRM device file's file_operations
structure.



Returns
-------

0 on success or a negative error code on failure.




.. _xref_drm_gem_cma_describe:

drm_gem_cma_describe
====================

.. c:function:: void drm_gem_cma_describe (struct drm_gem_cma_object * cma_obj, struct seq_file * m)

    describe a CMA GEM object for debugfs

    :param struct drm_gem_cma_object * cma_obj:
        CMA GEM object

    :param struct seq_file * m:
        debugfs file handle



Description
-----------

This function can be used to dump a human-readable representation of the
CMA GEM object into a synthetic file.




.. _xref_drm_gem_cma_prime_get_sg_table:

drm_gem_cma_prime_get_sg_table
==============================

.. c:function:: struct sg_table * drm_gem_cma_prime_get_sg_table (struct drm_gem_object * obj)

    provide a scatter/gather table of pinned pages for a CMA GEM object

    :param struct drm_gem_object * obj:
        GEM object



Description
-----------

This function exports a scatter/gather table suitable for PRIME usage by
calling the standard DMA mapping API. Drivers using the CMA helpers should
set this as their DRM driver's ->:c:func:`gem_prime_get_sg_table` callback.



Returns
-------

A pointer to the scatter/gather table of pinned pages or NULL on failure.




.. _xref_drm_gem_cma_prime_import_sg_table:

drm_gem_cma_prime_import_sg_table
=================================

.. c:function:: struct drm_gem_object * drm_gem_cma_prime_import_sg_table (struct drm_device * dev, struct dma_buf_attachment * attach, struct sg_table * sgt)

    produce a CMA GEM object from another driver's scatter/gather table of pinned pages

    :param struct drm_device * dev:
        device to import into

    :param struct dma_buf_attachment * attach:
        DMA-BUF attachment

    :param struct sg_table * sgt:
        scatter/gather table of pinned pages



Description
-----------

This function imports a scatter/gather table exported via DMA-BUF by
another driver. Imported buffers must be physically contiguous in memory
(i.e. the scatter/gather table must contain a single entry). Drivers that
use the CMA helpers should set this as their DRM driver's
->:c:func:`gem_prime_import_sg_table` callback.



Returns
-------

A pointer to a newly created GEM object or an ERR_PTR-encoded negative
error code on failure.




.. _xref_drm_gem_cma_prime_mmap:

drm_gem_cma_prime_mmap
======================

.. c:function:: int drm_gem_cma_prime_mmap (struct drm_gem_object * obj, struct vm_area_struct * vma)

    memory-map an exported CMA GEM object

    :param struct drm_gem_object * obj:
        GEM object

    :param struct vm_area_struct * vma:
        VMA for the area to be mapped



Description
-----------

This function maps a buffer imported via DRM PRIME into a userspace
process's address space. Drivers that use the CMA helpers should set this
as their DRM driver's ->:c:func:`gem_prime_mmap` callback.



Returns
-------

0 on success or a negative error code on failure.




.. _xref_drm_gem_cma_prime_vmap:

drm_gem_cma_prime_vmap
======================

.. c:function:: void * drm_gem_cma_prime_vmap (struct drm_gem_object * obj)

    map a CMA GEM object into the kernel's virtual address space

    :param struct drm_gem_object * obj:
        GEM object



Description
-----------

This function maps a buffer exported via DRM PRIME into the kernel's
virtual address space. Since the CMA buffers are already mapped into the
kernel virtual address space this simply returns the cached virtual
address. Drivers using the CMA helpers should set this as their DRM
driver's ->:c:func:`gem_prime_vmap` callback.



Returns
-------

The kernel virtual address of the CMA GEM object's backing store.




.. _xref_drm_gem_cma_prime_vunmap:

drm_gem_cma_prime_vunmap
========================

.. c:function:: void drm_gem_cma_prime_vunmap (struct drm_gem_object * obj, void * vaddr)

    unmap a CMA GEM object from the kernel's virtual address space

    :param struct drm_gem_object * obj:
        GEM object

    :param void * vaddr:
        kernel virtual address where the CMA GEM object was mapped



Description
-----------

This function removes a buffer exported via DRM PRIME from the kernel's
virtual address space. This is a no-op because CMA buffers cannot be
unmapped from kernel space. Drivers using the CMA helpers should set this
as their DRM driver's ->:c:func:`gem_prime_vunmap` callback.


