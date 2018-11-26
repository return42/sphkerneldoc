.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_syncobj.c

.. _`overview`:

Overview
========

DRM synchronisation objects (syncobj, see struct \ :c:type:`struct drm_syncobj <drm_syncobj>`\ ) are
persistent objects that contain an optional fence. The fence can be updated
with a new fence, or be NULL.

syncobj's can be waited upon, where it will wait for the underlying
fence.

syncobj's can be export to fd's and back, these fd's are opaque and
have no other use case, except passing the syncobj between processes.

Their primary use-case is to implement Vulkan fences and semaphores.

syncobj have a kref reference count, but also have an optional file.
The file is only created once the syncobj is exported.
The file takes a reference on the kref.

.. _`drm_syncobj_find`:

drm_syncobj_find
================

.. c:function:: struct drm_syncobj *drm_syncobj_find(struct drm_file *file_private, u32 handle)

    lookup and reference a sync object.

    :param file_private:
        drm file private pointer
    :type file_private: struct drm_file \*

    :param handle:
        sync object handle to lookup.
    :type handle: u32

.. _`drm_syncobj_find.description`:

Description
-----------

Returns a reference to the syncobj pointed to by handle or NULL. The
reference must be released by calling \ :c:func:`drm_syncobj_put`\ .

.. _`drm_syncobj_replace_fence`:

drm_syncobj_replace_fence
=========================

.. c:function:: void drm_syncobj_replace_fence(struct drm_syncobj *syncobj, u64 point, struct dma_fence *fence)

    replace fence in a sync object.

    :param syncobj:
        Sync object to replace fence in
    :type syncobj: struct drm_syncobj \*

    :param point:
        timeline point
    :type point: u64

    :param fence:
        fence to install in sync file.
    :type fence: struct dma_fence \*

.. _`drm_syncobj_replace_fence.description`:

Description
-----------

This replaces the fence on a sync object, or a timeline point fence.

.. _`drm_syncobj_find_fence`:

drm_syncobj_find_fence
======================

.. c:function:: int drm_syncobj_find_fence(struct drm_file *file_private, u32 handle, u64 point, struct dma_fence **fence)

    lookup and reference the fence in a sync object

    :param file_private:
        drm file private pointer
    :type file_private: struct drm_file \*

    :param handle:
        sync object handle to lookup.
    :type handle: u32

    :param point:
        timeline point
    :type point: u64

    :param fence:
        out parameter for the fence
    :type fence: struct dma_fence \*\*

.. _`drm_syncobj_find_fence.description`:

Description
-----------

This is just a convenience function that combines \ :c:func:`drm_syncobj_find`\  and
\ :c:func:`drm_syncobj_fence_get`\ .

Returns 0 on success or a negative error value on failure. On success \ ``fence``\ 
contains a reference to the fence, which must be released by calling
\ :c:func:`dma_fence_put`\ .

.. _`drm_syncobj_free`:

drm_syncobj_free
================

.. c:function:: void drm_syncobj_free(struct kref *kref)

    free a sync object.

    :param kref:
        kref to free.
    :type kref: struct kref \*

.. _`drm_syncobj_free.description`:

Description
-----------

Only to be called from kref_put in drm_syncobj_put.

.. _`drm_syncobj_create`:

drm_syncobj_create
==================

.. c:function:: int drm_syncobj_create(struct drm_syncobj **out_syncobj, uint32_t flags, struct dma_fence *fence)

    create a new syncobj

    :param out_syncobj:
        returned syncobj
    :type out_syncobj: struct drm_syncobj \*\*

    :param flags:
        DRM_SYNCOBJ_* flags
    :type flags: uint32_t

    :param fence:
        if non-NULL, the syncobj will represent this fence
    :type fence: struct dma_fence \*

.. _`drm_syncobj_create.description`:

Description
-----------

This is the first function to create a sync object. After creating, drivers
probably want to make it available to userspace, either through
\ :c:func:`drm_syncobj_get_handle`\  or \ :c:func:`drm_syncobj_get_fd`\ .

Returns 0 on success or a negative error value on failure.

.. _`drm_syncobj_get_handle`:

drm_syncobj_get_handle
======================

.. c:function:: int drm_syncobj_get_handle(struct drm_file *file_private, struct drm_syncobj *syncobj, u32 *handle)

    get a handle from a syncobj

    :param file_private:
        drm file private pointer
    :type file_private: struct drm_file \*

    :param syncobj:
        Sync object to export
    :type syncobj: struct drm_syncobj \*

    :param handle:
        out parameter with the new handle
    :type handle: u32 \*

.. _`drm_syncobj_get_handle.description`:

Description
-----------

Exports a sync object created with \ :c:func:`drm_syncobj_create`\  as a handle on
\ ``file_private``\  to userspace.

Returns 0 on success or a negative error value on failure.

.. _`drm_syncobj_get_fd`:

drm_syncobj_get_fd
==================

.. c:function:: int drm_syncobj_get_fd(struct drm_syncobj *syncobj, int *p_fd)

    get a file descriptor from a syncobj

    :param syncobj:
        Sync object to export
    :type syncobj: struct drm_syncobj \*

    :param p_fd:
        out parameter with the new file descriptor
    :type p_fd: int \*

.. _`drm_syncobj_get_fd.description`:

Description
-----------

Exports a sync object created with \ :c:func:`drm_syncobj_create`\  as a file descriptor.

Returns 0 on success or a negative error value on failure.

.. _`drm_syncobj_open`:

drm_syncobj_open
================

.. c:function:: void drm_syncobj_open(struct drm_file *file_private)

    initalizes syncobj file-private structures at devnode open time

    :param file_private:
        drm file-private structure to set up
    :type file_private: struct drm_file \*

.. _`drm_syncobj_open.description`:

Description
-----------

Called at device open time, sets up the structure for handling refcounting
of sync objects.

.. _`drm_syncobj_release`:

drm_syncobj_release
===================

.. c:function:: void drm_syncobj_release(struct drm_file *file_private)

    release file-private sync object resources

    :param file_private:
        drm file-private structure to clean up
    :type file_private: struct drm_file \*

.. _`drm_syncobj_release.description`:

Description
-----------

Called at close time when the filp is going away.

Releases any remaining references on objects by this filp.

.. _`drm_timeout_abs_to_jiffies`:

drm_timeout_abs_to_jiffies
==========================

.. c:function:: signed long drm_timeout_abs_to_jiffies(int64_t timeout_nsec)

    calculate jiffies timeout from absolute value

    :param timeout_nsec:
        timeout nsec component in ns, 0 for poll
    :type timeout_nsec: int64_t

.. _`drm_timeout_abs_to_jiffies.description`:

Description
-----------

Calculate the timeout in jiffies from an absolute time in sec/nsec.

.. This file was automatic generated / don't edit.

