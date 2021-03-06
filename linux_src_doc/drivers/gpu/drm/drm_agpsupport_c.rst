.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_agpsupport.c

.. _`drm_agp_info`:

drm_agp_info
============

.. c:function:: int drm_agp_info(struct drm_device *dev, struct drm_agp_info *info)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param info:
        *undescribed*
    :type info: struct drm_agp_info \*

.. _`drm_agp_info.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg pointer to a (output) drm_agp_info structure.
\return zero on success or a negative number on failure.

Verifies the AGP device has been initialized and acquired and fills in the
drm_agp_info structure with the information in drm_agp_head::agp_info.

.. _`drm_agp_acquire`:

drm_agp_acquire
===============

.. c:function:: int drm_agp_acquire(struct drm_device *dev)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

.. _`drm_agp_acquire.description`:

Description
-----------

\param dev DRM device that is to acquire AGP.
\return zero on success or a negative number on failure.

Verifies the AGP device hasn't been acquired before and calls
\c agp_backend_acquire.

.. _`drm_agp_acquire_ioctl`:

drm_agp_acquire_ioctl
=====================

.. c:function:: int drm_agp_acquire_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param data:
        *undescribed*
    :type data: void \*

    :param file_priv:
        *undescribed*
    :type file_priv: struct drm_file \*

.. _`drm_agp_acquire_ioctl.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg user argument.
\return zero on success or a negative number on failure.

Verifies the AGP device hasn't been acquired before and calls
\c agp_backend_acquire.

.. _`drm_agp_release`:

drm_agp_release
===============

.. c:function:: int drm_agp_release(struct drm_device *dev)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

.. _`drm_agp_release.description`:

Description
-----------

\param dev DRM device that is to release AGP.
\return zero on success or a negative number on failure.

Verifies the AGP device has been acquired and calls \c agp_backend_release.

.. _`drm_agp_enable`:

drm_agp_enable
==============

.. c:function:: int drm_agp_enable(struct drm_device *dev, struct drm_agp_mode mode)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param mode:
        *undescribed*
    :type mode: struct drm_agp_mode

.. _`drm_agp_enable.description`:

Description
-----------

\param dev DRM device that has previously acquired AGP.
\param mode Requested AGP mode.
\return zero on success or a negative number on failure.

Verifies the AGP device has been acquired but not enabled, and calls
\c agp_enable.

.. _`drm_agp_alloc`:

drm_agp_alloc
=============

.. c:function:: int drm_agp_alloc(struct drm_device *dev, struct drm_agp_buffer *request)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param request:
        *undescribed*
    :type request: struct drm_agp_buffer \*

.. _`drm_agp_alloc.description`:

Description
-----------

\param inode device inode.
\param file_priv file private pointer.
\param cmd command.
\param arg pointer to a drm_agp_buffer structure.
\return zero on success or a negative number on failure.

Verifies the AGP device is present and has been acquired, allocates the
memory via \ :c:func:`agp_allocate_memory`\  and creates a drm_agp_mem entry for it.

.. _`drm_agp_lookup_entry`:

drm_agp_lookup_entry
====================

.. c:function:: struct drm_agp_mem *drm_agp_lookup_entry(struct drm_device *dev, unsigned long handle)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param handle:
        *undescribed*
    :type handle: unsigned long

.. _`drm_agp_lookup_entry.description`:

Description
-----------

\param dev DRM device structure.
\param handle AGP memory handle.
\return pointer to the drm_agp_mem structure associated with \p handle.

Walks through drm_agp_head::memory until finding a matching handle.

.. _`drm_agp_unbind`:

drm_agp_unbind
==============

.. c:function:: int drm_agp_unbind(struct drm_device *dev, struct drm_agp_binding *request)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param request:
        *undescribed*
    :type request: struct drm_agp_binding \*

.. _`drm_agp_unbind.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg pointer to a drm_agp_binding structure.
\return zero on success or a negative number on failure.

Verifies the AGP device is present and acquired, looks-up the AGP memory
entry and passes it to the \ :c:func:`unbind_agp`\  function.

.. _`drm_agp_bind`:

drm_agp_bind
============

.. c:function:: int drm_agp_bind(struct drm_device *dev, struct drm_agp_binding *request)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param request:
        *undescribed*
    :type request: struct drm_agp_binding \*

.. _`drm_agp_bind.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg pointer to a drm_agp_binding structure.
\return zero on success or a negative number on failure.

Verifies the AGP device is present and has been acquired and that no memory
is currently bound into the GATT. Looks-up the AGP memory entry and passes
it to \ :c:func:`bind_agp`\  function.

.. _`drm_agp_free`:

drm_agp_free
============

.. c:function:: int drm_agp_free(struct drm_device *dev, struct drm_agp_buffer *request)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param request:
        *undescribed*
    :type request: struct drm_agp_buffer \*

.. _`drm_agp_free.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg pointer to a drm_agp_buffer structure.
\return zero on success or a negative number on failure.

Verifies the AGP device is present and has been acquired and looks up the
AGP memory entry. If the memory it's currently bound, unbind it via
\ :c:func:`unbind_agp`\ . Frees it via \ :c:func:`free_agp`\  as well as the entry itself
and unlinks from the doubly linked list it's inserted in.

.. _`drm_agp_init`:

drm_agp_init
============

.. c:function:: struct drm_agp_head *drm_agp_init(struct drm_device *dev)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

.. _`drm_agp_init.description`:

Description
-----------

\return pointer to a drm_agp_head structure.

Gets the drm_agp_t structure which is made available by the agpgart module
via the inter_module\_\* functions. Creates and initializes a drm_agp_head
structure.

Note that final cleanup of the kmalloced structure is directly done in
drm_pci_agp_destroy.

.. _`drm_legacy_agp_clear`:

drm_legacy_agp_clear
====================

.. c:function:: void drm_legacy_agp_clear(struct drm_device *dev)

    Clear AGP resource list

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_legacy_agp_clear.description`:

Description
-----------

Iterate over all AGP resources and remove them. But keep the AGP head
intact so it can still be used. It is safe to call this if AGP is disabled or
was already removed.

Cleanup is only done for drivers who have DRIVER_LEGACY set.

.. _`drm_agp_bind_pages`:

drm_agp_bind_pages
==================

.. c:function:: struct agp_memory *drm_agp_bind_pages(struct drm_device *dev, struct page **pages, unsigned long num_pages, uint32_t gtt_offset, u32 type)

    the AGP memory structure containing them.

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param pages:
        *undescribed*
    :type pages: struct page \*\*

    :param num_pages:
        *undescribed*
    :type num_pages: unsigned long

    :param gtt_offset:
        *undescribed*
    :type gtt_offset: uint32_t

    :param type:
        *undescribed*
    :type type: u32

.. _`drm_agp_bind_pages.description`:

Description
-----------

No reference is held on the pages during this time -- it is up to the
caller to handle that.

.. This file was automatic generated / don't edit.

