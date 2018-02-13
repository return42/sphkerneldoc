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

    :param struct drm_file \*file_private:
        drm file private pointer

    :param u32 handle:
        sync object handle to lookup.

.. _`drm_syncobj_find.description`:

Description
-----------

Returns a reference to the syncobj pointed to by handle or NULL. The
reference must be released by calling \ :c:func:`drm_syncobj_put`\ .

.. _`drm_syncobj_add_callback`:

drm_syncobj_add_callback
========================

.. c:function:: void drm_syncobj_add_callback(struct drm_syncobj *syncobj, struct drm_syncobj_cb *cb, drm_syncobj_func_t func)

    adds a callback to syncobj::cb_list

    :param struct drm_syncobj \*syncobj:
        Sync object to which to add the callback

    :param struct drm_syncobj_cb \*cb:
        Callback to add

    :param drm_syncobj_func_t func:
        Func to use when initializing the drm_syncobj_cb struct

.. _`drm_syncobj_add_callback.description`:

Description
-----------

This adds a callback to be called next time the fence is replaced

.. _`drm_syncobj_remove_callback`:

drm_syncobj_remove_callback
===========================

.. c:function:: void drm_syncobj_remove_callback(struct drm_syncobj *syncobj, struct drm_syncobj_cb *cb)

    removes a callback to syncobj::cb_list

    :param struct drm_syncobj \*syncobj:
        Sync object from which to remove the callback

    :param struct drm_syncobj_cb \*cb:
        Callback to remove

.. _`drm_syncobj_replace_fence`:

drm_syncobj_replace_fence
=========================

.. c:function:: void drm_syncobj_replace_fence(struct drm_syncobj *syncobj, struct dma_fence *fence)

    replace fence in a sync object.

    :param struct drm_syncobj \*syncobj:
        Sync object to replace fence in

    :param struct dma_fence \*fence:
        fence to install in sync file.

.. _`drm_syncobj_replace_fence.description`:

Description
-----------

This replaces the fence on a sync object.

.. _`drm_syncobj_find_fence`:

drm_syncobj_find_fence
======================

.. c:function:: int drm_syncobj_find_fence(struct drm_file *file_private, u32 handle, struct dma_fence **fence)

    lookup and reference the fence in a sync object

    :param struct drm_file \*file_private:
        drm file private pointer

    :param u32 handle:
        sync object handle to lookup.

    :param struct dma_fence \*\*fence:
        out parameter for the fence

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

    :param struct kref \*kref:
        kref to free.

.. _`drm_syncobj_free.description`:

Description
-----------

Only to be called from kref_put in drm_syncobj_put.

.. _`drm_syncobj_create`:

drm_syncobj_create
==================

.. c:function:: int drm_syncobj_create(struct drm_syncobj **out_syncobj, uint32_t flags, struct dma_fence *fence)

    create a new syncobj

    :param struct drm_syncobj \*\*out_syncobj:
        returned syncobj

    :param uint32_t flags:
        DRM_SYNCOBJ_* flags

    :param struct dma_fence \*fence:
        if non-NULL, the syncobj will represent this fence

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

    :param struct drm_file \*file_private:
        drm file private pointer

    :param struct drm_syncobj \*syncobj:
        Sync object to export

    :param u32 \*handle:
        out parameter with the new handle

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

    :param struct drm_syncobj \*syncobj:
        Sync object to export

    :param int \*p_fd:
        out parameter with the new file descriptor

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

    :param struct drm_file \*file_private:
        drm file-private structure to set up

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

    :param struct drm_file \*file_private:
        drm file-private structure to clean up

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

    :param int64_t timeout_nsec:
        timeout nsec component in ns, 0 for poll

.. _`drm_timeout_abs_to_jiffies.description`:

Description
-----------

Calculate the timeout in jiffies from an absolute time in sec/nsec.

.. This file was automatic generated / don't edit.

