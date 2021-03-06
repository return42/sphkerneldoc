.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_gem.c

.. _`drm_gem_init`:

drm_gem_init
============

.. c:function:: int drm_gem_init(struct drm_device *dev)

    Initialize the GEM device fields

    :param dev:
        drm_devic structure to initialize
    :type dev: struct drm_device \*

.. _`drm_gem_object_init`:

drm_gem_object_init
===================

.. c:function:: int drm_gem_object_init(struct drm_device *dev, struct drm_gem_object *obj, size_t size)

    initialize an allocated shmem-backed GEM object

    :param dev:
        drm_device the object should be initialized for
    :type dev: struct drm_device \*

    :param obj:
        drm_gem_object to initialize
    :type obj: struct drm_gem_object \*

    :param size:
        object size
    :type size: size_t

.. _`drm_gem_object_init.description`:

Description
-----------

Initialize an already allocated GEM object of the specified size with
shmfs backing store.

.. _`drm_gem_private_object_init`:

drm_gem_private_object_init
===========================

.. c:function:: void drm_gem_private_object_init(struct drm_device *dev, struct drm_gem_object *obj, size_t size)

    initialize an allocated private GEM object

    :param dev:
        drm_device the object should be initialized for
    :type dev: struct drm_device \*

    :param obj:
        drm_gem_object to initialize
    :type obj: struct drm_gem_object \*

    :param size:
        object size
    :type size: size_t

.. _`drm_gem_private_object_init.description`:

Description
-----------

Initialize an already allocated GEM object of the specified size with
no GEM provided backing store. Instead the caller is responsible for
backing the object and handling it.

.. _`drm_gem_object_handle_free`:

drm_gem_object_handle_free
==========================

.. c:function:: void drm_gem_object_handle_free(struct drm_gem_object *obj)

    release resources bound to userspace handles

    :param obj:
        GEM object to clean up.
    :type obj: struct drm_gem_object \*

.. _`drm_gem_object_handle_free.description`:

Description
-----------

Called after the last handle to the object has been closed

Removes any name for the object. Note that this must be
called before drm_gem_object_free or we'll be touching
freed memory

.. _`drm_gem_handle_delete`:

drm_gem_handle_delete
=====================

.. c:function:: int drm_gem_handle_delete(struct drm_file *filp, u32 handle)

    deletes the given file-private handle

    :param filp:
        drm file-private structure to use for the handle look up
    :type filp: struct drm_file \*

    :param handle:
        userspace handle to delete
    :type handle: u32

.. _`drm_gem_handle_delete.description`:

Description
-----------

Removes the GEM handle from the \ ``filp``\  lookup table which has been added with
\ :c:func:`drm_gem_handle_create`\ . If this is the last handle also cleans up linked
resources like GEM names.

.. _`drm_gem_dumb_map_offset`:

drm_gem_dumb_map_offset
=======================

.. c:function:: int drm_gem_dumb_map_offset(struct drm_file *file, struct drm_device *dev, u32 handle, u64 *offset)

    return the fake mmap offset for a gem object

    :param file:
        drm file-private structure containing the gem object
    :type file: struct drm_file \*

    :param dev:
        corresponding drm_device
    :type dev: struct drm_device \*

    :param handle:
        gem object handle
    :type handle: u32

    :param offset:
        return location for the fake mmap offset
    :type offset: u64 \*

.. _`drm_gem_dumb_map_offset.description`:

Description
-----------

This implements the \ :c:type:`drm_driver.dumb_map_offset <drm_driver>`\  kms driver callback for
drivers which use gem to manage their backing storage.

.. _`drm_gem_dumb_map_offset.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_gem_dumb_destroy`:

drm_gem_dumb_destroy
====================

