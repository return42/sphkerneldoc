.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_prime.c

.. _`drm_gem_map_attach`:

drm_gem_map_attach
==================

.. c:function:: int drm_gem_map_attach(struct dma_buf *dma_buf, struct device *target_dev, struct dma_buf_attachment *attach)

    dma_buf attach implementation for GEM

    :param struct dma_buf \*dma_buf:
        buffer to attach device to

    :param struct device \*target_dev:
        not used

    :param struct dma_buf_attachment \*attach:
        buffer attachment data

.. _`drm_gem_map_attach.description`:

Description
-----------

Allocates \ :c:type:`struct drm_prime_attachment <drm_prime_attachment>`\  and calls \ :c:type:`drm_driver.gem_prime_pin <drm_driver>`\  for
device specific attachment. This can be used as the \ :c:type:`dma_buf_ops.attach <dma_buf_ops>`\ 
callback.

Returns 0 on success, negative error code on failure.

.. _`drm_gem_map_detach`:

drm_gem_map_detach
==================

.. c:function:: void drm_gem_map_detach(struct dma_buf *dma_buf, struct dma_buf_attachment *attach)

    dma_buf detach implementation for GEM

    :param struct dma_buf \*dma_buf:
        buffer to detach from

    :param struct dma_buf_attachment \*attach:
        attachment to be detached

.. _`drm_gem_map_detach.description`:

Description
-----------

Cleans up \ :c:type:`struct dma_buf_attachment <dma_buf_attachment>`\ . This can be used as the \ :c:type:`dma_buf_ops.detach <dma_buf_ops>`\ 
callback.

.. _`drm_gem_map_dma_buf`:

drm_gem_map_dma_buf
===================

.. c:function:: struct sg_table *drm_gem_map_dma_buf(struct dma_buf_attachment *attach, enum dma_data_direction dir)

    map_dma_buf implementation for GEM

    :param struct dma_buf_attachment \*attach:
        attachment whose scatterlist is to be returned

    :param enum dma_data_direction dir:
        direction of DMA transfer

.. _`drm_gem_map_dma_buf.description`:

Description
-----------

Calls \ :c:type:`drm_driver.gem_prime_get_sg_table <drm_driver>`\  and then maps the scatterlist. This
can be used as the \ :c:type:`dma_buf_ops.map_dma_buf <dma_buf_ops>`\  callback.

Returns sg_table containing the scatterlist to be returned; returns ERR_PTR
on error. May return -EINTR if it is interrupted by a signal.

.. _`drm_gem_unmap_dma_buf`:

drm_gem_unmap_dma_buf
=====================

.. c:function:: void drm_gem_unmap_dma_buf(struct dma_buf_attachment *attach, struct sg_table *sgt, enum dma_data_direction dir)

    unmap_dma_buf implementation for GEM

    :param struct dma_buf_attachment \*attach:
        attachment to unmap buffer from

    :param struct sg_table \*sgt:
        scatterlist info of the buffer to unmap

    :param enum dma_data_direction dir:
        direction of DMA transfer

.. _`drm_gem_unmap_dma_buf.description`:

Description
-----------

Not implemented. The unmap is done at \ :c:func:`drm_gem_map_detach`\ .  This can be
used as the \ :c:type:`dma_buf_ops.unmap_dma_buf <dma_buf_ops>`\  callback.

.. _`drm_gem_dmabuf_export`:

drm_gem_dmabuf_export
=====================

.. c:function:: struct dma_buf *drm_gem_dmabuf_export(struct drm_device *dev, struct dma_buf_export_info *exp_info)

    dma_buf export implementation for GEM

    :param struct drm_device \*dev:
        parent device for the exported dmabuf

    :param struct dma_buf_export_info \*exp_info:
        the export information used by \ :c:func:`dma_buf_export`\ 

.. _`drm_gem_dmabuf_export.description`:

Description
-----------

