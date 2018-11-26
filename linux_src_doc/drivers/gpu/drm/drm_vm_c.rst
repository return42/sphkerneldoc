.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_vm.c

.. _`drm_mmap_dma`:

drm_mmap_dma
============

.. c:function:: int drm_mmap_dma(struct file *filp, struct vm_area_struct *vma)

    :param filp:
        *undescribed*
    :type filp: struct file \*

    :param vma:
        *undescribed*
    :type vma: struct vm_area_struct \*

.. _`drm_mmap_dma.description`:

Description
-----------

\param file_priv DRM file private.
\param vma virtual memory area.
\return zero on success or a negative number on failure.

Sets the virtual memory area operations structure to vm_dma_ops, the file
pointer, and calls \ :c:func:`vm_open`\ .

.. _`drm_mmap_locked`:

drm_mmap_locked
===============

.. c:function:: int drm_mmap_locked(struct file *filp, struct vm_area_struct *vma)

    :param filp:
        *undescribed*
    :type filp: struct file \*

    :param vma:
        *undescribed*
    :type vma: struct vm_area_struct \*

.. _`drm_mmap_locked.description`:

Description
-----------

\param file_priv DRM file private.
\param vma virtual memory area.
\return zero on success or a negative number on failure.

If the virtual memory area has no offset associated with it then it's a DMA
area, so calls \ :c:func:`mmap_dma`\ . Otherwise searches the map in drm_device::maplist,
checks that the restricted flag is not set, sets the virtual memory operations
according to the mapping type and remaps the pages. Finally sets the file
pointer and calls \ :c:func:`vm_open`\ .

.. This file was automatic generated / don't edit.