.. c:function:: int drm_gem_dumb_destroy(struct drm_file *file, struct drm_device *dev, uint32_t handle)

    dumb fb callback helper for gem based drivers

    :param file:
        drm file-private structure to remove the dumb handle from
    :type file: struct drm_file \*

    :param dev:
        corresponding drm_device
    :type dev: struct drm_device \*

    :param handle:
        the dumb handle to remove
    :type handle: uint32_t

.. _`drm_gem_dumb_destroy.description`:

Description
-----------

This implements the \ :c:type:`drm_driver.dumb_destroy <drm_driver>`\  kms driver callback for drivers
which use gem to manage their backing storage.

.. _`drm_gem_handle_create_tail`:

drm_gem_handle_create_tail
==========================

.. c:function:: int drm_gem_handle_create_tail(struct drm_file *file_priv, struct drm_gem_object *obj, u32 *handlep)

    internal functions to create a handle

    :param file_priv:
        drm file-private structure to register the handle for
    :type file_priv: struct drm_file \*

    :param obj:
        object to register
    :type obj: struct drm_gem_object \*

    :param handlep:
        pointer to return the created handle to the caller
    :type handlep: u32 \*

.. _`drm_gem_handle_create_tail.description`:

Description
-----------

This expects the \ :c:type:`drm_device.object_name_lock <drm_device>`\  to be held already and will
drop it before returning. Used to avoid races in establishing new handles
when importing an object from either an flink name or a dma-buf.

Handles must be release again through \ :c:func:`drm_gem_handle_delete`\ . This is done
when userspace closes \ ``file_priv``\  for all attached handles, or through the
GEM_CLOSE ioctl for individual handles.

.. _`drm_gem_handle_create`:

drm_gem_handle_create
=====================

.. c:function:: int drm_gem_handle_create(struct drm_file *file_priv, struct drm_gem_object *obj, u32 *handlep)

    create a gem handle for an object

    :param file_priv:
        drm file-private structure to register the handle for
    :type file_priv: struct drm_file \*

    :param obj:
        object to register
    :type obj: struct drm_gem_object \*

    :param handlep:
        pionter to return the created handle to the caller
    :type handlep: u32 \*

.. _`drm_gem_handle_create.description`:

Description
-----------

Create a handle for this object. This adds a handle reference to the object,
which includes a regular reference count. Callers will likely want to
dereference the object afterwards.

Since this publishes \ ``obj``\  to userspace it must be fully set up by this point,
drivers must call this last in their buffer object creation callbacks.

.. _`drm_gem_free_mmap_offset`:

drm_gem_free_mmap_offset
========================

.. c:function:: void drm_gem_free_mmap_offset(struct drm_gem_object *obj)

    release a fake mmap offset for an object

    :param obj:
        obj in question
    :type obj: struct drm_gem_object \*

.. _`drm_gem_free_mmap_offset.description`:

Description
-----------

This routine frees fake offsets allocated by \ :c:func:`drm_gem_create_mmap_offset`\ .

Note that \ :c:func:`drm_gem_object_release`\  already calls this function, so drivers
don't have to take care of releasing the mmap offset themselves when freeing
the GEM object.

.. _`drm_gem_create_mmap_offset_size`:

drm_gem_create_mmap_offset_size
===============================

.. c:function:: int drm_gem_create_mmap_offset_size(struct drm_gem_object *obj, size_t size)

    create a fake mmap offset for an object

    :param obj:
        obj in question
    :type obj: struct drm_gem_object \*

    :param size:
        the virtual size
    :type size: size_t

.. _`drm_gem_create_mmap_offset_size.description`:

Description
-----------

GEM memory mapping works by handing back to userspace a fake mmap offset
it can use in a subsequent mmap(2) call.  The DRM core code then looks
up the object based on the offset and sets up the various memory mapping
structures.

This routine allocates and attaches a fake offset for \ ``obj``\ , in cases where
the virtual size differs from the physical size (ie. \ :c:type:`drm_gem_object.size <drm_gem_object>`\ ).
Otherwise just use \ :c:func:`drm_gem_create_mmap_offset`\ .