This wraps \ :c:func:`dma_buf_export`\  for use by generic GEM drivers that are using
\ :c:func:`drm_gem_dmabuf_release`\ . In addition to calling \ :c:func:`dma_buf_export`\ , we take
a reference to the \ :c:type:`struct drm_device <drm_device>`\  and the exported \ :c:type:`struct drm_gem_object <drm_gem_object>`\  (stored in
\ :c:type:`dma_buf_export_info.priv <dma_buf_export_info>`\ ) which is released by \ :c:func:`drm_gem_dmabuf_release`\ .

Returns the new dmabuf.

.. _`drm_gem_dmabuf_release`:

drm_gem_dmabuf_release
======================

.. c:function:: void drm_gem_dmabuf_release(struct dma_buf *dma_buf)

    dma_buf release implementation for GEM

    :param struct dma_buf \*dma_buf:
        buffer to be released

.. _`drm_gem_dmabuf_release.description`:

Description
-----------

Generic release function for dma_bufs exported as PRIME buffers. GEM drivers
must use this in their dma_buf ops structure as the release callback.
\ :c:func:`drm_gem_dmabuf_release`\  should be used in conjunction with
\ :c:func:`drm_gem_dmabuf_export`\ .

.. _`drm_gem_dmabuf_vmap`:

drm_gem_dmabuf_vmap
===================

.. c:function:: void *drm_gem_dmabuf_vmap(struct dma_buf *dma_buf)

    dma_buf vmap implementation for GEM

    :param struct dma_buf \*dma_buf:
        buffer to be mapped

.. _`drm_gem_dmabuf_vmap.description`:

Description
-----------

Sets up a kernel virtual mapping. This can be used as the \ :c:type:`dma_buf_ops.vmap <dma_buf_ops>`\ 
callback.

Returns the kernel virtual address.

.. _`drm_gem_dmabuf_vunmap`:

drm_gem_dmabuf_vunmap
=====================

.. c:function:: void drm_gem_dmabuf_vunmap(struct dma_buf *dma_buf, void *vaddr)

    dma_buf vunmap implementation for GEM

    :param struct dma_buf \*dma_buf:
        buffer to be unmapped

    :param void \*vaddr:
        the virtual address of the buffer

.. _`drm_gem_dmabuf_vunmap.description`:

Description
-----------

Releases a kernel virtual mapping. This can be used as the
\ :c:type:`dma_buf_ops.vunmap <dma_buf_ops>`\  callback.

.. _`drm_gem_dmabuf_kmap_atomic`:

drm_gem_dmabuf_kmap_atomic
==========================

.. c:function:: void *drm_gem_dmabuf_kmap_atomic(struct dma_buf *dma_buf, unsigned long page_num)

    map_atomic implementation for GEM

    :param struct dma_buf \*dma_buf:
        buffer to be mapped

    :param unsigned long page_num:
        page number within the buffer

.. _`drm_gem_dmabuf_kmap_atomic.description`:

Description
-----------

Not implemented. This can be used as the \ :c:type:`dma_buf_ops.map_atomic <dma_buf_ops>`\  callback.

.. _`drm_gem_dmabuf_kunmap_atomic`:

drm_gem_dmabuf_kunmap_atomic
============================

.. c:function:: void drm_gem_dmabuf_kunmap_atomic(struct dma_buf *dma_buf, unsigned long page_num, void *addr)

    unmap_atomic implementation for GEM

    :param struct dma_buf \*dma_buf:
        buffer to be unmapped

    :param unsigned long page_num:
        page number within the buffer

    :param void \*addr:
        virtual address of the buffer

.. _`drm_gem_dmabuf_kunmap_atomic.description`:

Description
-----------

Not implemented. This can be used as the \ :c:type:`dma_buf_ops.unmap_atomic <dma_buf_ops>`\  callback.

.. _`drm_gem_dmabuf_kmap`:

drm_gem_dmabuf_kmap
===================

.. c:function:: void *drm_gem_dmabuf_kmap(struct dma_buf *dma_buf, unsigned long page_num)

    map implementation for GEM

    :param struct dma_buf \*dma_buf:
        buffer to be mapped

    :param unsigned long page_num:
        page number within the buffer

.. _`drm_gem_dmabuf_kmap.description`:

Description
-----------

