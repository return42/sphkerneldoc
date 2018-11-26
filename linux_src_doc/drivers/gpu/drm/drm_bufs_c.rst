.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_bufs.c

.. _`drm_addmap_core`:

drm_addmap_core
===============

.. c:function:: int drm_addmap_core(struct drm_device *dev, resource_size_t offset, unsigned int size, enum drm_map_type type, enum drm_map_flags flags, struct drm_map_list **maplist)

    non-root process.

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param offset:
        *undescribed*
    :type offset: resource_size_t

    :param size:
        *undescribed*
    :type size: unsigned int

    :param type:
        *undescribed*
    :type type: enum drm_map_type

    :param flags:
        *undescribed*
    :type flags: enum drm_map_flags

    :param maplist:
        *undescribed*
    :type maplist: struct drm_map_list \*\*

.. _`drm_addmap_core.description`:

Description
-----------

Adjusts the memory offset to its absolute value according to the mapping
type.  Adds the map to the map list drm_device::maplist. Adds MTRR's where
applicable and if supported by the kernel.

.. _`drm_legacy_addmap_ioctl`:

drm_legacy_addmap_ioctl
=======================

.. c:function:: int drm_legacy_addmap_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    non-root process.

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param data:
        *undescribed*
    :type data: void \*

    :param file_priv:
        *undescribed*
    :type file_priv: struct drm_file \*

.. _`drm_legacy_addmap_ioctl.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg pointer to a drm_map structure.
\return zero on success or a negative value on error.

.. _`drm_legacy_rmmap_locked`:

drm_legacy_rmmap_locked
=======================

.. c:function:: int drm_legacy_rmmap_locked(struct drm_device *dev, struct drm_local_map *map)

    isn't in use.

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param map:
        *undescribed*
    :type map: struct drm_local_map \*

.. _`drm_legacy_rmmap_locked.description`:

Description
-----------

Searches the map on drm_device::maplist, removes it from the list, see if
its being used, and free any associate resource (such as MTRR's) if it's not
being on use.

\sa drm_legacy_addmap

.. _`drm_cleanup_buf_error`:

drm_cleanup_buf_error
=====================

.. c:function:: void drm_cleanup_buf_error(struct drm_device *dev, struct drm_buf_entry *entry)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param entry:
        *undescribed*
    :type entry: struct drm_buf_entry \*

.. _`drm_cleanup_buf_error.description`:

Description
-----------

\param dev DRM device.
\param entry buffer entry where the error occurred.

Frees any pages and buffers associated with the given entry.

.. _`drm_legacy_addbufs_agp`:

drm_legacy_addbufs_agp
======================

.. c:function:: int drm_legacy_addbufs_agp(struct drm_device *dev, struct drm_buf_desc *request)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param request:
        *undescribed*
    :type request: struct drm_buf_desc \*

.. _`drm_legacy_addbufs_agp.description`:

Description
-----------

\param dev struct drm_device to which the buffers are to be added.
\param request pointer to a struct drm_buf_desc describing the request.
\return zero on success or a negative number on failure.

After some sanity checks creates a drm_buf structure for each buffer and
reallocates the buffer list of the same size order to accommodate the new
buffers.

.. _`drm_legacy_addbufs`:

drm_legacy_addbufs
==================

.. c:function:: int drm_legacy_addbufs(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param data:
        *undescribed*
    :type data: void \*

    :param file_priv:
        *undescribed*
    :type file_priv: struct drm_file \*

.. _`drm_legacy_addbufs.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg pointer to a struct drm_buf_desc request.
\return zero on success or a negative number on failure.

According with the memory type specified in drm_buf_desc::flags and the
build options, it dispatches the call either to \ :c:func:`addbufs_agp`\ ,
\ :c:func:`addbufs_sg`\  or \ :c:func:`addbufs_pci`\  for AGP, scatter-gather or consistent
PCI memory respectively.

.. _`__drm_legacy_infobufs`:

\__drm_legacy_infobufs
======================

.. c:function:: int __drm_legacy_infobufs(struct drm_device *dev, void *data, int *p, int (*f)(void *, int, struct drm_buf_entry *))

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param data:
        *undescribed*
    :type data: void \*

    :param p:
        *undescribed*
    :type p: int \*

    :param int (\*f)(void \*, int, struct drm_buf_entry \*):
        *undescribed*

.. _`__drm_legacy_infobufs.description`:

Description
-----------

This was originally mean for debugging purposes, or by a sophisticated
client library to determine how best to use the available buffers (e.g.,
large buffers can be used for image transfer).

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg pointer to a drm_buf_info structure.
\return zero on success or a negative number on failure.

Increments drm_device::buf_use while holding the drm_device::buf_lock
lock, preventing of allocating more buffers after this call. Information
about each requested buffer is then copied into user space.

.. _`drm_legacy_markbufs`:

drm_legacy_markbufs
===================

.. c:function:: int drm_legacy_markbufs(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param data:
        *undescribed*
    :type data: void \*

    :param file_priv:
        *undescribed*
    :type file_priv: struct drm_file \*

.. _`drm_legacy_markbufs.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg a pointer to a drm_buf_desc structure.
\return zero on success or a negative number on failure.

Verifies that the size order is bounded between the admissible orders and
updates the respective drm_device_dma::bufs entry low and high water mark.

\note This ioctl is deprecated and mostly never used.

.. _`drm_legacy_freebufs`:

drm_legacy_freebufs
===================

.. c:function:: int drm_legacy_freebufs(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param data:
        *undescribed*
    :type data: void \*

    :param file_priv:
        *undescribed*
    :type file_priv: struct drm_file \*

.. _`drm_legacy_freebufs.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg pointer to a drm_buf_free structure.
\return zero on success or a negative number on failure.

Calls \ :c:func:`free_buffer`\  for each used buffer.
This function is primarily used for debugging.

.. _`__drm_legacy_mapbufs`:

\__drm_legacy_mapbufs
=====================

.. c:function:: int __drm_legacy_mapbufs(struct drm_device *dev, void *data, int *p, void __user **v, int (*f)(void *, int, unsigned long, struct drm_buf *), struct drm_file *file_priv)

    virtual space (ioctl).

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param data:
        *undescribed*
    :type data: void \*

    :param p:
        *undescribed*
    :type p: int \*

    :param v:
        *undescribed*
    :type v: void __user \*\*

    :param int (\*f)(void \*, int, unsigned long, struct drm_buf \*):
        *undescribed*

    :param file_priv:
        *undescribed*
    :type file_priv: struct drm_file \*

.. _`__drm_legacy_mapbufs.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg pointer to a drm_buf_map structure.
\return zero on success or a negative number on failure.

Maps the AGP, SG or PCI buffer region with \ :c:func:`vm_mmap`\ , and copies information
about each buffer into user space. For PCI buffers, it calls \ :c:func:`vm_mmap`\  with
offset equal to 0, which \ :c:func:`drm_mmap`\  interpretes as PCI buffers and calls
\ :c:func:`drm_mmap_dma`\ .

.. This file was automatic generated / don't edit.