This function is idempotent and handles an already allocated mmap offset
transparently. Drivers do not need to check for this case.

.. _`drm_gem_create_mmap_offset`:

drm_gem_create_mmap_offset
==========================

.. c:function:: int drm_gem_create_mmap_offset(struct drm_gem_object *obj)

    create a fake mmap offset for an object

    :param obj:
        obj in question
    :type obj: struct drm_gem_object \*

.. _`drm_gem_create_mmap_offset.description`:

Description
-----------

GEM memory mapping works by handing back to userspace a fake mmap offset
it can use in a subsequent mmap(2) call.  The DRM core code then looks
up the object based on the offset and sets up the various memory mapping
structures.

This routine allocates and attaches a fake offset for \ ``obj``\ .

Drivers can call \ :c:func:`drm_gem_free_mmap_offset`\  before freeing \ ``obj``\  to release
the fake offset again.

.. _`drm_gem_get_pages`:

drm_gem_get_pages
=================

.. c:function:: struct page **drm_gem_get_pages(struct drm_gem_object *obj)

    helper to allocate backing pages for a GEM object from shmem

    :param obj:
        obj in question
    :type obj: struct drm_gem_object \*

.. _`drm_gem_get_pages.description`:

Description
-----------

This reads the page-array of the shmem-backing storage of the given gem
object. An array of pages is returned. If a page is not allocated or
swapped-out, this will allocate/swap-in the required pages. Note that the
whole object is covered by the page-array and pinned in memory.

Use \ :c:func:`drm_gem_put_pages`\  to release the array and unpin all pages.

This uses the GFP-mask set on the shmem-mapping (see \ :c:func:`mapping_set_gfp_mask`\ ).
If you require other GFP-masks, you have to do those allocations yourself.

Note that you are not allowed to change gfp-zones during runtime. That is,
\ :c:func:`shmem_read_mapping_page_gfp`\  must be called with the same gfp_zone(gfp) as
set during initialization. If you have special zone constraints, set them
after \ :c:func:`drm_gem_object_init`\  via \ :c:func:`mapping_set_gfp_mask`\ . shmem-core takes care
to keep pages in the required zone during swap-in.

.. _`drm_gem_put_pages`:

drm_gem_put_pages
=================

.. c:function:: void drm_gem_put_pages(struct drm_gem_object *obj, struct page **pages, bool dirty, bool accessed)

    helper to free backing pages for a GEM object

    :param obj:
        obj in question
    :type obj: struct drm_gem_object \*

    :param pages:
        pages to free
    :type pages: struct page \*\*

    :param dirty:
        if true, pages will be marked as dirty
    :type dirty: bool

    :param accessed:
        if true, the pages will be marked as accessed
    :type accessed: bool

.. _`drm_gem_object_lookup`:

drm_gem_object_lookup
=====================

.. c:function:: struct drm_gem_object *drm_gem_object_lookup(struct drm_file *filp, u32 handle)

    look up a GEM object from it's handle

    :param filp:
        DRM file private date
    :type filp: struct drm_file \*

    :param handle:
        userspace handle
    :type handle: u32

.. _`drm_gem_object_lookup.return`:

Return
------


A reference to the object named by the handle if such exists on \ ``filp``\ , NULL
otherwise.

.. _`drm_gem_close_ioctl`:

drm_gem_close_ioctl
===================

.. c:function:: int drm_gem_close_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    implementation of the GEM_CLOSE ioctl

    :param dev:
        drm_device
    :type dev: struct drm_device \*

    :param data:
        ioctl data
    :type data: void \*

    :param file_priv:
        drm file-private structure
    :type file_priv: struct drm_file \*

.. _`drm_gem_close_ioctl.description`:

Description
-----------

Releases the handle to an mm object.

.. _`drm_gem_flink_ioctl`:

drm_gem_flink_ioctl
===================