Not implemented. This can be used as the \ :c:type:`dma_buf_ops.map <dma_buf_ops>`\  callback.

.. _`drm_gem_dmabuf_kunmap`:

drm_gem_dmabuf_kunmap
=====================

.. c:function:: void drm_gem_dmabuf_kunmap(struct dma_buf *dma_buf, unsigned long page_num, void *addr)

    unmap implementation for GEM

    :param struct dma_buf \*dma_buf:
        buffer to be unmapped

    :param unsigned long page_num:
        page number within the buffer

    :param void \*addr:
        virtual address of the buffer

.. _`drm_gem_dmabuf_kunmap.description`:

Description
-----------

Not implemented. This can be used as the \ :c:type:`dma_buf_ops.unmap <dma_buf_ops>`\  callback.

.. _`drm_gem_dmabuf_mmap`:

drm_gem_dmabuf_mmap
===================

.. c:function:: int drm_gem_dmabuf_mmap(struct dma_buf *dma_buf, struct vm_area_struct *vma)

    dma_buf mmap implementation for GEM

    :param struct dma_buf \*dma_buf:
        buffer to be mapped

    :param struct vm_area_struct \*vma:
        virtual address range

.. _`drm_gem_dmabuf_mmap.description`:

Description
-----------

Provides memory mapping for the buffer. This can be used as the
\ :c:type:`dma_buf_ops.mmap <dma_buf_ops>`\  callback.

Returns 0 on success or a negative error code on failure.

.. _`prime-helpers`:

PRIME Helpers
=============

Drivers can implement \ ``gem_prime_export``\  and \ ``gem_prime_import``\  in terms of
simpler APIs by using the helper functions \ ``drm_gem_prime_export``\  and
\ ``drm_gem_prime_import``\ .  These functions implement dma-buf support in terms of
six lower-level driver callbacks:

Export callbacks:

 * \ ``gem_prime_pin``\  (optional): prepare a GEM object for exporting
 * \ ``gem_prime_get_sg_table``\ : provide a scatter/gather table of pinned pages
 * \ ``gem_prime_vmap``\ : vmap a buffer exported by your driver
 * \ ``gem_prime_vunmap``\ : vunmap a buffer exported by your driver
 * \ ``gem_prime_mmap``\  (optional): mmap a buffer exported by your driver

Import callback:

 * \ ``gem_prime_import_sg_table``\  (import): produce a GEM object from another
   driver's scatter/gather table

.. _`drm_gem_prime_export`:

drm_gem_prime_export
====================

.. c:function:: struct dma_buf *drm_gem_prime_export(struct drm_device *dev, struct drm_gem_object *obj, int flags)

    helper library implementation of the export callback

    :param struct drm_device \*dev:
        drm_device to export from

    :param struct drm_gem_object \*obj:
        GEM object to export

    :param int flags:
        flags like DRM_CLOEXEC and DRM_RDWR

.. _`drm_gem_prime_export.description`:

Description
-----------

This is the implementation of the gem_prime_export functions for GEM drivers
using the PRIME helpers.

.. _`drm_gem_prime_handle_to_fd`:

drm_gem_prime_handle_to_fd
==========================

.. c:function:: int drm_gem_prime_handle_to_fd(struct drm_device *dev, struct drm_file *file_priv, uint32_t handle, uint32_t flags, int *prime_fd)

    PRIME export function for GEM drivers

    :param struct drm_device \*dev:
        dev to export the buffer from

    :param struct drm_file \*file_priv:
        drm file-private structure

    :param uint32_t handle:
        buffer handle to export

    :param uint32_t flags:
        flags like DRM_CLOEXEC

    :param int \*prime_fd:
        pointer to storage for the fd id of the create dma-buf

.. _`drm_gem_prime_handle_to_fd.description`:

Description
-----------

This is the PRIME export function which must be used mandatorily by GEM
drivers to ensure correct lifetime management of the underlying GEM object.
The actual exporting from GEM object to a dma-buf is done through the
gem_prime_export driver callback.

.. _`drm_gem_prime_import_dev`:

drm_gem_prime_import_dev
========================

