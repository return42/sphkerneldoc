.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_prime.c

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

.. c:function:: int drm_prime_sg_to_page_addr_arrays(struct sg_table *sgt, struct page **pages, dma_addr_t *addrs, int max_pages)

    convert an sg table into a page array

    :param struct sg_table \*sgt:
        scatter-gather table to convert

    :param struct page \*\*pages:
        array of page pointers to store the page array in

    :param dma_addr_t \*addrs:
        optional array to store the dma bus address of each page

    :param int max_pages:
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