.. c:function:: int drm_gem_flink_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    implementation of the GEM_FLINK ioctl

    :param dev:
        drm_device
    :type dev: struct drm_device \*

    :param data:
        ioctl data
    :type data: void \*

    :param file_priv:
        drm file-private structure
    :type file_priv: struct drm_file \*

.. _`drm_gem_flink_ioctl.description`:

Description
-----------

Create a global name for an object, returning the name.

Note that the name does not hold a reference; when the object
is freed, the name goes away.

.. _`drm_gem_open_ioctl`:

drm_gem_open_ioctl
==================

.. c:function:: int drm_gem_open_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    implementation of the GEM_OPEN ioctl

    :param dev:
        drm_device
    :type dev: struct drm_device \*

    :param data:
        ioctl data
    :type data: void \*

    :param file_priv:
        drm file-private structure
    :type file_priv: struct drm_file \*

.. _`drm_gem_open_ioctl.description`:

Description
-----------

Open an object using the global name, returning a handle and the size.

This handle (of course) holds a reference to the object, so the object
will not go away until the handle is deleted.

.. _`drm_gem_open`:

drm_gem_open
============

.. c:function:: void drm_gem_open(struct drm_device *dev, struct drm_file *file_private)

    initalizes GEM file-private structures at devnode open time

    :param dev:
        drm_device which is being opened by userspace
    :type dev: struct drm_device \*

    :param file_private:
        drm file-private structure to set up
    :type file_private: struct drm_file \*

.. _`drm_gem_open.description`:

Description
-----------

Called at device open time, sets up the structure for handling refcounting
of mm objects.

.. _`drm_gem_release`:

drm_gem_release
===============

.. c:function:: void drm_gem_release(struct drm_device *dev, struct drm_file *file_private)

    release file-private GEM resources

    :param dev:
        drm_device which is being closed by userspace
    :type dev: struct drm_device \*

    :param file_private:
        drm file-private structure to clean up
    :type file_private: struct drm_file \*

.. _`drm_gem_release.description`:

Description
-----------

Called at close time when the filp is going away.

Releases any remaining references on objects by this filp.

.. _`drm_gem_object_release`:

drm_gem_object_release
======================

.. c:function:: void drm_gem_object_release(struct drm_gem_object *obj)

    release GEM buffer object resources

    :param obj:
        GEM buffer object
    :type obj: struct drm_gem_object \*

.. _`drm_gem_object_release.description`:

Description
-----------

This releases any structures and resources used by \ ``obj``\  and is the invers of
\ :c:func:`drm_gem_object_init`\ .

.. _`drm_gem_object_free`:

drm_gem_object_free
===================

.. c:function:: void drm_gem_object_free(struct kref *kref)

    free a GEM object

    :param kref:
        kref of the object to free
    :type kref: struct kref \*

.. _`drm_gem_object_free.description`:

Description
-----------

Called after the last reference to the object has been lost.
Must be called holding \ :c:type:`drm_device.struct_mutex <drm_device>`\ .

Frees the object

.. _`drm_gem_object_put_unlocked`:

drm_gem_object_put_unlocked
===========================

.. c:function:: void drm_gem_object_put_unlocked(struct drm_gem_object *obj)

    drop a GEM buffer object reference

    :param obj:
        GEM buffer object
    :type obj: struct drm_gem_object \*

.. _`drm_gem_object_put_unlocked.description`:

Description
-----------

This releases a reference to \ ``obj``\ . Callers must not hold the
\ :c:type:`drm_device.struct_mutex <drm_device>`\  lock when calling this function.

See also \ :c:func:`__drm_gem_object_put`\ .

.. _`drm_gem_object_put`:

drm_gem_object_put
==================

.. c:function:: void drm_gem_object_put(struct drm_gem_object *obj)

    release a GEM buffer object reference

    :param obj:
        GEM buffer object
    :type obj: struct drm_gem_object \*