.. c:function:: struct drm_gem_object *drm_gem_prime_import_dev(struct drm_device *dev, struct dma_buf *dma_buf, struct device *attach_dev)

    core implementation of the import callback

    :param struct drm_device \*dev:
        drm_device to import into

    :param struct dma_buf \*dma_buf:
        dma-buf object to import

    :param struct device \*attach_dev:
        struct device to dma_buf attach

.. _`drm_gem_prime_import_dev.description`:

Description
-----------

This is the core of drm_gem_prime_import. It's designed to be called by
drivers who want to use a different device structure than dev->dev for
attaching via dma_buf.

.. _`drm_gem_prime_import`:

drm_gem_prime_import
====================

.. c:function:: struct drm_gem_object *drm_gem_prime_import(struct drm_device *dev, struct dma_buf *dma_buf)

    helper library implementation of the import callback

    :param struct drm_device \*dev:
        drm_device to import into

    :param struct dma_buf \*dma_buf:
        dma-buf object to import

.. _`drm_gem_prime_import.description`:

Description
-----------

This is the implementation of the gem_prime_import functions for GEM drivers
using the PRIME helpers.

.. _`drm_gem_prime_fd_to_handle`:

drm_gem_prime_fd_to_handle
==========================

.. c:function:: int drm_gem_prime_fd_to_handle(struct drm_device *dev, struct drm_file *file_priv, int prime_fd, uint32_t *handle)

    PRIME import function for GEM drivers

    :param struct drm_device \*dev:
        dev to export the buffer from

    :param struct drm_file \*file_priv:
        drm file-private structure

    :param int prime_fd:
        fd id of the dma-buf which should be imported

    :param uint32_t \*handle:
        pointer to storage for the handle of the imported buffer object

.. _`drm_gem_prime_fd_to_handle.description`:

Description
-----------

This is the PRIME import function which must be used mandatorily by GEM
drivers to ensure correct lifetime management of the underlying GEM object.
The actual importing of GEM object from the dma-buf is done through the
gem_import_export driver callback.

.. _`drm_prime_pages_to_sg`:

drm_prime_pages_to_sg
=====================

.. c:function:: struct sg_table *drm_prime_pages_to_sg(struct page **pages, unsigned int nr_pages)

    converts a page array into an sg list

    :param struct page \*\*pages:
        pointer to the array of page pointers to convert

    :param unsigned int nr_pages:
        length of the page vector

.. _`drm_prime_pages_to_sg.description`:

Description
-----------

This helper creates an sg table object from a set of pages
the driver is responsible for mapping the pages into the
importers address space for use with dma_buf itself.

.. _`drm_prime_sg_to_page_addr_arrays`:

drm_prime_sg_to_page_addr_arrays
================================

.. c:function:: int drm_prime_sg_to_page_addr_arrays(struct sg_table *sgt, struct page **pages, dma_addr_t *addrs, int max_entries)

    convert an sg table into a page array

    :param struct sg_table \*sgt:
        scatter-gather table to convert

    :param struct page \*\*pages:
        optional array of page pointers to store the page array in

    :param dma_addr_t \*addrs:
        optional array to store the dma bus address of each page

    :param int max_entries:
        size of both the passed-in arrays

.. _`drm_prime_sg_to_page_addr_arrays.description`:

Description
-----------

Exports an sg table into an array of pages and addresses. This is currently
required by the TTM driver in order to do correct fault handling.

.. _`drm_prime_gem_destroy`:

drm_prime_gem_destroy
=====================

.. c:function:: void drm_prime_gem_destroy(struct drm_gem_object *obj, struct sg_table *sg)

    helper to clean up a PRIME-imported GEM object

    :param struct drm_gem_object \*obj:
        GEM object which was created from a dma-buf

    :param struct sg_table \*sg:
        the sg-table which was pinned at import time

.. _`drm_prime_gem_destroy.description`:

Description
-----------

This is the cleanup functions which GEM drivers need to call when they use
\ ``drm_gem_prime_import``\  to import dma-bufs.

.. This file was automatic generated / don't edit.