.. _`drm_gem_object_put.description`:

Description
-----------

This releases a reference to \ ``obj``\ . Callers must hold the
\ :c:type:`drm_device.struct_mutex <drm_device>`\  lock when calling this function, even when the
driver doesn't use \ :c:type:`drm_device.struct_mutex <drm_device>`\  for anything.

For drivers not encumbered with legacy locking use
\ :c:func:`drm_gem_object_put_unlocked`\  instead.

.. _`drm_gem_vm_open`:

drm_gem_vm_open
===============

.. c:function:: void drm_gem_vm_open(struct vm_area_struct *vma)

    vma->ops->open implementation for GEM

    :param vma:
        VM area structure
    :type vma: struct vm_area_struct \*

.. _`drm_gem_vm_open.description`:

Description
-----------

This function implements the #vm_operations_struct \ :c:func:`open`\  callback for GEM
drivers. This must be used together with \ :c:func:`drm_gem_vm_close`\ .

.. _`drm_gem_vm_close`:

drm_gem_vm_close
================

.. c:function:: void drm_gem_vm_close(struct vm_area_struct *vma)

    vma->ops->close implementation for GEM

    :param vma:
        VM area structure
    :type vma: struct vm_area_struct \*

.. _`drm_gem_vm_close.description`:

Description
-----------

This function implements the #vm_operations_struct \ :c:func:`close`\  callback for GEM
drivers. This must be used together with \ :c:func:`drm_gem_vm_open`\ .

.. _`drm_gem_mmap_obj`:

drm_gem_mmap_obj
================

.. c:function:: int drm_gem_mmap_obj(struct drm_gem_object *obj, unsigned long obj_size, struct vm_area_struct *vma)

    memory map a GEM object

    :param obj:
        the GEM object to map
    :type obj: struct drm_gem_object \*

    :param obj_size:
        the object size to be mapped, in bytes
    :type obj_size: unsigned long

    :param vma:
        VMA for the area to be mapped
    :type vma: struct vm_area_struct \*

.. _`drm_gem_mmap_obj.description`:

Description
-----------

Set up the VMA to prepare mapping of the GEM object using the gem_vm_ops
provided by the driver. Depending on their requirements, drivers can either
provide a fault handler in their gem_vm_ops (in which case any accesses to
the object will be trapped, to perform migration, GTT binding, surface
register allocation, or performance monitoring), or mmap the buffer memory
synchronously after calling drm_gem_mmap_obj.

This function is mainly intended to implement the DMABUF mmap operation, when
the GEM object is not looked up based on its fake offset. To implement the
DRM mmap operation, drivers should use the \ :c:func:`drm_gem_mmap`\  function.

\ :c:func:`drm_gem_mmap_obj`\  assumes the user is granted access to the buffer while
\ :c:func:`drm_gem_mmap`\  prevents unprivileged users from mapping random objects. So
callers must verify access restrictions before calling this helper.

Return 0 or success or -EINVAL if the object size is smaller than the VMA
size, or if no gem_vm_ops are provided.

.. _`drm_gem_mmap`:

drm_gem_mmap
============

.. c:function:: int drm_gem_mmap(struct file *filp, struct vm_area_struct *vma)

    memory map routine for GEM objects

    :param filp:
        DRM file pointer
    :type filp: struct file \*

    :param vma:
        VMA for the area to be mapped
    :type vma: struct vm_area_struct \*

.. _`drm_gem_mmap.description`:

Description
-----------

If a driver supports GEM object mapping, mmap calls on the DRM file
descriptor will end up here.

Look up the GEM object based on the offset passed in (vma->vm_pgoff will
contain the fake offset we created when the GTT map ioctl was called on
the object) and map it with a call to \ :c:func:`drm_gem_mmap_obj`\ .

If the caller is not granted access to the buffer object, the mmap will fail
with EACCES. Please see the vma manager for more information.

.. This file was automatic generated / don't edit.

